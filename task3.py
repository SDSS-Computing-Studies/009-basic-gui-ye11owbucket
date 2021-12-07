#!python3
import tkinter as tk 
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk

"""
The 3rd method of placing widgets is to treat the window as a map with x and y
coordinates, and then place the widget based on the location from the top left
corner of the window.  Distances are measured in pixels

"""
window = tk.Tk()
window.title("dubious little creature")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window,text="Pochacco!")
label3 = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", borderwidth=1, bg="#A3FFFF")
label1.grid(column=0, row=0) 
label2.grid(column=1, row=0) 
label3.grid(column=0, row=1, columnspan=2)

window.mainloop()