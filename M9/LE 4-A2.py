import tkinter as tk
window = tk.Tk()
window.configure(bg="red")
for i in range(3): #0,1,2
    for j in range(3):
        frame = tk.Frame(master=window,relief=tk.RAISED, borderwidth=5)
        frame.grid(row=i, column=j,padx=3,pady=3)
        label = tk.Label(master=frame,text=f"Row {i}\ncolumn{j}")
        label.pack()
window.mainloop()