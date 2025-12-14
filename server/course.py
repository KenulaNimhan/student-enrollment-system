class Course:

    # constructor
    def __init__(self, subject, tutor, courseId=None):
        self.courseId = courseId
        self.subject = subject
        self.tutor = tutor

    def __str__(self) -> str:
        return f'Course Details\nsubject: {self.subject}\ntutor: {self.tutor}'

    def __repr__(self) -> str:
        return self.__str__()
