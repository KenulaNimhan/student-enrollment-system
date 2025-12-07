@router.get("/student/details")
def get_details_of_student(student_id):
    return database.fetch_details_of_student(student_id)