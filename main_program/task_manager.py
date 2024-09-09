tasks = []

def main_menu():
    while True:
        print("\nTask Manager - Main Menu")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Exit the program")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
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
        tasks.append({'title': title, 'description': description})
        print(f"Task '{title}' has been added.")
        break

def view_tasks():
    if not tasks:
        print("Task list is empty.")
    else:
        print("\nTask list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['description']}")

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

if __name__ == "__main__":
    main_menu()