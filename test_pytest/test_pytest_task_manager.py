import pytest
from io import StringIO
from unittest.mock import patch
from main_program.task_manager import tasks, add_task, view_tasks, remove_task

@pytest.fixture
def reset_tasks():
    """Fixture to clear tasks before each test."""
    tasks.clear()

def test_add_task(reset_tasks):
    with patch('builtins.input', side_effect=['Task 1', 'Description for task 1', 'Deadline  for task 1', 'high']):
        add_task()
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Task 1'
    assert tasks[0]['description'] == 'Description for task 1'
    assert tasks[0]['deadline'] == 'Deadline  for task 1'
    assert tasks[0]['priority'] == 'high'

def test_view_tasks_empty(reset_tasks):
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        view_tasks()
    assert "Task list is empty." in captured_output.getvalue()

def test_view_tasks_with_tasks_and_priority(reset_tasks):
    with patch('builtins.input', side_effect=[
        'Task 1', 'Description for task 1', 'Deadline for task 1', 'high',
        'Task 2', 'Description for task 2', 'Deadline for task 2', 'medium']):
        add_task()
        add_task()

    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        view_tasks()

    output = captured_output.getvalue()

    assert "1. Task 1 - Description for task 1 - Deadline: Deadline for task 1 - Priority: high" in output
    assert "2. Task 2 - Description for task 2 - Deadline: Deadline for task 2 - Priority: medium" in output



def test_remove_task_valid(reset_tasks):
    with patch('builtins.input', side_effect=['Task 1', 'Description for task 1', 'Deadline  for task 1', 'high', 'Task 2', 'Description for task 2', 'Deadline  for task 2', 'high', '1']):
        add_task()
        add_task()
        remove_task()
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Task 2'

    # Remove the remaining task
    with patch('builtins.input', side_effect=['1']):
        remove_task()
    assert len(tasks) == 0
    captured_output = StringIO()
    with patch('sys.stdout', new=captured_output):
        view_tasks()
    assert "Task list is empty." in captured_output.getvalue()

def test_remove_task_invalid(reset_tasks):
    with patch('builtins.input', side_effect=['Task 1', 'Description for task 1', 'Deadline  for task 1', 'high', '3']):
        add_task()
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            remove_task()
    assert "Invalid task number." in captured_output.getvalue()
    assert len(tasks) == 1  # Ensure the task wasn't removed
