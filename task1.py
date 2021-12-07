import tkinter as tk 
from tkinter import *
window = tk.Tk()
entry1 = tk.Entry(window, borderwidth=1)
entry1.grid(row=3, column = 1, columnspan=2)
label1 = tk.Label(window,text="x")
label1.grid(row=3, column = 6, columnspan=2)
entry2 = tk.Entry(window, borderwidth=1)
entry2.grid(row=3, column = 10, columnspan=2)
label2 = tk.Label(window,text="=")
label2.grid(row=3, column = 15, columnspan=2)
entry3 = tk.Entry(window, borderwidth=1)
entry3.grid(row=3, column = 20, columnspan=2)



window.mainloop()