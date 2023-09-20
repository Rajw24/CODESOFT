import tkinter as tk
from tkinter import messagebox



class todo_app:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title("To-Do")

        self.create_task_entry()
        self.create_add_button()
        self.create_list_box()
        self.create_remove_task()
    
    # Function to add a task
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    # Function to remove a selected task
    def remove_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            self.task_listbox.delete(selected_task)

    # Create and configure the task entry field
    def create_task_entry(self):
        self.task_entry = tk.Entry(self.window, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.focus()

    # Create and configure the "Add Task" button
    def create_add_button(self):
        self.add_button = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_button.pack()

    # Create and configure the task listbox
    def create_list_box(self):
        self.task_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE, width=40)
        self.task_listbox.pack(pady=10)

    # Create and configure the "Remove Task" button
    def create_remove_task(self):
        self.remove_button = tk.Button(self.window, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

    # Run the tkinter main loop
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = todo_app()
    app.run()