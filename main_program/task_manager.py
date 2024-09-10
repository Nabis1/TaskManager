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

        match choice:
            case "1":
                add_task()
            case "2":
                view_tasks()
            case "3":
                remove_task()
            case "4":
                edit_task()
            case "5":
                save_tasks()
            case "6":
                load_tasks()
            case "7":
                print("Exiting the program.")
                break
            case _:
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
        tasks.append({"title": title, "description": description, "deadline": deadline})
        print(f"Task '{title}' has been added.")
        break


def view_tasks():
    if not tasks:
        print("Task list is empty.")
    else:
        print("\nTask list:")
        for index, task in enumerate(tasks, start=1):
            print(
                f"{index}. {task['title']} - {task['description']} - Deadline: {task['deadline']}"
            )


def edit_task():
    if not tasks:
        print("No tasks available to edit.")
        return

    while True:
        try:
            index = int(input("Enter the task number to edit: "))
            if 1 <= index <= len(tasks):
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    task = tasks[index - 1]

    title = input(f"Enter new title (leave empty to keep '{task['title']}'): ").strip()
    description = input(
        f"Enter new description (leave empty to keep '{task['description']}'): "
    ).strip()
    deadline = input(
        f"Enter new deadline (leave empty to keep '{task['deadline']}'): "
    ).strip()

    if title:
        task["title"] = title
    if description:
        task["description"] = description
    if deadline:
        task["deadline"] = deadline

    print(
        f"Task updated to: {task['title']} - {task['description']} - Deadline: {task['deadline']}"
    )


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
