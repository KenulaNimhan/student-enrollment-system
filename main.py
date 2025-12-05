from student import *
import database

def run():
    database.fetch_and_print_student_list()
    database.fetch_and_print_course_list()

    database.enroll(1,2)

    print("enrolled...")

    database.fetch_and_print_enrollments()

    database.disenroll_from_course(1,2)

    database.fetch_and_print_enrollments()


    print("disenrolled...")

if __name__ == "__main__":
    run()