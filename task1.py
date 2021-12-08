import tkinter as tk 
from tkinter import *
window = tk.Tk()

entry1 = tk.Entry(window, borderwidth=1, width = 15)
entry1.grid(row=0, column = 0)

label1 = tk.Label(window,text="x")
label1.grid(row=0, column = 1)

entry2 = tk.Entry(window, borderwidth=1, width = 15)
entry2.grid(row=0, column = 2)

label2 = tk.Label(window,text="=")
label2.grid(row=0, column = 3)

entry3 = tk.Entry(window, borderwidth=1, width = 23)
entry3.grid(row=0, column = 4)

window.mainloop()