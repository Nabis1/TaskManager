# Test Scenarios for Task Manager Project

## Feature 1: Main Menu (`main_menu`)

### Scenario 1: Valid User Input
- **Given** the user starts the task manager
- **When** the user selects a valid option (1-7)
- **Then** the corresponding function should be called:
  - Option `1`: Calls `add_task()`.
  - Option `2`: Calls `view_task()`.
  - Option `3`: Calls `remove_task()`.
  - Option `4`: Calls `edit_task()`.
  - Option `5`: Calls `save_task()`.
  - Option `6`: Calls `load_task()`.
  - Option `7`: Exits the program.

### Scenario 2: Invalid User Input
- **Given** the user is in the main menu
- **When** the user selects an invalid option (e.g., `0`, `8`, `abc`)
- **Then** the program should display an error message and re-display the menu.

---

## Feature 2: Add Task (`add_task`)

### Scenario 1: Valid Task Addition
- **Given** the user selects option `1` to add a task
- **When** the user provides a valid task name and description
- **Then** the task should be added to the list and a success message should be displayed.

### Scenario 2: Empty Task Name
- **Given** the user selects option `1` to add a task
- **When** the user provides an empty task name (e.g., `""`)
- **Then** the program should display an error message and prompt the user to re-enter the task name.

### Scenario 3: Empty Task Description
- **Given** the user selects option `1` to add a task
- **When** the user provides an empty task description (e.g., `""`)
- **Then** the program should display an error message and prompt the user to re-enter the task description.

### Scenario 4: Both Task Name and Description Empty
- **Given** the user selects option `1` to add a task
- **When** the user provides both empty task name and description
- **Then** the program should prompt the user to re-enter both fields.

---

## Feature 3: View Tasks (`veiw_task`)

### Scenario 1: Viewing Non-Empty Task List
- **Given** there are tasks in the list
- **When** the user selects option `2` to view tasks
- **Then** all tasks should be displayed with their corresponding number, name, and description.

### Scenario 2: Viewing Empty Task List
- **Given** there are no tasks in the list
- **When** the user selects option `2` to view tasks
- **Then** the program should display a message stating "The task list is empty."

---

## Feature 4: Remove Task (`remove_task`)

### Scenario 1: Valid Task Deletion
- **Given** there are tasks in the list
- **When** the user selects option `3` and provides a valid task number
- **Then** the selected task should be removed from the list and a success message should be displayed.

### Scenario 2: Task Deletion from Empty List
- **Given** there are no tasks in the list
- **When** the user selects option `3`
- **Then** the program should display a message stating "The task list is empty" and return to the main menu.

### Scenario 3: Invalid Task Number
- **Given** there are tasks in the list
- **When** the user selects option `3` and provides an invalid task number (e.g., `0`, `5` when there are only 3 tasks)
- **Then** the program should display an error message stating "Invalid task number" and prompt the user again.

### Scenario 4: Non-Numeric Task Input
- **Given** there are tasks in the list
- **When** the user selects option `3` and provides a non-numeric input (e.g., `abc`)
- **Then** the program should display an error message stating "Invalid input, please enter a number" and prompt the user again.

---

## Feature 5: Edit Task (`edit_task`)

### Scenario 1: Valid Task Edit
- **Given** the user selects option `4` to edit a task
- **When** the user provides a valid task index and updates the task details
- **Then** the task should be updated in the list and a success message should be displayed.

### Scenario 2: Invalid Task Index
- **Given** the user selects option `4` to edit a task
- **When** the user provides an invalid task index (e.g., index out of range)
- **Then** the program should display an error message and prompt the user to re-enter the index.

---

## Feature 6: Save Tasks (`save_tasks`)

### Scenario 1: Successful Task Saving
- **Given** the user selects option `5` to save tasks
- **When** there are tasks in the list
- **Then** the tasks should be saved to a file and a success message displayed.

## Scenario 2: No Tasks to Save
- **Given** the user selects option `5` to save tasks
- **When** the task list is empty
- **Then** the program should display a message indicating there are no tasks to save.

---

## Feature 7: Load Tasks (`load_tasks`)

### Scenario 1: Successful Task Loading
- **Given** the user selects option `6` to load tasks
- **When** a valid file with tasks is present
- **Then** the tasks should be loaded from the file and displayed in the task list.

### Scenario 2: No Tasks in File
- **Given** the user selects option `6` to load tasks
- **When** the file is empty or doesn't contain valid tasks
- **Then** the program should display a message indicating no tasks were loaded.

### Scenario 3: File Not Found
- **Given** the user selects option `6` to load tasks
- **When** the file is not found
- **Then** the program should display an error message indicating the file could not be located.

---

## Feature 8: Exit Program (`main_menu`)

### Scenario 1: Valid Exit
- **Given** the user selects option `7`
- **When** the user confirms their choice
- **Then** the program should display "Exiting the program" and exit cleanly.

### Scenario 2: Unexpected Exit Attempt
- **Given** the user is in the middle of adding or removing a task
- **When** the user tries to exit by force (e.g., closing the terminal or using Ctrl+C)
- **Then** the program should save the current state (if applicable) and exit safely without corruption.

---

## Edge Cases

### Edge Case 1: Long Task Names and Descriptions
- **Given** the user adds a task with an extremely long name or description
- **When** the user submits the task
- **Then** the task should be stored and displayed properly without truncation or errors.

### Edge Case 2: Whitespace Handling
- **Given** the user adds a task with only whitespace as the name or description
- **When** the user submits the task
- **Then** the program should display an error and request proper input.

### Edge Case 3: Concurrent Actions
- **Given** the user adds multiple tasks quickly in succession
- **When** tasks are added or deleted
- **Then** the system should handle multiple requests without lag or data corruption.
