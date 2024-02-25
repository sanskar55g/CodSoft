import tkinter as tk
from tkinter import StringVar, IntVar
import random
import string
import pyperclip

def generate_password():
    length = int(length_var.get())
    use_special_chars = special_chars_var.get()
    use_numbers = numbers_var.get()
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()

    characters = ""
    if use_special_chars:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        password_var.set("Please select at least one option.")
        return

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(generated_password)

def copy_to_clipboard():
    password = password_var.get()
    pyperclip.copy(password)
    copied_label.config(text="Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator by CodSoft")

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
length_var = StringVar()
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10, pady=5)

special_chars_var = IntVar()
special_chars_checkbox = tk.Checkbutton(root, text="Special Characters", variable=special_chars_var)
special_chars_checkbox.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)

numbers_var = IntVar()
numbers_checkbox = tk.Checkbutton(root, text="Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

uppercase_var = IntVar()
uppercase_checkbox = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

lowercase_var = IntVar()
lowercase_checkbox = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, pady=10)

password_var = StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12, "bold"))
password_label.grid(row=7, column=0, columnspan=2, pady=5)

copied_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
copied_label.grid(row=8, column=0, columnspan=2, pady=5)

root.mainloop()
