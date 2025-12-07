# IMPORTS
from os import getenv
from dotenv import load_dotenv
from mssql_python import connect, DatabaseError

# OTHER IMPORTS
from student import Student
from course import Course

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
    except DatabaseError as e:
        cursor.rollback()
        raise Exception("Database Error"+str(e))


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
    except DatabaseError as e:
        cursor.rollback()
        raise Exception("Database Error" + str(e))

    # READ METHODS
def fetch_all_courses() -> list:
    """
    fetches list of all courses from Courses table
    :return: subject names of all the courses
    """
    query = f"SELECT Subject FROM Courses"
    cursor.execute(query)
    records = cursor.fetchall()
    all_courses = []
    for r in records:
        all_courses.append(r.Subject)

    return all_courses

def fetch_details_of_student(student_id) -> Student:
    """
    fetch details (name, age, email, password) of student from Student table
    :param student_id: requesting student
    :return: requested Student object
    """
    query = f"SELECT * FROM Students WHERE StudentId={student_id}"
    cursor.execute(query)
    r = cursor.fetchone()

    # creating student object form fetched record
    fetched_student = Student(r.Name, r.Age, r.Email, r.Password)
    fetched_student.set_studentId(r.StudentId)

    return fetched_student

def fetch_names_of_enrolled_students(course_id) -> list:
    """
    :param course_id: identifier of the course
    :return: list of names of students enrolled
    """
    query = f"""
    SELECT Students.Name FROM Students
    FULL JOIN Enrollments
    ON Enrollments.StudentId = Students.StudentId
    WHERE Enrollments.CourseId={course_id}
    """
    cursor.execute(query)
    records = cursor.fetchall()
    student_names = []
    for r in records:
        student_names.append(r.Name)

    return student_names

def fetch_enrolled_courses_of_student(studentId) -> list:
    """
    fetches the enrolled course details from the database given the student id
    :param studentId: id of the requester
    :return: list of enrolled courses
    """

    # collecting ids of enrolled courses
    query = f"""
    SELECT Courses.CourseId, Courses.Subject, Courses.Tutor FROM Courses
    FULL JOIN Enrollments
    ON Enrollments.CourseId = Courses.CourseId
    WHERE StudentId={studentId}
    """
    enrolled_courses: list[Course] = []
    cursor.execute(query)
    records = cursor.fetchall()
    for r in records:
        course = Course(r.Subject, r.Tutor, r.CourseId)
        enrolled_courses.append(course)

    return enrolled_courses

def fetch_not_enrolled_courses_of_student(studentId) -> list:
    """
    :param studentId: identifier of student
    :return: list of courses the student is not enrolled in
    """

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
    except DatabaseError as e:
        cursor.rollback()
        raise Exception("Database Error" + str(e))