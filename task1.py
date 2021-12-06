import tkinter as tk 
from tkinter import *
window = tk.Tk()
entry1 = tk.Entry(window, borderwidth=3, relief=SUNKEN)
entry1.grid(row=3, column = 1, columnspan=2)
label1 = tk.Label(window,text="x")
label1.grid(row=3, column = 6, columnspan=2)
entry2 = tk.Entry(window, borderwidth=3, relief=SUNKEN)
entry2.grid(row=3, column = 10, columnspan=2)
label2 = tk.Label(window,text="=")
label2.grid(row=3, column = 15, columnspan=2)
a = entry1
b = entry2
akaya = (a * b)
label3 = tk.Label(window,text=akaya)



window.mainloop()