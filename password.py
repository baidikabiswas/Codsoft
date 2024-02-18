from tkinter import *
import random

root = Tk()
root.title("Password Generator")
root.geometry("539x560")
root.resizable(False, False)
root.configure(background="#FAF9F6")

# TITLE
Title = Label(root, text="Password Generator", fg="blue", bg="#FAF9F6", font=('arial', 18, "bold", 'underline'))
Title.pack(anchor="center", pady=20)

# USERNAME
username = Label(root, text="Enter Username:", fg="black", bg="#FAF9F6", font=('arial', 12))
username.place(x=30, y=100)

username_entry = Entry(root, font=('arial', 12))
username_entry.place(y=100, x=210)
username_entry.pack

# PASSWORD
length_password = Label(root, text="Enter Password Length:", fg="black", bg="#FAF9F6", font=('arial', 12))
length_password.place(x=30, y=150)

generated_password = Label(root, text="Generated Password:", fg="black", bg="#FAF9F6", font=('arial', 12))
generated_password.place(x=30, y=200)

character_entry = Entry(root, font=('arial', 12))
character_entry.pack(pady=77, padx=210)

label_password = Label(root, width=20, font=('Arial', 15))
label_password.place(x=210, y=200)

alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*+-_'
characters = alphabets + numbers + symbols


def generate_password():
    length = character_entry.get()
    password = "".join(random.sample(characters, int(length)))
    label_password.config(text='' + password)


Button(root, text="Generate Password", command=generate_password, width=16, height=1, font=("arial", 14, "bold")).place(
    x=165, y=290)

root.mainloop()
