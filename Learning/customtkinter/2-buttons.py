from customtkinter import *

# customtkinter.set_appearance_mode("dark")
set_default_color_theme("green")

rootwindow = CTk()
rootwindow.geometry('600x400')
# define helloworld fuunction
def  hello():
    lblhello = CTkLabel(rootwindow, text="Hello World!!!")
    lblhello.pack()

#create button
btnhello = CTkButton(rootwindow, text="Say Hello", command=hello)
btnhello.pack(pady= 20)

rootwindow.mainloop()