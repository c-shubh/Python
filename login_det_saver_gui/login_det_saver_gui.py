from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

file_path = ""


def save_to_file():
    with open(file_path, "a") as file:
        file.write("{:10s} {:10s}\n".format("Service:", service.get()))
        if username.get() != "":
            file.write("{:10s} {:10s}\n".format("Username:", username.get()))
        if email.get() != "":
            file.write("{:10s} {:10s}\n".format("Email:", email.get()))
        if password.get() != "":
            file.write("{:10s} {:10s}\n".format("Password:", password.get()))
        if phoneno.get() != "":
            file.write("{:10s} {:10s}\n\n".format("Phone no:", phoneno.get()))
        file.write("\n\n")


def clear_fields():
    service_entry.delete(0, "end")
    username_entry.delete(0, "end")
    email_entry.delete(0, "end")
    password_entry.delete(0, "end")
    phoneno_entry.delete(0, "end")


def select_file():
    global file_path
    while True:
        file_path = filedialog.askopenfilename(
            title="Select a text file",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
        )
        if file_path == "":
            exit()
        elif os.path.splitext(file_path)[1] != ".txt":
            print("Invalid file format. Only text files supported.")
        else:
            break
    filename_label["text"] = os.path.split(file_path)[1]


def pass_toggle():
    if pass_toggle_button.image == eye_open:
        pass_toggle_button["image"] = eye_close
        pass_toggle_button.image = eye_close

        password_entry["show"] = ""
    else:
        pass_toggle_button["image"] = eye_open
        pass_toggle_button.image = eye_open

        password_entry["show"] = "●"


root = Tk()
root.title("Login details saver")

mainframe = ttk.Frame(root)
mainframe.pack(expand=True)

select = ttk.Button(mainframe, text="Select a text file", command=select_file)
select.grid(row=0, column=0)
filename_label = ttk.Label(mainframe)
filename_label.grid(row=0, column=1, sticky=W, padx=5, pady=5)

service = StringVar()
username = StringVar()
email = StringVar()
password = StringVar()
phoneno = StringVar()

ttk.Label(mainframe, text="Service").grid(row=1, column=0, sticky=E, padx=5, pady=5)
service_entry = ttk.Entry(mainframe, textvariable=service)
service_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

ttk.Label(mainframe, text="Username").grid(row=2, column=0, sticky=E, padx=5, pady=5)
username_entry = ttk.Entry(mainframe, textvariable=username)
username_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

ttk.Label(mainframe, text="Email").grid(row=3, column=0, sticky=E, padx=5, pady=5)
email_entry = ttk.Entry(mainframe, textvariable=email)
email_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

ttk.Label(mainframe, text="Password").grid(row=4, column=0, sticky=E, padx=5, pady=5)
password_entry = ttk.Entry(mainframe, show="●", textvariable=password)
password_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

eye_open = PhotoImage(file="./trans-eye-outline.png", format="PNG")
eye_close = PhotoImage(file="./trans-eye-off-outline.png", format="PNG")
pass_toggle_button = ttk.Button(mainframe, image=eye_open, command=pass_toggle)
pass_toggle_button.grid(row=4, column=2, sticky=W)
pass_toggle_button.image = eye_open

ttk.Label(mainframe, text="Phone no").grid(row=5, column=0, sticky=E, padx=5, pady=5)
phoneno_entry = ttk.Entry(mainframe, textvariable=phoneno)
phoneno_entry.grid(row=5, column=1, sticky=W, padx=5, pady=5)

clear = ttk.Button(mainframe, text="Clear fields", command=clear_fields).grid(
    row=6, column=0, sticky=W
)

save = ttk.Button(mainframe, text="Save to file", command=save_to_file).grid(
    row=6, column=1, columnspan=2, sticky=E
)

service_entry.focus()


root.mainloop()
