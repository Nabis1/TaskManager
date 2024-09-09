# Task Manager

## Overview

The Task Manager is a simple command-line application for managing tasks. It allows users to add, view, and remove tasks through a console interface. This project demonstrates basic operations with task management and includes unit tests using both `unittest` and `pytest`.

## Features

- **Add a New Task**: Allows the user to enter a task title and description, which are then added to the task list.
- **View All Tasks**: Displays all tasks with their titles and descriptions.
- **Remove a Task**: Enables the user to remove a task by specifying its number in the list.
- **Exit the Program**: Ends the program execution.

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nabis1/TaskManager.git
   ```
2. To run the application, execute the following command:
   ```bash
   python main_program/task_manager.py
   ```
   
### Running Tests
#### Using unittest
1. To run the unit tests with unittest, execute the following command:
   ```bash
   python -m unittest discover -s tests_unittest
   ```

#### Using pytest
1. To run the tests with pytest, execute the following command:
   ```bash
   pytest test_pytest
   ```

## Code Structure
main_program/task_manager.py
This file contains the main implementation of the Task Manager with the following functions:

- main_menu(): Displays the main menu and handles user choices.
- add_task(): Adds a new task to the list.
- view_tasks(): Displays all tasks.
- remove_task(): Removes a task by its number.

  
Contains tests for the Task Manager using pytest. It verifies the functionality of adding, viewing, and removing tasks.
 - tests_pytest/test_pytest_task_manager.py

Contains tests for the Task Manager using unittest. It also verifies the functionality of adding, viewing, and removing tasks.
- tests_unittest/test_unittest_task_manager.py
   
   
