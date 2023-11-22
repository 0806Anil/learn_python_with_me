tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def complete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task marked as completed.")
    else:
        print("Task not found.")

def display_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main program
while True:
    print("\n1. Add Task\n2. Complete Task\n3. Display Tasks\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to complete: ")
        complete_task(task)
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
