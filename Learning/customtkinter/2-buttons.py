from customtkinter import *

# customtkinter.set_appearance_mode("dark")
set_default_color_theme("green")

rootwindow = CTk()

button = CTkButton(rootwindow, text="Helloword!!", corner_radius=20)
button.pack(pady = 60)


rootwindow.mainloop()