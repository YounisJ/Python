from customtkinter import *

rootwindow = CTk()
rootwindow.title("Entry Widgets")
rootwindow.geometry('500x300')

def submit():
    if txtInput.get() == "":
        else:


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