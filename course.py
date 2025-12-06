class Course:

    # define constructor
    def __init__(self, subject, tutor):
        self.courseId = None
        self.subject = subject
        self.tutor = tutor

    # setter methods
    def set_courseId(self, id):
        self.courseId = id

    def __str__(self) -> str:
        return f'Course Details\nsubject: {self.subject}\ntutor: {self.tutor}'
