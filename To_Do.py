import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

root = customtkinter.CTk()
root.title("To-Do List")
root.geometry("539x560")
root.resizable(False, False)
root.configure(background="black")


def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(0, task)
        task_entry.delete(0, END)

    else:
        messagebox.showerror("ERROR", 'Enter a task.')


def delete_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected[0])

    else:
        messagebox.showerror('ERROR', 'Choose a task to delete.')


def edit_task():
    selected = task_list.curselection()
    if selected:
        edited_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=task_list.get(selected))
        if edited_task:
            task_list.delete(selected)
            task_list.insert(selected, edited_task)

    else:
        messagebox.showerror('ERROR', 'Choose a task to edit.')

# TITLE
Title = customtkinter.CTkLabel(root, text="To-Do List", font=('arial', 25, "bold"))
Title.place(x=200, y=20)

# ENTRY
task_entry = customtkinter.CTkEntry(root, height=50, width=400, text_color="black", fg_color="white",
                                    font=('arial', 23))
task_entry.place(x=70, y=350)

# LISTBOX
task_list = Listbox(root, width=60, height=15, font=('arial', 12))
task_list.place(x=65, y=80)

# ADD
add_button = customtkinter.CTkButton(root, height=50, width=200, command=add_task, text='ADD TASK', fg_color="green",
                                     font=('arial', 24))
add_button.place(x=40, y=420)

# DELETE
delete_button = customtkinter.CTkButton(root, height=50, width=200, command=delete_task, text='DELETE TASK',
                                        fg_color="red", font=('arial', 24))
delete_button.place(x=300, y=420)

#EDIT
edit_button = customtkinter.CTkButton(root, height=20, width=80, command=edit_task, text='EDIT TASK',
                                      fg_color="orange", font=('arial', 24))
edit_button.place(x=40, y=490)

root.mainloop()
