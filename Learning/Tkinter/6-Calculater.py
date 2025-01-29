from tkinter import *

rootwindow = Tk()
rootwindow.title("Calculater")

txtinput = Entry(rootwindow, width=35, borderwidth=5)
txtinput.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

def button_add():
    return

btn1 = Button(rootwindow, text="1",command=button_add)
btn2 = Button(rootwindow, text="2",command=button_add)
btn3 = Button(rootwindow, text="3",command=button_add)

btn4 = Button(rootwindow, text="4",command=button_add)
btn5 = Button(rootwindow, text="5",command=button_add)
btn6 = Button(rootwindow, text="6",command=button_add)

btn7 = Button(rootwindow, text="7",command=button_add)
btn8 = Button(rootwindow, text="8",command=button_add)
btn9 = Button(rootwindow, text="9",command=button_add)

btn0 = Button(rootwindow, text="0",command=button_add)






rootwindow.mainloop()
