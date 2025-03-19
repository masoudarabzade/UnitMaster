def load_students(students):
    """Load student data from a file."""
    with open('students.txt', 'r') as file:
        return [line.strip().split(',') for line in file]


def load_courses(courses):
    """Load course data from a file."""
    with open('courses.txt', 'r') as file:
        return [line.strip().split(',') for line in file]


def get_max_units(gpa):
    """Determine the maximum allowed units based on GPA."""
    if gpa >= 17:
        return 24
    elif 14 <= gpa < 17:
        return 20
    else:
        return 12


def main():
    # Get student ID from user
    while True:
        id_user = input('Enter your student ID: ')
        students = load_students('students.txt')
        student_info = None

        # Find the student by ID
        for student in students:
            if student[0] == id_user:
                student_info = student
                break

        if student_info:
            break  # Exit loop if student is found
        else:
            print('This ID was not found!\nPlease try again.\n')

    # Load course data
    courses = load_courses('courses.txt')

    # Display available courses
    print('\nAvailable courses:')
    course_dict = {}
    for course in courses:
        course_dict[course[0]] = int(course[2])  # Store course code and units
        print(f'Code: {course[0]} --- Course Name: {course[1]} --- Units: {course[2]}')

    # Calculate maximum allowed units based on GPA
    gpa = float(student_info[3])
    max_units = get_max_units(gpa)

    # Display student information
    print(f'\nYour information: ID: {student_info[0]} --- Name: {student_info[1]} {student_info[2]} --- GPA: {gpa}')
    print(f'You can select up to {max_units} units.')

    # Get selected courses from user
    while True:
        selected_courses = input(
            '\nEnter the codes of the courses you want to select, separated by commas: ').strip().split(',')

        # Check if all selected courses exist
        invalid_courses = [code for code in selected_courses if code not in course_dict]
        if invalid_courses:
            print(f'The following course codes are invalid: {invalid_courses}.\nPlease try again.')
            continue

        # Calculate total units of selected courses
        total_units = sum(course_dict[code] for code in selected_courses)

        # Check if total units are within the allowed limit
        if total_units <= max_units and total_units > 0:
            break  # Exit loop if units are valid
        elif total_units <= 0:
            print('Please select at least one unit!')
        else:
            print(f'The total units ({total_units}) exceed the allowed limit ({max_units})!\nPlease try again.')

    # Save selected courses to a file
    with open(f'{id_user}.txt', 'w') as file:
        file.write(f'ID: {id_user}, Selected Courses: {selected_courses}, Total Units: {total_units}')
    print('\nCourse selection was successful. Your selections have been saved.')


if __name__ == '__main__':
    main()