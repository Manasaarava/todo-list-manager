tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, task)

def remove_task():
    view_tasks()
    num = int(input("Enter task number to remove: "))
    
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        print("Removed:", removed)
    else:
        print("Invalid number")

while True:
    print("\n---- To-Do List Manager ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
