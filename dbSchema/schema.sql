USE EnrollmentSystem;

CREATE TABLE Students (
    StudentId INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age INT,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(50) NOT NULL
);

CREATE TABLE Courses (
    CourseId INT IDENTITY(1,1) PRIMARY KEY,
    Subject VARCHAR(50) UNIQUE NOT NULL,
    Tutor VARCHAR(50) NOT NULL
);

CREATE TABLE Enrollments (
    StudentId INT NOT NULL,
    CourseId INT NOT NULL,
    FOREIGN KEY (StudentId) REFERENCES Students(StudentId),
    FOREIGN KEY (CourseId) REFERENCES Courses(CourseId),
    PRIMARY KEY (StudentId, CourseId)
);