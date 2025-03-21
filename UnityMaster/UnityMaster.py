import pyodbc

# Database connection details
connection_string = r'DRIVER={SQL Server};SERVER=DESKTOP-1B1FLGB\MASTERSQL;DATABASE=UnitMasterDB;Trusted_Connection=yes'


def get_student_info(student_id):
    """
    Fetch student information from the database.

    Args:
        student_id (str): The ID of the student.

    Returns:
        tuple: A tuple containing student information if found, otherwise None.
    """
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students WHERE StudentID = ?", student_id)
        return cursor.fetchone()


def get_available_courses():
    """
    Fetch all available courses from the database.

    Returns:
        list: A list of tuples containing course information.
    """
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Courses")
        return cursor.fetchall()


def save_selected_courses(student_id, selected_courses):
    """
    Save the selected courses to the database in the SelectedCourses table.

    Args:
        student_id (str): The ID of the student.
        selected_courses (list): A list of course codes selected by the student.
    """
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        for course_code in selected_courses:
            try:
                cursor.execute("""
                    INSERT INTO SelectedCourses (StudentID, CourseCode)
                    VALUES (?, ?)
                """, student_id, course_code)
            except pyodbc.IntegrityError as e:
                print(f"Error: Invalid StudentID or CourseCode. Details: {e}")
                return
        conn.commit()  # Commit the transaction to save changes


def get_max_units(gpa):
    """
    Determine the maximum allowed units based on the student's GPA.

    Args:
        gpa (float): The GPA of the student.

    Returns:
        int: The maximum number of units the student can enroll in.
    """
    if gpa >= 17:
        return 24
    elif 14 <= gpa < 17:
        return 20
    else:
        return 12


def main():
    """
    Main function to handle the course selection process.
    """
    # Get student ID from user
    while True:
        id_user = input('Enter your student ID: ')
        student_info = get_student_info(id_user)

        if student_info:
            break  # Exit loop if student is found
        else:
            print('Error: This ID was not found! Please try again.\n')

    # Fetch available courses
    courses = get_available_courses()

    # Display available courses
    print('\nAvailable courses:')
    course_dict = {}
    for course in courses:
        course_dict[int(course.CourseCode)] = course.Units  # Convert CourseCode to int
        print(f'Code: {course.CourseCode} --- Course Name: {course.CourseName} --- Units: {course.Units}')

    # Calculate maximum allowed units based on GPA
    gpa = float(student_info.GPA)
    max_units = get_max_units(gpa)

    # Display student information
    print(
        f'\nYour information: ID: {student_info.StudentID} --- Name: {student_info.FirstName} {student_info.LastName} --- GPA: {gpa}')
    print(f'You can select up to {max_units} units.')

    # Get selected courses from user
    while True:
        selected_courses = input(
            '\nEnter the codes of the courses you want to select, separated by commas: ').strip().split(',')

        try:
            # Convert course codes to integers
            selected_courses = [int(code.strip()) for code in selected_courses]
        except ValueError:
            print('Error: Please enter valid course codes (numbers only).')
            continue

        # Check if all selected courses exist
        invalid_courses = [code for code in selected_courses if code not in course_dict]
        if invalid_courses:
            print(f'Error: The following course codes are invalid: {invalid_courses}. Please try again.')
            continue

        # Calculate total units of selected courses
        total_units = sum(course_dict[code] for code in selected_courses)

        # Check if total units are within the allowed limit
        if total_units <= max_units and total_units > 0:
            break  # Exit loop if units are valid
        elif total_units <= 0:
            print('Error: Please select at least one unit!')
        else:
            print(f'Error: The total units ({total_units}) exceed the allowed limit ({max_units})! Please try again.')

    # Save selected courses to the database
    save_selected_courses(id_user, selected_courses)
    print('\nCourse selection was successful. Your selections have been saved to the database.')


if __name__ == '__main__':
    main()