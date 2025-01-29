from tkinter import *

rootwindow = Tk()
rootwindow.title("Calculater")

txtinput = Entry(rootwindow, width=35, borderwidth=5)
txtinput.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

def button_add():
    return

btn1 = Button(rootwindow, text="1",padx=40,pady=20,command=button_add)
btn2 = Button(rootwindow, text="2",padx=40,pady=20,command=button_add)
btn3 = Button(rootwindow, text="3",padx=40,pady=20,command=button_add)

btn4 = Button(rootwindow, text="4",padx=40,pady=20,command=button_add)
btn5 = Button(rootwindow, text="5",padx=40,pady=20,command=button_add)
btn6 = Button(rootwindow, text="6",padx=40,pady=20,command=button_add)

btn7 = Button(rootwindow, text="7",padx=40,pady=20,command=button_add)
btn8 = Button(rootwindow, text="8",padx=40,pady=20,command=button_add)
btn9 = Button(rootwindow, text="9",padx=40,pady=20,command=button_add)

btn0 = Button(rootwindow, text="0",padx=40,pady=20,command=button_add)

btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)

btn4.grid(row=2, column=1)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)

btn7.grid(row=3, column=1)
btn8.grid(row=3, column=2)
btn9.grid(row=3, column=3)

btn0.grid(row=4, column=1)




rootwindow.mainloop()
