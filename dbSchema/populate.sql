USE EnrollmentSystem;
GO

INSERT INTO Students (Name, Age, Email, Password)
VALUES
('Mark Roberts', 24, 'markr@gmail.com', 'mark123'),
('Julia Roberts', 19, 'julia@gmail.com', 'julia123'),
('Alice Johnson', 30, 'alicej@gmail.com', 'alice123'),
('Bob Smith', 27, 'bobsmith@gmail.com', 'bob123'),
('Clara Lee', 22, 'claralee@gmail.com', 'clara123'),
('David Brown', 35, 'davidb@gmail.com', 'david123'),
('Eva Green', 28, 'evagreen@gmail.com', 'eva123');
GO

INSERT INTO Courses (Subject, Tutor)
VALUES
('Combined Maths', 'Mr. Tharindu Hasith'),
('Physics', 'Ms. Anushka Perera'),
('Chemistry', 'Mr. Nimal Fernando'),
('Biology', 'Ms. Sanduni Jayasuriya'),
('English', 'Mr. Kasun Wijesinghe'),
('History', 'Ms. Chamari Silva'),
('Geography', 'Mr. Arjuna Perera'),
('Computer Science', 'Ms. Nilusha Fernando'),
('Sinhala', 'Mr. Ruwan Jayawardena'),
('Tamil', 'Ms. Priya Kumarasinghe'),
('Art', 'Mr. Sameera Wickramasinghe');
GO