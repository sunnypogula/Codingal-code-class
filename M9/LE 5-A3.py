#Import necessary libraries
from tkinter import *

#setting up main window
root = Tk()
root.geometry("400x300")
root.title("main")

#Function to open new (top level) window
def topwin():
    #setting up top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    #Adding a label widget to top window
    l2 = Label(top,text = "this is toplevel window")
    l2.pack()
    top.mainloop()
    #
#Adding a label and button widget to root (main)window 
l = Label (root,twex="Click here to open another window",command = topwin)

#Arraning widgets
l.pack()
btn.pack()