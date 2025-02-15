import sys
from datetime import datetime

tasks = []

def add_task(task, year, days, priority, difficulty):
    tasks.append({"task": task, "year": year, "days": days, "priority": priority, "difficulty": difficulty, "completed": False})
    print(f'Added task: {task}')

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(f'Deleted task: {removed_task["task"]}')
    except IndexError:
        print("Invalid task number")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f'{i + 1}. {task["task"]} [Year: {task["year"]}, Days: {task["days"]}, Priority: {task["priority"]}, Difficulty: {task["difficulty"]}, Status: {status}]')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        print(f'Marked task as completed: {tasks[task_index]["task"]}')
    except IndexError:
        print("Invalid task number")

def show_help():
    print("""
    Available commands:
    - add <task> <year> <days> <priority> <difficulty>: Add a new task
    - delete <task_number>: Delete a task by its number
    - view: View all tasks
    - complete <task_number>: Mark a task as completed
    - help: Show this help message
    - exit: Exit the application
    """)

def main():
    print("Task Manager Application")
    show_help()
    while True:
        command = input("Enter command: ").strip().split()
        if not command:
            continue
        if command[0] == "add":
            if len(command) > 5:
                task = " ".join(command[1:-4])
                year = command[-4]
                days = command[-3]
                priority = command[-2]
                difficulty = command[-1]
                add_task(task, year, days, priority, difficulty)
            else:
                print("Please provide a task, year, days, priority, and difficulty.")
        elif command[0] == "delete":
            if len(command) > 1 and command[1].isdigit():
                delete_task(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif command[0] == "view":
            view_tasks()
        elif command[0] == "complete":
            if len(command) > 1 and command[1].isdigit():
                mark_task_completed(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif command[0] == "help":
            show_help()
        elif command[0] == "exit":
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()