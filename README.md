# Student Management System

## Overview
The Student Management System is a simple console-based application that allows users to manage student details such as roll number, name, department, course, and CGPA. This application uses a Binary Search Tree (BST) to store and manage the student records efficiently.

## Features
1. **Add Student Details**: Add new student records to the system.
2. **Search Student Details**: Search for a student by their roll number.
3. **Display Student**: Display student records based on department, course, or all records.
4. **Delete Student Details**: Delete a student record by roll number.
5. **Exit**: Exit the application.

## Requirements
- Python 3.x

## How to Use

1. **Run the Application**:
   ```bash
   python student_management_system.py
   ```

2. **Menu Options**:
   - The main menu will be displayed with the following options:
     ```plaintext
     [---------------MENU---------------]
        1.      Add Student Details:
        2.      Search Student Details:
        3.      Display Student:
        4.      Delete Student Details:
        5.      Exit:
     ----------------------------------
     ```

3. **Adding Student Details**:
   - Select option `1` to add a new student.
   - Enter the student details when prompted:
     - Roll Number
     - Name
     - Department
     - Course
     - CGPA
   - The student record will be added to the BST.

4. **Searching Student Details**:
   - Select option `2` to search for a student.
   - Enter the roll number of the student to search.
   - If found, the student's details will be displayed.

5. **Displaying Student Records**:
   - Select option `3` to display student records.
   - You can choose to display records based on department, course, or all records:
     - Enter `1` to display by department and provide the department name.
     - Enter `2` to display by course and provide the course name.
     - Any other input will display all student records.

6. **Deleting Student Details**:
   - Select option `4` to delete a student.
   - Enter the roll number of the student to delete.
   - If the student is found, their record will be deleted from the BST.

7. **Exiting the Application**:
   - Select option `5` to exit the application.

## Code Explanation

### Main Function
The main function controls the flow of the application. It continuously displays the menu and handles user input for different operations.

### Node Class
The `Node` class represents a node in the BST. Each node stores student details and references to its left and right child nodes.

### BST Functions
- **Insert**: Inserts a new student record into the BST. If the roll number already exists, the user is prompted to update the existing record.
- **Search**: Searches for a student by roll number in the BST.
- **Delete**: Deletes a student record from the BST.
- **Inorder**: Traverses the BST in inorder fashion to display all student records.
- **Display by Department**: Displays student records for a specific department.
- **Display by Course**: Displays student records for a specific course.
- **Rebalance Tree**: Rebalances the BST after every 10 insertions to maintain efficiency.

### Sample Output
```plaintext
 _______________________________________________________________________________________________________
                                                        STUDENT MANAGEMENT SYSTEM                                                                 
 -------------------------------------------------------------------------------------------------------

[---------------MENU---------------]
        1.      Add Student Details:
        2.      Search Student Details:
        3.      Display Student:
        4.      Delete Student Details:
        5.      Exit:
----------------------------------
Enter your choice: 1
---------------------------------
                        ADDING...
Roll Number: 101
Name: John Doe
Department: Computer Science
Course: Data Structures
CGPA: 9.0

[---------------MENU---------------]
        1.      Add Student Details:
        2.      Search Student Details:
        3.      Display Student:
        4.      Delete Student Details:
        5.      Exit:
----------------------------------
Enter your choice: 3
---------------------------------
                        DISPLAY
Note:- if above choice not selected all would be printed
1. Department
2. Course
->
DATABASE
Roll Number       Name                Department         Course              CGPA
101                       John Doe               Computer Science     Data Structures         9.0
     -              -                     -                 -                  -
```

## Conclusion
The Student Management System provides a simple and efficient way to manage student records using a Binary Search Tree. It supports adding, searching, displaying, and deleting student details, making it a useful tool for educational institutions.
