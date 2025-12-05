# IMPORTS
from os import getenv
from dotenv import load_dotenv
from mssql_python import connect

# OTHER IMPORTS
# from student import Student

# ESTABLISH CONNECTION
load_dotenv()
conn = connect(getenv("SQL_CONNECTION_STRING"))
cursor = conn.cursor()


# DATABASE METHODS

    # CREATE METHODS
def register_student(student):
    """
    registers student by creating a new record in the database.
    :param student: newly registered student
    :return: none
    """
    query = f"""
INSERT INTO Students (Name, Age, Email, Password)
VALUES ('{student.name}', {student.age}, '{student.email}', '{student.password}')
"""
    try:
        cursor.execute(query)
        conn.commit()
    except Exception:
        print('Student registration unsuccessful')

def enroll(studentId, courseId):
    query = f"""
INSERT INTO Enrollments (StudentId, CourseId)
VALUES ({studentId}, {courseId})
"""
    try:
        cursor.execute(query)
        conn.commit()
    except Exception:
        print('Enrollment failed')

    # READ METHODS
def fetch_and_print_student_list():
    query = "SELECT * FROM Students"
    cursor.execute(query)
    records = cursor.fetchall()
    print("STUDENTS\n--------")
    for r in records:
        print(f'id = {r.StudentId} / name = {r.Name} / age = {r.Age} / email = {r.Email} / password = {r.Password}')

def fetch_and_print_course_list():
    query = "SELECT * FROM Courses"
    cursor.execute(query)
    records = cursor.fetchall()
    print("COURSES\n--------")
    for r in records:
        print(f'id = {r.CourseId} / subject = {r.Subject} / tutor = {r.Tutor}')

def fetch_and_print_enrollments():
    query = "SELECT * FROM Enrollments"
    cursor.execute(query)
    records = cursor.fetchall()
    print("ENROLLMENTS\n-----------")
    for r in records:
        print(f'{r.StudentId} -> {r.CourseId}')

def fetch_enrolled_courses_of_student(studentId):
    query = f"SELECT * FROM Enrollments WHERE StudentId={studentId}"

    # DELETE METHODS
def disenroll_from_course(studentId, courseId):
    query = f"DELETE FROM Enrollments WHERE StudentId={studentId} AND CourseId={courseId}"

    try:
        cursor.execute(query)
        conn.commit()
    except Exception:
        print("Operation unsuccessful")