USE UnitMasterDB;

-- Create Students table
CREATE TABLE Students (
    StudentID NVARCHAR(50) PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    GPA FLOAT
);

-- Create Courses table
CREATE TABLE Courses (
    CourseCode INT PRIMARY KEY,
    CourseName NVARCHAR(100),
    Units INT
);

-- Create SelectedCourses table
CREATE TABLE SelectedCourses (
    StudentID NVARCHAR(50),
    CourseCode INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseCode) REFERENCES Courses(CourseCode)
);