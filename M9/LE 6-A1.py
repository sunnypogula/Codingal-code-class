from tkinter import *
from tkinter import messsagebox
from PIL import image , ImageTk

#setting up main window
root =Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

#adding image and labels in the main window
upload = Image.open("")
#resize the image using resize ()method
upload = upload.resize((300,300))
image =ImageTk.photoImage(upload)
label = Label(root,i,age-image, bg='light blue')
label.place(x=180,y=20)

label1 = Label(root,
               text="Hey user! Welcome to Denomaination Counter Application .",
               bg = 'light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

#funtion to display a messagebox and priceed if OK is clicked
def msg():
    msgBox = messagebox.showinfo(
        "Alert", "Do ypu want to calculate the denomination count?")
    if msgBox=='ok':
        topwin()
#adding buttons to the main window
button1= Button(root,
                text="Let's get staerted!",
                command=msg,
                bg='brown',
                fg='white')
button1.place(x=260, y=360)

#funtion for openuing new/top window
def topwin():
    top = Toplevel()
    top.title("Denomination Calculatoer")
    top.configure(bg='light grey')
    top.geometry("600x350x50x50")

    label = Label(top, text ="Enter toatl amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="200", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount 
            amount - int(entry.grt())
            note2000 = amount // 2000
            amount %=2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError: 
            messagebox.showerror("Error","Placse entry a vaild number.")
    btn = Button(top, text='Calculate', command=calculator,bg='brown', fg='white') 