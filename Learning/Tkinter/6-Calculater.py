from tkinter import *

rootwindow = Tk()
rootwindow.title("Calculater")

txtinput = Entry(rootwindow, width=30)
txtinput.grid(row=0,column=0)

btn1 = Button(rootwindow, text="1",height=2,width=6)
btn1.grid(row= 1,column=0)
btn2 = Button(rootwindow, text="2")
btn2.grid(row= 1,column=1)
btn3 = Button(rootwindow, text="3")
btn3.grid(row= 1,column=2)




rootwindow.mainloop()
