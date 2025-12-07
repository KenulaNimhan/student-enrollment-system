from fastapi import APIRouter
import database

router = APIRouter(prefix="/courses")

@router.get("")
def get_all_courses():
    return database.fetch_all_courses()

@router.get("/student/enrolled-courses")
def get_enrolled_courses(student_id):
    return database.fetch_enrolled_courses_of_student(student_id)
