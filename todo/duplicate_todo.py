from tkinter import *
from PIL import Image, ImageTk

def open_text(): 
    with open("list.dat", "r") as file:
        content = file.readlines()
        for task in content:
            tasks.insert(END, task.strip() + "\n")

def get_input():
    user_input = entry.get()
    if user_input:
        with open("list.dat", 'a') as f:
            f.write(user_input + "\n")
        tasks.insert(END, user_input + "\n")
        entry.delete(0, END)

def delete_all():
    with open("list.dat", 'w'):
        pass
    tasks.delete(0, END)

def delete_task():
    selected_task = tasks.curselection()
    if selected_task:
        tasks.delete(selected_task)
        with open("list.dat", 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for task in content:
                if task.strip() != tasks.get(selected_task).strip():
                    f.write(task)
            f.truncate()

def dark_mode():
    w.configure(bg="black")
    tasks.configure(bg="black")
    header_label.configure(bg="black")
    entry.configure(bg="black")
    entry.configure(fg="white")
    button_frame.configure(bg="black")
    add_button.configure(bg="black")
    delete_btn.configure(bg="black")
    delete_all_button.configure(bg="black")

def light_mode():
    w.configure(bg="white")
    tasks.configure(bg="white")
    header_label.configure(bg="white")
    entry.configure(bg="white")
    entry.configure(fg="black")
    button_frame.configure(bg="white")
    add_button.configure(bg="white")
    delete_btn.configure(bg="white")
    delete_all_button.configure(bg="white")

w = Tk()
w.title("Your To-Do List")

# Get screen width and height
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()

# Header
header_label = Label(w, text="TO-DO LIST", font=("Courier New", 24), fg="green", bg="white")
header_label.pack(pady=20)

# Listbox for tasks
tasks = Listbox(w, width=50, height=10, bg="white", font=("Courier New", 16), fg="green")
tasks.pack(pady=20)

# Entry for new task
entry = Entry(w, width=50, font=("Courier New", 14), bg="white", fg="black")
entry.pack(pady=10)

# Button Frame
button_frame = Frame(w)
button_frame.pack(pady=10)

# Add Button
add_button = Button(button_frame, text="Add Task", command=lambda: get_input(), font=("Courier New", 14), bg="white", fg="green")
add_button.pack(side=LEFT, padx=10)

# Delete Task Button
delete_btn = Button(button_frame, text="Done Task", command=lambda: delete_task(), font=("Courier New", 14), bg="white", fg="green")
delete_btn.pack(side=LEFT, padx=10)

# Delete All Button
delete_all_button = Button(button_frame, text="Delete all tasks", command=lambda: delete_all(), font=("Courier New", 14), bg="white", fg="green")
delete_all_button.pack(side=LEFT, padx=10)

# Light Mode Button
lgt = Button(w, text="LIGHT MODE", command=lambda: light_mode(), font=("Courier New", 10), fg="green", bg="black")
lgt.place(x=screen_width - 120, y=10)

# Dark Mode Button
drk = Button(w, text="DARK MODE", command=lambda: dark_mode(), font=("Courier New", 10), fg="green", bg="black")
drk.place(x=screen_width - 220, y=10)

# Set the window size to full screen
w.geometry(f"{screen_width}x{screen_height}")

w.mainloop()
