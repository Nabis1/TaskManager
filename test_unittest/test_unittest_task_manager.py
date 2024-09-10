import unittest
import sys
from unittest.mock import patch
from io import StringIO
from main_program.task_manager import tasks, add_task, view_tasks, remove_task

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Reset the tasks list before each test."""
        tasks.clear()

    @patch('builtins.input', side_effect=['Task 1', 'Description for task 1', 'Deadline for task 1'])
    def test_add_task(self, mock_input):
        add_task()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Task 1')
        self.assertEqual(tasks[0]['description'], 'Description for task 1')
        self.assertEqual(tasks[0]['deadline'], 'Deadline for task 1')

    def test_view_tasks_empty(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        view_tasks()
        sys.stdout = sys.__stdout__
        self.assertIn("Task list is empty.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['Task 1', 'Description for task 1', 'Deadline for task 1', 'Task 2', 'Description for task 2', 'Deadline for task 2'])
    def test_view_tasks_with_tasks(self, mock_input):
        add_task()
        add_task()
        captured_output = StringIO()
        sys.stdout = captured_output
        view_tasks()
        sys.stdout = sys.__stdout__
        self.assertIn("1. Task 1 - Description for task 1 - Deadline: Deadline for task 1", captured_output.getvalue())
        self.assertIn("2. Task 2 - Description for task 2 - Deadline: Deadline for task 2", captured_output.getvalue())

    @patch('builtins.input', side_effect=['Task 1', 'Description for task 1', 'Deadline for task 1', 'Task 2', 'Description for task 2', 'Deadline for task 2', '1'])
    def test_remove_task_valid(self, mock_input):
        add_task()
        add_task()
        remove_task()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Task 2')

        # Remove the remaining task
        with patch('builtins.input', side_effect=['1']):
            remove_task()
        self.assertEqual(len(tasks), 0)
        captured_output = StringIO()
        sys.stdout = captured_output
        view_tasks()
        sys.stdout = sys.__stdout__
        self.assertIn("Task list is empty.", captured_output.getvalue())

    @patch('builtins.input', side_effect=['Task 1', 'Description for task 1', 'Deadline for task 1', '3'])
    def test_remove_task_invalid(self, mock_input):
        add_task()
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_task()
        sys.stdout = sys.__stdout__
        self.assertIn("Invalid task number.", captured_output.getvalue())
        self.assertEqual(len(tasks), 1)  # Ensure the task wasn't removed

if __name__ == "__main__":
    unittest.main()
