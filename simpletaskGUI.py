import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    messagebox.showinfo("Success", f'Added task: {task}')
    view_tasks()

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        messagebox.showinfo("Success", f'Deleted task: {removed_task["task"]}')
        view_tasks()
    except IndexError:
        messagebox.showwarning("Error", "Invalid task number")

def view_tasks():
    task_list.delete(0, tk.END)
    if not tasks:
        task_list.insert(tk.END, "No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            task_list.insert(tk.END, f'{i + 1}. {task["task"]} [{status}]')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        messagebox.showinfo("Success", f'Marked task as completed: {tasks[task_index]["task"]}')
        view_tasks()
    except IndexError:
        messagebox.showwarning("Error", "Invalid task number")

def add_task_gui():
    task = task_entry.get()
    if task:
        add_task(task)
    else:
        messagebox.showwarning("Error", "Please enter a task")

def delete_task_gui():
    task_index = delete_entry.get()
    if task_index.isdigit():
        delete_task(int(task_index) - 1)
    else:
        messagebox.showwarning("Error", "Invalid task number")

def complete_task_gui():
    task_index = complete_entry.get()
    if task_index.isdigit():
        mark_task_completed(int(task_index) - 1)
    else:
        messagebox.showwarning("Error", "Invalid task number")

# Create the main window
root = tk.Tk()
root.title("Task Manager")

# Create frames
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

view_frame = tk.Frame(root)
view_frame.pack(pady=10)

delete_frame = tk.Frame(root)
delete_frame.pack(pady=10)

complete_frame = tk.Frame(root)
complete_frame.pack(pady=10)

# Add task widgets
tk.Label(add_frame, text="Task:").grid(row=0, column=0)
task_entry = tk.Entry(add_frame)
task_entry.grid(row=0, column=1)
tk.Button(add_frame, text="Add Task", command=add_task_gui).grid(row=1, columnspan=2, pady=5)

# View tasks widget
task_list = tk.Listbox(view_frame, width=50)
task_list.pack()

# Delete task widgets
tk.Label(delete_frame, text="Task Number to Delete:").grid(row=0, column=0)
delete_entry = tk.Entry(delete_frame)
delete_entry.grid(row=0, column=1)
tk.Button(delete_frame, text="Delete Task", command=delete_task_gui).grid(row=1, columnspan=2, pady=5)

# Complete task widgets
tk.Label(complete_frame, text="Task Number to Complete:").grid(row=0, column=0)
complete_entry = tk.Entry(complete_frame)
complete_entry.grid(row=0, column=1)
tk.Button(complete_frame, text="Complete Task", command=complete_task_gui).grid(row=1, columnspan=2, pady=5)

# Initial view of tasks
view_tasks()

# Run the application
root.mainloop()