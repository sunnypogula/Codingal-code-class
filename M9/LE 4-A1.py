#1.mport thinker module
#2.create the GUI applocation main qindow
#3.add widgtes
from tkinter import*
window = Tk()
window.title('Thinter sample window')
window.geometry('300x300')

#label 
greeting = Label(text="hello user",fg='black',bg='white')
#button 
button = Button(text="click me",bg='black',fg='white')
#entry
entry = Entry(fg="yellow",bg="blue",width=200)

greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()
label = Label(master=frame, text='Sample Frame')
label.pack()

textbox = Text(fg='green', bg='white')
textbox.pack()
window.mainloop()