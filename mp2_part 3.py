tasks = []


def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")


def add_task():
    task = input("Enter task description: ").strip()
    
    if task:
        tasks.append(task)
        print(f"Task added: '{task}'")
    else:
        print("Task description cannot be empty.")

def remove_task():
    task = input("Enter task description to remove: ").strip()
    if task in tasks:
        tasks.remove(task)
        print(f"Task removed: '{task}'")
    else:
        print("Task not found in the list.")

def view_tasks():
    if tasks:
        print("\nYour Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

main()