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
    adds a new record to the 'Students' table.
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
        print("Student registration unsuccessful")

def enroll(studentId, courseId):
    """
    enrolls student to a specific course.
    creates a new record in the 'Enrollments' table
    :param studentId: id of the student joining
    :param courseId: id of the enrolling course
    :return: none
    """
    query = f"""
    INSERT INTO Enrollments (StudentId, CourseId)
    VALUES ({studentId}, {courseId})
    """
    try:
        cursor.execute(query)
        conn.commit()
    except Exception:
        print("Enrollment failed")

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

def fetch_and_print_enrolled_course_details(studentId):
    # collecting ids of enrolled courses
    query = f"""
    SELECT * FROM Courses
    FULL JOIN Enrollments
    ON Enrollments.CourseId = Courses.CourseId
    WHERE StudentId={studentId}
    """

    cursor.execute(query)
    records = cursor.fetchall()
    for r in records:
        print(f'courseId= {r.CourseId} / subject = {r.Subject} / tutor = {r.Tutor}')


def fetch_enrolled_courses_of_student(studentId) -> list:

    # collecting ids of enrolled courses
    query = f"""
    SELECT Courses.CourseId, Courses.Subject, Courses.Tutor FROM Courses
    FULL JOIN Enrollments
    ON Enrollments.CourseId = Courses.CourseId
    WHERE StudentId={studentId}
    """
    enrolled_courses = []
    cursor.execute(query)
    records = cursor.fetchall()
    for r in records:
        enrolled_courses.append(r)

    return enrolled_courses

def fetch_not_enrolled_courses_of_student(studentId) -> list:

    # collecting all course ids
    query = "SELECT CourseId FROM Courses"
    all_courses = []
    cursor.execute(query)
    records = cursor.fetchall()
    for r in records:
        all_courses.append(r)

    # collecting ids of enrolled courses
    query = f"SELECT CourseId FROM Enrollments WHERE StudentId={studentId}"
    enrolled_courses = []
    cursor.execute(query)
    records = cursor.fetchall()
    for r in records:
        enrolled_courses.append(r)

    # filtering out un-enrolled courses for the student
    for id in enrolled_courses:
        all_courses.remove(id)

    return all_courses


    # DELETE METHODS
def disenroll_from_course(studentId, courseId):
    """
    Cancels the enrollment of a student in a course.
    Deletes the pertaining record from 'Enrollments' table
    :param studentId: id of the student requesting removal from course.
    :param courseId: id of the course
    :return: none
    """
    query = f"DELETE FROM Enrollments WHERE StudentId={studentId} AND CourseId={courseId}"
    try:
        cursor.execute(query)
        conn.commit()
    except Exception:
        print("Operation unsuccessful")