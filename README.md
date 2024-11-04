# Student Management System

A simple console-based Student Management System implemented in Python using a Binary Search Tree (BST) for efficient data storage and retrieval.

## Features

- **Add Student Details**: Add new student records with roll number, name, department, course, and CGPA.
- **Search Student Details**: Search for student records by roll number.
- **Display Student Details**: Display all student records or filter by department or course.
- **Delete Student Details**: Delete student records by roll number.
- **Automatic Tree Balancing**: Automatically restructures the BST for improved efficiency after every 10 insertions.

## Technologies Used

- Python

## How to Run

1. Ensure you have Python installed on your system.
2. Copy the code into a Python file, e.g., `student_management_system.py`.
3. Run the script using the command:
   ```bash
   python student_management_system.py
   ```

## Usage

1. The program will display a menu with options to add, search, display, and delete student details.
2. Enter the corresponding number to choose an option.
3. Follow the prompts to enter student details or search criteria.
4. The program will display the results or perform the requested action.

## Example

```
 _______________________________________________________________________________________________________
                                                STUDENT MANAGEMENT SYSTEM
 -------------------------------------------------------------------------------------------------------
[---------------MENU---------------]
    1.  Add Student Details:
    2.  Search Student Details:
    3.  Display Student:
    4.  Delete Student Details:
    5.  Exit:
----------------------------------
Enter your choice: 1
 ---------------------------------
                        ADDING...
Roll Number: 1
Name: John Doe
Department: Computer Science
Course: B.Tech
CGPA: 3.8
```

## Directory Structure

```
student_management_system.py  # Main script file
```

## License

This project is available under the MIT License.
