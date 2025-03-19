UnitMaster: A Smart Course Selection System 🎓

UnitMaster is an intuitive and interactive Python-based application designed to simplify the course selection process for students. It allows students to manage their academic units efficiently by providing a user-friendly interface to select courses, check unit limits based on GPA, and save their selections for future reference.
Key Features ✨

    GPA-Based Unit Limits: The system automatically calculates the maximum number of units a student can enroll in based on their GPA.

    Interactive Course Selection: Students can view available courses, select their desired ones, and get real-time feedback on their choices.

    Error Handling: The system provides clear warnings and prompts if the student exceeds the allowed unit limit or enters invalid course codes, allowing them to correct their inputs without restarting the process.

    Data Persistence: Selected courses are saved in a personalized text file for easy access and record-keeping.

    User-Friendly: Designed with simplicity in mind, UnitMaster ensures a smooth experience for students of all technical levels.

How It Works 🛠️

    Enter Student ID: The system verifies the student's identity using a preloaded database (students.txt).

    View Available Courses: Students can browse through a list of courses loaded from courses.txt, including course codes, names, and unit counts.

    Select Courses: Students enter the codes of the courses they wish to enroll in, separated by commas.

    Validation: The system checks if the selected courses are valid and ensures the total units do not exceed the GPA-based limit.

    Save Selections: Once validated, the selected courses are saved in a text file named after the student's ID.

Why UnitMaster? 🌟

    Efficiency: Streamlines the course selection process, saving time for both students and administrators.

    Flexibility: Allows students to experiment with different course combinations and receive instant feedback.

    Transparency: Clear rules for unit limits based on GPA ensure fairness and compliance with academic policies.

    Open Source: Fully customizable and open-source, making it easy for institutions to adapt and extend the system to their needs.

Getting Started 🚀
Prerequisites

    Python 3.x

    Git (optional, for cloning the repository)

Installation

    Clone the repository:
    bash
    Copy

    git clone https://github.com/your-username/UnitMaster.git

    Navigate to the project directory:
    bash
    Copy

    cd UnitMaster

    Ensure the required text files (students.txt and courses.txt) are properly formatted and placed in the project directory.

Usage

    Run the script:
    bash
    Copy

    python course_selection.py

    Follow the on-screen prompts to select courses and save your selections.

Contributing 🤝

We welcome contributions! If you'd like to improve UnitMaster, please follow these steps:

    Fork the repository.

    Create a new branch for your feature or bugfix.

    Commit your changes.

    Submit a pull request with a detailed description of your changes.
