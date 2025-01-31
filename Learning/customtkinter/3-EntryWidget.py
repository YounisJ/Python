from customtkinter import *

rootwindow = CTk()
rootwindow.title("Entry Widgets")
rootwindow.geometry('600x400')

def submit():
    lblhello = CTkLabel(
        rootwindow,
        font=("Helvetica", 20),
        text="Hello Mr. " + txtInput.get()
    )
    lblhello.pack(pady=10)

btnsubmit = CTkButton(
    rootwindow,
    text="Submit",
    command=submit
)
btnsubmit.pack(pady=40)

txtInput = CTkEntry(
    rootwindow,
    placeholder_text="Please Enter Your name"
)
txtInput.pack(pady=20)

rootwindow.mainloop()