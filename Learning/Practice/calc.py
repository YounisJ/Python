from customtkinter import *

app = CTk()
app.title("Calculater")
app.geometry('300x560')

###############
def sendnum(number):
    txtinput.insert(END, number)

txtinput = CTkEntry(
    app,
    placeholder_text="Calculater",
    height=50,
    width=250,
    font=("helvetica", 20),
    corner_radius=10
    )

txtinput.grid(row=0,column=0, columnspan=5, padx=25, pady = 25)

btn_1 = CTkButton(app, text="1", height=60, width=60, corner_radius=60, command=lambda: sendnum(1))
btn_2 = CTkButton(app, text="2", height=60, width=60, corner_radius=60, command=lambda: sendnum(2))
btn_3 = CTkButton(app, text="3", height=60, width=60, corner_radius=60, command=lambda: sendnum(3))

btn_4 = CTkButton(app, text="4", height=60, width=60, corner_radius=60, command=lambda: sendnum(4))
btn_5 = CTkButton(app, text="5", height=60, width=60, corner_radius=60, command=lambda: sendnum(5))
btn_6 = CTkButton(app, text="6", height=60, width=60, corner_radius=60, command=lambda: sendnum(6))

btn_7 = CTkButton(app, text="7", height=60, width=60, corner_radius=60, command=lambda: sendnum(7))
btn_8 = CTkButton(app, text="8", height=60, width=60, corner_radius=60, command=lambda: sendnum(8))
btn_9 = CTkButton(app, text="9", height=60, width=60, corner_radius=60, command=lambda: sendnum(9))

btn_0 = CTkButton(app, text="0", height=60, width=60, corner_radius=60, command=lambda: sendnum(0))
btn_clear = CTkButton(app, text="clear", height=60, width=130, corner_radius=60)

btn_add = CTkButton(app, text="+", height=60, width=60, corner_radius=60)
btn_equal = CTkButton(app, text="=", height=60, width=60, corner_radius=60)


btn_9.grid(row=1,column=2, padx= 17, pady = 17)
btn_8.grid(row=1,column=1, padx= 17, pady = 17)
btn_7.grid(row=1,column=0, padx= 17, pady = 17)

btn_6.grid(row=2,column=2, padx= 17, pady = 17)
btn_5.grid(row=2,column=1, padx= 17, pady = 17)
btn_4.grid(row=2,column=0, padx= 17, pady = 17)

btn_3.grid(row=3,column=2, padx= 17, pady = 17)
btn_2.grid(row=3,column=1, padx= 17, pady = 17)
btn_1.grid(row=3,column=0, padx= 17, pady = 17)

btn_0.grid(row=4,column=0, padx= 17, pady = 17)
btn_clear.grid(row=4,column=1, padx= 5, pady = 17)

btn_add.grid(row=5,column=0, padx= 5, pady = 17)
btn_equal.grid(row=5,column=1, padx= 5, pady = 17)

app .mainloop()