from tkinter import *
from tkinter import ttk
import random, string 
import pyperclip
from docx import Document
import os
document = Document()
#Sets up window
app = Tk() 
app.geometry("400x400")
app.resizable(0,0)
app.title("Jack Sweeney - Strong password generator. ")

#Sets up the title text at the top, and the subtitle text at the bottom
Label(app, text = "PASSWORD GENERATOR", font ="arial 15 bold").pack()
Label(app, text ="By Jack Sweeney", font = "arial 15 bold").pack(side = BOTTOM)

#Sets up the label for the password length spinbox, which allows the user to select a number from 8 to 64
pass_label = Label(app, text = 'Password Length (8-64) ', font = "arial 10 bold").pack()
pass_len = IntVar()
length = Spinbox(app, from_ = 8, to_ = 64, textvariable = pass_len, width = 15).pack()

pass_str = StringVar()
def Generate():
    """Generates a password using the user specified length"""
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

#Buttons to generate the password and generate the text input field
Button(app, text = "Generate your Password", command = Generate ).pack(pady=5)

Entry(app , textvariable = pass_str).pack()

def Copy_password():
    """Function to copy the password to your clipboard"""
    pyperclip.copy(pass_str.get())
Button(app, text = "Copy your password to clipboard", command = Copy_password).pack(pady=5)

def Save_password():
    """Function to save the password to a word document"""
    documentName = input("What would you like your document to be called?")
    if os.path.isfile('./' + documentName + '.docx') == True:
        print("Filename already in use! Please try again")
        Save_password()
    else:
        document.add_paragraph(pass_str.get())
        document.save(documentName + '.docx')
Button(app, text = "Save your password in a document", command = Save_password).pack(pady=5)
 
app.mainloop()
