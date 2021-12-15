#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.geometry("258x134")
window.title("dubious little creature")
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window,text="Pochacco!")
label3 = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", borderwidth=1, bg="#A3FFFF")
label1.place(x=50, y=0)
label2.place(x=125, y=40)
label3.place(x=0, y=100)

window.mainloop()



