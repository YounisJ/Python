from customtkinter import *

app = CTk()
app.title("Calculater")
app.geometry('300x500')

###############
def sendnum(number):
    txtinput.insert(END, number)

txtinput = CTkEntry(
    app,
    placeholder_text="Calculater",
    height=50,
    width=250,
    font=("", 20),
    corner_radius=10
    )

txtinput.grid(row=0,column=0, columnspan=5, padx=25, pady = 25)

btn_1 = CTkButton(app, text="1", height=50, width=50, corner_radius=60, command=lambda: sendnum(1))
btn_2 = CTkButton(app, text="2", height=50, width=50, corner_radius=60, command=lambda: sendnum(2))
btn_3 = CTkButton(app, text="3", height=50, width=50, corner_radius=60, command=lambda: sendnum(3))

btn_4 = CTkButton(app, text="4", height=50, width=50, corner_radius=60, command=lambda: sendnum(4))
btn_5 = CTkButton(app, text="5", height=50, width=50, corner_radius=60, command=lambda: sendnum(5))
btn_6 = CTkButton(app, text="6", height=50, width=50, corner_radius=60, command=lambda: sendnum(6))

btn_7 = CTkButton(app, text="7", height=50, width=50, corner_radius=60, command=lambda: sendnum(7))
btn_8 = CTkButton(app, text="8", height=50, width=50, corner_radius=60, command=lambda: sendnum(8))
btn_9 = CTkButton(app, text="9", height=50, width=50, corner_radius=60, command=lambda: sendnum(9))

btn_0 = CTkButton(app, text="0", height=50, width=50, corner_radius=60, command=lambda: sendnum(0))


btn_9.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_7.grid(row=1,column=2)

btn_6.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_4.grid(row=2,column=2)

btn_3.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_1.grid(row=3,column=2)

btn_9.grid(row=4,column=0)

app .mainloop()