FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from the text file."""
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.read().splitlines()
        return tasks

    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    """Add a new task."""
    task = input("Enter your new task: ").strip()

    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")

    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n========== YOUR TO-DO LIST ==========")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("=====================================")


def delete_task(tasks):
    """Delete a completed task."""
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter the task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task deleted: {removed_task}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Display the menu and handle user choices."""
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST MANAGER ==========")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a completed task")
        print("4. Exit")
        print("========================================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Thank you for using the To-Do List Manager!")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


if __name__ == "__main__":
    main()
