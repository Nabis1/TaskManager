import json
tasks = []

def main_menu():
    while True:
        print("\nTask Manager - Main Menu")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Edit task")
        print("5. Save tasks")
        print("6. Load tasks")
        print("7. Exit the program")
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            load_tasks()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

def add_task():
    while True:
        title = input("Enter the task title: ").strip()
        if not title:
            print("Task title cannot be empty.")
            continue
        description = input("Enter the task description: ").strip()
        if not description:
            print("Task description cannot be empty.")
            continue
        deadline = input("Enter the task deadline(DD.MM.YYYY): ")
        if not deadline:
            print("Task deadline cannot be empty")
            continue
        tasks.append({'title': title, 'description': description, 'deadline': deadline})
        print(f"Task '{title}' has been added.")
        break

def view_tasks():
    if not tasks:
        print("Task list is empty.")
    else:
        print("\nTask list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['description']} - Deadline: {task['deadline']}")

def edit_task():
    view_tasks()
    if not tasks:
        print("No tasks available to edit.")
        return
    
    try:
        task_number = int(input("Enter the task number you want to edit: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            print(f"Editing task: {task['title']}")
            
            new_title = input("Enter the new title (leave empty to keep current): ").strip()
            if new_title:
                task['title'] = new_title
            
            new_description = input("Enter the new description (leave empty to keep current): ").strip()
            if new_description:
                task['description'] = new_description
            
            new_deadline = input("Enter the new deadline (DD.MM.YYYY) (leave empty to keep current): ").strip()
            if new_deadline:
                task['deadline'] = new_deadline
            
            print(f"Task updated to: {task['title']} - {task['description']} (Deadline: {task['deadline']})")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input, please enter a number.")

def remove_task():
    view_tasks()
    if tasks:
        try:
            number = int(input("Enter the task number to remove: "))
            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                print(f"Task '{removed_task['title']}' has been removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input, please enter a task number.")
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks have been saved to tasks.json.")

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks have been loaded from tasks.json.")
    except FileNotFoundError:
        print("No saved tasks found.")

if __name__ == "__main__":
    main_menu()