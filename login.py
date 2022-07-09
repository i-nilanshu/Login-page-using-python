from cgitb import text
from email.mime import image
from logging import root
from tkinter import *
from venv import create
root = Tk()
root.geometry("500x500")
root.configure(bg="#424949")
root.title("Login page")
root.iconbitmap("login1.ico")
picture = PhotoImage(file="admin01.png")
lab = Label(root, image=picture)

username = Label(root, text="Username", font="none 15", bg="#424949", fg="white")
password = Label(root, text="Password", font="none 15", bg="#424949", fg="white")

username_box = Entry(root, font="none 15", w=20)
password_box = Entry(root, font="none 15", w=20, show="*")

login = Button(root, text="Login", padx=30, pady=10)

lab.grid(row=0, column=0, columnspan=2, padx=95, pady=40)

username.grid(row=1, column=0, pady=10)
password.grid(row=2, column=0, pady=10)

username_box.grid(row=1, column=1, pady=10)
password_box.grid(row=2, column=1, pady=10)

login.grid(row=3, columnspan=2, column=0, pady=10)

root.mainloop()