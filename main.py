from fastapi import FastAPI, HTTPException
import database
from database import fetch_user
from requestDTO.login_request import LoginReq
from student import Student
from requestDTO.register_request import RegisterReq
from requestDTO.course_request import CourseReq

app = FastAPI()

@app.get("/")
def root():
    return "App started"

# GET

@app.get("/all-courses")
def get_all_courses():
    return database.fetch_all_courses()

    # expects a query parameter

@app.get("/student-details")
def get_details_of_student(student_id: int):
    return database.fetch_details_of_student(student_id)

@app.get("/course-students")
def get_students_enrolled_in_course(course_id: int):
    return database.fetch_names_of_enrolled_students(course_id)

@app.get("/enrolled-courses")
def get_enrolled_courses(student_id: int):
    return database.fetch_enrolled_courses_of_student(student_id)

@app.get("/unenrolled-courses")
def get_unenrolled_courses(student_id: int):
    return database.fetch_un_enrolled_courses_of_student(student_id)

@app.get("/get-password")
def get_password(email: str):
    return database.fetch_user(email)

# POST

@app.post("/login")
def login(request: LoginReq):
    user = fetch_user(request.email)
    if user is None:
        return HTTPException(status_code=400, detail="invalid email")
    elif user.password == request.password:
        user.password = None
        return user
    else:
        return "invalid password"


@app.post("/register-student")
def register_student(request: RegisterReq):
    new_student = Student(request.name)
    try:
        new_student.set_age(request.age)
        new_student.set_email(request.email)
        new_student.set_password(request.password)
        database.register_student(new_student)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return new_student

@app.post("/enroll")
def enroll(request: CourseReq):
    try:
        database.enroll(request.student_id, request.course_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return "Enrollment Successful"

# DELETE

@app.delete("/disenroll")
def disenroll(request: CourseReq):
    try:
        database.disenroll_from_course(request.student_id, request.course_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return "Removed from course success"
