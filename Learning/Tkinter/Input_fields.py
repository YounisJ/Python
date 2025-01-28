from tkinter import *

#Starts Here
root = Tk()

input =  Entry(root)
input.pack()
#Some Parameters
#bg = blue
#fg = "white"
#width = 50
#height = 50
#borderwidth = 5
#insert() = put some default text into textfield
 
def getname():
    #get() = used toget data from input field
    hello = "Hello " + input.get()
    lblname = Label(root, text=hello)
    lblname.pack()

Newbutton = Button(root, text="Get name", command=getname)
Newbutton.pack()



#Ends here
root.mainloop()
