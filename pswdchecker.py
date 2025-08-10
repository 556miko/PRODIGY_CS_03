import re
import tkinter as tk
from tkinter import messagebox

def check_password():
    pswd = entry.get()
    pswd_len = len(pswd)
    error_found = False

    if pswd_len < 7:
        messagebox.showerror("Error", "Invalid: Password must be at least 7 characters long")
        error_found = True
    if pswd_len > 20:
        messagebox.showerror("Error", "Invalid: Password must be at most 20 characters long")
        error_found = True
    if re.search("[A-Z]", pswd) is None:
        messagebox.showerror("Error", "Invalid: Password must contain at least one capital letter")
        error_found = True
    if re.search("[a-z]", pswd) is None:
        messagebox.showerror("Error", "Invalid: Password must contain at least one small letter")
        error_found = True
    if re.search(r"[!@#$%^&*(){}\[\]]", pswd) is None:
        messagebox.showerror("Error", "Invalid: Password must contain at least one special character")
        error_found = True
    if re.search("[0-9]", pswd) is None:
        messagebox.showerror("Error", "Invalid: Password must contain at least one number")
        error_found = True
    if re.search(" ", pswd):
        messagebox.showerror("Error", "Invalid: Password must not contain whitespace")
        error_found = True

    if not error_found:
        messagebox.showinfo("Success", "Your Password is Strong!")
        
window = tk.Tk()
window.title("Password Complexity Checker")
window.geometry("500x300")

label = tk.Label(window, text="Enter your password", pady=10)
label.pack()

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

btn = tk.Button(window, text="Check Password", command=check_password)
btn.pack(pady=20)

window.mainloop()
