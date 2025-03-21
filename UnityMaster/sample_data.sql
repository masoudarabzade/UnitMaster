USE UnitMasterDB;

-- Insert sample data into Students
INSERT INTO Students (StudentID, FirstName, LastName, GPA)
VALUES
('1', 'John', 'Doe', 18.5),
('2', 'Jane', 'Smith', 16.0);

-- Insert sample data into Courses
INSERT INTO Courses (CourseCode, CourseName, Units)
VALUES
(101, 'Introduction to Programming', 3),
(102, 'Data Structures', 4);

-- Insert sample data into SelectedCourses
INSERT INTO SelectedCourses (StudentID, CourseCode)
VALUES
('1', 101),
('2', 102);