# Task Manager

## Overview

The Task Manager is a simple command-line application for managing tasks. It allows users to add, view, and remove tasks through a console interface. This project demonstrates basic operations with task management and includes unit tests using both `unittest` and `pytest`.

## Project Structure

The project directory is organized as follows:
TaskManager/ 
│ 
├── main_program/ 
│ └── task_manager.py # Main application code 
│ 
├── tests_pytest/ 
│ └── test_pytest_task_manager.py # Pytest unit tests 
│ 
├── tests_unittest/ 
│ └── test_unittest_task_manager.py # Unittest unit tests

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
   Running the Application
   bash
2. To run the application, execute the following command:
python main_program/task_manager.py
Running Tests
Using unittest
3. To run the unit tests with unittest, execute the following command:

python -m unittest discover -s tests_unittest
Using pytest
To run the tests with pytest, execute the following command:
pytest tests_pytest