import unittest
from student import *

class TestStudentSetters(unittest.TestCase):

    # SET AGE

    def test_setting_age_below_18(self):
        test_student = Student("John")
        with self.assertRaises(ValueError):
            test_student.set_age(17)

    def test_setting_age_above_40(self):
        test_student = Student("John")
        with self.assertRaises(ValueError):
            test_student.set_age(42)

    def test_setting_valid_age(self):
        test_student = Student("John")
        test_student.set_age(23)

        self.assertEqual(test_student.age, 23)

    # SET EMAIL

    def test_setting_invalid_email(self):
        test_student = Student("John")
        invalid_email = "john123.com"

        with self.assertRaises(ValueError):
            test_student.set_email(invalid_email)

    def test_setting_valid_email(self):
        test_student = Student("John")
        valid_email = "john@gmail.com"

        test_student.set_email(valid_email)
        self.assertEqual(test_student.email, valid_email)

    # SET PASSWORD

    def test_setting_invalid_password(self):
        test_student = Student("John")
        invalid_password = "1234"

        with self.assertRaises(ValueError):
            test_student.set_password(invalid_password)

    def test_setting_valid_password(self):
        test_student = Student("John")
        valid_password = "123456"

        test_student.set_password(valid_password)
        self.assertEqual(test_student.password, valid_password)

if __name__ == '__main__':
    unittest.main()