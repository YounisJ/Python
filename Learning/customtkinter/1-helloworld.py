import customtkinter

#Theme setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# creating root window
rootwindow = customtkinter.CTk()
rootwindow.title("HelloWorld")
rootwindow.geometry('600x400')

# define helloworld fuunction
def  hello():
    lblhello = customtkinter.CTkLabel(rootwindow, text="Hello World!!!")
    lblhello.pack()

#create button
btnhello = customtkinter.CTkButton(rootwindow, text="Say Hello", command=hello)
btnhello.pack(pady= 20)

#main window check regularly
rootwindow.mainloop()