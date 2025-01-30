from tkinter import *

rootwindow = Tk()
rootwindow.title("Calculater")

txtinput = Entry(rootwindow, width=35, borderwidth=5)
txtinput.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

def btnClicked(number):
    # prevnum = txtinput.get()
    # txtinput.delete(0, END)
    txtinput.insert(0, number)
    # if number>9:
    #     txtinput.delete(0, END)
    #     txtinput.insert(0, prevnum+number)
        
        


btn1 = Button(rootwindow, text="1",padx=40,pady=20,command=lambda: btnClicked(1))
btn2 = Button(rootwindow, text="2",padx=40,pady=20,command=lambda: btnClicked(2))
btn3 = Button(rootwindow, text="3",padx=40,pady=20,command=lambda: btnClicked(3))

btn4 = Button(rootwindow, text="4",padx=40,pady=20,command=lambda: btnClicked(4))
btn5 = Button(rootwindow, text="5",padx=40,pady=20,command=lambda: btnClicked(5))
btn6 = Button(rootwindow, text="6",padx=40,pady=20,command=lambda: btnClicked(6))

btn7 = Button(rootwindow, text="7",padx=40,pady=20,command=lambda: btnClicked(7))
btn8 = Button(rootwindow, text="8",padx=40,pady=20,command=lambda: btnClicked(8))
btn9 = Button(rootwindow, text="9",padx=40,pady=20,command=lambda: btnClicked(9))

btn0 = Button(rootwindow, text="0",padx=40,pady=20,command=lambda: btnClicked(0))
btnclear = Button(rootwindow, text="clear",padx=78,pady=20,command=lambda: btnClicked())
btnadd = Button(rootwindow, text="+",padx=39,pady=20,command=lambda: btnClicked())
btnequal = Button(rootwindow, text="=",padx = 86,pady=20,command=lambda: btnClicked())

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column=0)
btnclear.grid(row=4, column=1, columnspan=3)
btnadd.grid(row=5, column=0)
btnequal.grid(row=5, column=1, columnspan=3)




rootwindow.mainloop()
