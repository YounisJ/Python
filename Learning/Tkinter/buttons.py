from tkinter import *

# Main Window
root = Tk()

def SayHello():
    myLable = Label(root, text="Hey How are You!")
    myLable.pack()

mybutton = Button(root, text="Say Hello", command=SayHello, fg="blue")
#We have some parameters for button
#1. State = ENABLED/DISABLED
#2. padx = 50
#3. pady = 50




mybutton.pack()


# Main Window ends here
root.mainloop()