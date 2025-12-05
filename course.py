class Course:

    # define constructor
    def __init__(self, subject, tutor):
        self.subject = subject
        self.tutor = tutor

    def __str__(self) -> str:
        return f'Course Details\nsubject: {self.subject}\ntutor: {self.tutor}'
