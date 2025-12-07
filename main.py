from fastapi import FastAPI
import database

app = FastAPI()

@app.get("/")
def root():
    return "App started"

# GET

@app.get("/student/details")
def get_details_of_student(student_id):
    return database.fetch_details_of_student(student_id)

@app.get("/students/enrolled-in-course/{course_id}")
def get_students_enrolled_in_course(course_id):
    return database.fetch_names_of_enrolled_students(course_id)


@app.get("/courses")
def get_all_courses():
    return database.fetch_all_courses()

@app.get("/courses/enrolled-by-student")
def get_enrolled_courses(student_id):
    return database.fetch_enrolled_courses_of_student(student_id)

# POST