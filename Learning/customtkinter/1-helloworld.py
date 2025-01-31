from customtkinter import *

#Theme setting
set_appearance_mode("dark")
set_default_color_theme("green")

# creating root window
rootwindow = CTk()
rootwindow.title("HelloWorld")
rootwindow.geometry('600x400')

lblHello= CTkLabel(rootwindow, text="Hello World!!")
lblHello.pack(pady = 60)

#main window check regularly
rootwindow.mainloop()