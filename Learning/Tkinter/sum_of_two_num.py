from tkinter import *

rootwindow = Tk()

txtnum1 = Entry(rootwindow)
txtnum1.pack()
txtnum2 = Entry(rootwindow)
txtnum2.pack()

def sum_of_two_num():
    num1 = txtnum1.get()
    num2 = txtnum2.get()

    sum = int(num1)+int(num2)

    lblshownum = Label(rootwindow, text=sum)
    lblshownum.pack()

Button = Button(rootwindow, text="Sum", command=sum_of_two_num).pack()

rootwindow.mainloop()
