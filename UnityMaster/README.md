UnitMaster: Course Selection System
Description

UnitMaster is a Python-based course selection system designed to help students manage their academic course enrollments efficiently. The program allows students to:

    View available courses.

    Select courses based on their GPA and unit limits.

    Save their course selections to a database for future reference.

The system ensures that students cannot exceed the maximum allowed units based on their GPA, providing a seamless and error-free course selection experience.
Features

    GPA-Based Unit Limits: Automatically calculates the maximum number of units a student can enroll in based on their GPA.

    Interactive Course Selection: Students can view available courses and select their desired ones.

    Database Integration: Course selections are saved in a SQL Server database for persistent storage.

    Error Handling: Provides clear warnings for invalid course codes or exceeding unit limits.

Requirements

To run this program, you need the following:

    Python 3.x: Download and install Python from python.org.

    SQL Server: Ensure you have access to a SQL Server instance.

    pyodbc: A Python library for connecting to SQL Server. Install it using pip.

Installation

Follow these steps to set up and run the UnitMaster program:
1. Clone the Repository

First, clone the repository to your local machine:

    git clone https://github.com/masoudarabzade/UnitMaster.git
    cd UnitMaster

2. Install Dependencies

Install the required Python libraries using pip:

    pip install -r requirements.txt

3. Set Up the Database

    Open SQL Server Management Studio (SSMS) and connect to your SQL Server instance.

    Create a new database named UnitMasterDB.

    Run the database_schema.sql script to create the necessary tables (Students, Courses, and SelectedCourses).

    Optionally, run the sample_data.sql script to populate the database with sample data.

4. Configure the Connection String

Update the connection_string variable in the UnitMaster.py file with your SQL Server details:

    connection_string = r'DRIVER={SQL Server};SERVER=your_server_name;DATABASE=UnitMasterDB;Trusted_Connection=yes'

Replace your_server_name with the name of your SQL Server instance.
5. Run the Program

Execute the program using Python:

    python UnitMaster.py

How It Works

    Enter Student ID: The program prompts the user to enter their student ID. It verifies the ID against the Students table in the database.

    View Available Courses: The program displays a list of available courses from the Courses table.

    Select Courses: The user enters the course codes they wish to enroll in, separated by commas.

    Validate Selections: The program checks if the selected courses are valid and ensures the total units do not exceed the GPA-based limit.

    Save Selections: The selected courses are saved to the SelectedCourses table in the database.

Database Schema

The database consists of three tables:

    Students:

        StudentID (Primary Key)

        FirstName

        LastName

        GPA

    Courses:

        CourseCode (Primary Key)

        CourseName

        Units

    SelectedCourses:

        StudentID (Foreign Key referencing Students)

        CourseCode (Foreign Key referencing Courses)

Sample Data

The sample_data.sql file includes sample data for testing:

    Students:

        1, John, Doe, 18.5

        2, Jane, Smith, 16.0

    Courses:

        101, Introduction to Programming, 3

        102, Data Structures, 4

    SelectedCourses:

        1, 101

        1, 102

Contributing

We welcome contributions to improve UnitMaster! If you'd like to contribute, please follow these steps:

    Fork the repository.

    Create a new branch for your feature or bugfix.

    Commit your changes.

    Submit a pull request with a detailed description of your changes.


Enjoy using UnitMaster! 🎓