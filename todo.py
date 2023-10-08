# todo.py

tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
def main():
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()
