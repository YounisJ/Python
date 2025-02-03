from customtkinter import *

app = CTk()
app.title("Calculator")
app.geometry('300x560')

# Global variables for operations
num1 = None
operator = None

def sendnum(number):
    """ Inserts numbers into the input field """
    txtinput.insert(END, number)

def getnum1(op):
    """ Stores first number and operation, then clears input field """
    global num1, operator
    num1 = int(txtinput.get())  # Store first number
    operator = op  # Store the selected operator
    txtinput.delete(0, END)  # Clear input for next number

def evaluate():
    """ Performs the calculation and displays result """
    global num1, operator
    num2 = int(txtinput.get())  # Get second number
    txtinput.delete(0, END)  # Clear input field

    if operator == "+":
        result = num1 + num2
        txtinput.insert(END, result)  # Display result

def clear():
    """ Clears the input field and resets stored values """
    global num1, operator
    txtinput.delete(0, END)
    num1 = None
    operator = None

# Input field
txtinput = CTkEntry(app, placeholder_text="Calculator", height=50, width=250, font=("helvetica", 20), corner_radius=10)
txtinput.grid(row=0, column=0, columnspan=5, padx=25, pady=25)

# Number buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 0)
]

for (text, row, col) in buttons:
    btn = CTkButton(app, text=text, height=60, width=60, corner_radius=60, command=lambda t=text: sendnum(t))
    btn.grid(row=row, column=col, padx=17, pady=17)

# Operator buttons
btn_add = CTkButton(app, text="+", height=60, width=60, corner_radius=60, command=lambda: getnum1("+"))
btn_equal = CTkButton(app, text="=", height=60, width=60, corner_radius=60, command=evaluate)
btn_clear = CTkButton(app, text="C", height=60, width=60, corner_radius=60, command=clear)

btn_add.grid(row=5, column=0, padx=5, pady=17)
btn_equal.grid(row=5, column=1, padx=5, pady=17)
btn_clear.grid(row=4, column=1, padx=5, pady=17)

app.mainloop()
