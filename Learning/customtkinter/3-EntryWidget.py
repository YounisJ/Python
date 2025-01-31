from customtkinter import *

rootwindow = CTk()
rootwindow.title("Entry Widgets")
rootwindow.geometry('500x300')

def submit():
    if txtInput.get() == "":
        print("No text in the text field")
    else:
        lblhello = CTkLabel(
        rootwindow,
        font=("Helvetica", 20),
        text="Hello Mr. " + txtInput.get()
        )
        lblhello.pack(pady=10)
        txtInput.delete(0,END)



btnsubmit = CTkButton(
    rootwindow,
    text="Submit",
    command=submit,
    height=40,
    width=80
)
btnsubmit.pack(pady=40)

txtInput = CTkEntry(
    rootwindow,
    placeholder_text="Please Enter Your name",
    width=200,
    height=40,
    font=("",13),
    corner_radius=40,
    text_color="green"
)
txtInput.pack(pady=20)

rootwindow.mainloop()