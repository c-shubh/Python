'''A Simple password manager which stores details.'''
import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()
while True:
    file_path = filedialog.askopenfilename(title="Select a text file")
    if file_path == '':
        exit()
    elif os.path.splitext(file_path)[1] != ".txt":
        print("Invalid file format. Only text files supported.")
    else:
        break


# for input
def usrname():
    return input("{:10s} ".format('Username:'))


def email():
    return input("{:10s} ".format('Email:'))


def psw():
    return input("{:10s} ".format('Password:'))


def phno():
    return input("{:10s} ".format('Phone no:'))


# printing stuff
# file_path = input("{:10s} ".format('File path:'))
print()
service = input("{:10s} ".format('Service:'))
print()
print("Select one or multiple of the following: ")
print("1. Username")
print("2. Email")
print("3. Password")
print("4. Phone no")

selection = input().split()

with open(file_path, 'a') as file:
    file.write("{:10s} {:10s}\n".format('Service:', service))
    if '1' in selection:
        file.write("{:10s} {:10s}\n".format('Username:', usrname()))
    if '2' in selection:
        file.write("{:10s} {:10s}\n".format('Email:', email()))
    if '3' in selection:
        file.write("{:10s} {:10s}\n".format('Password:', psw()))
    if '4' in selection:
        file.write("{:10s} {:10s}\n\n".format('Phone no:', phno()))

print('\nDetails saved successfully.')
