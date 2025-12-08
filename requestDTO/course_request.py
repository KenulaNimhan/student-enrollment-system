from pydantic import BaseModel

# THIS DTO IS USED FOR ANY ENROLLMENTS OR DISENROLLMENT (REMOVALS) REQUESTS
class CourseReq(BaseModel):
    student_id: int
    course_id: int