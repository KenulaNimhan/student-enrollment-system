from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

import database
from database import fetch_user
from requestDTO.login_request import LoginReq
from student import Student
from requestDTO.register_request import RegisterReq
from requestDTO.course_request import CourseReq

app = FastAPI()

origins = ["http://localhost:5173","http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

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
    if user is None or user.password != request.password:
        raise HTTPException(status_code=400, detail="invalid email or password")
    return user.studentId


@app.post("/register-student")
def register_student(request: RegisterReq):
    new_student = Student(request.name)
    try:
        new_student.set_age(request.age)
        new_student.set_email(request.email)
        new_student.set_password(request.password)
        database.register_student(new_student)
    except ValueError as e:
        raise HTTPException(status_code=400, detail="invalid data. please try again")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str("registration unsuccessful. try again"))

    return "registration successful. please login."

@app.post("/enroll")
def enroll(request: CourseReq):
    try:
        database.enroll(request.student_id, request.course_id)
    except Exception as e:
        print(str(e))
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
