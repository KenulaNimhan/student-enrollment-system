from pydantic import BaseModel

# THIS DTO IS USED FOR ANY ENROLLMENTS OR DISENROLLMENTS (REMOVALS)
class CourseReq(BaseModel):
    student_id: int = None
    course_id: int = None