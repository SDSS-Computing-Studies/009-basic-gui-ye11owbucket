import tkinter as tk 
from tkinter import *

### PreReq

window = tk.Tk()
window.title("T-Town Veterinary Database ")
dogphoto = PhotoImage(file="dog.png")

# Labels

label1 = tk.Label(window,text="Client Database")
label2 = tk.Label(window, image=dogphoto, borderwidth=1)
label5 = tk.Label(window,text="Name")
label6 = tk.Label(window,text="Type")
label7 = tk.Label(window,text="Breed")
label8 = tk.Label(window,text="Owner")
label9 = tk.Label(window,text="Birthdate")

# Label Grid

label1.grid(row = 1, column = 2)
label2.grid(row = 1, column = 0)
label5.grid(row = 2, column = 0)
label6.grid(row = 2, column = 1)
label7.grid(row = 2, column = 2)
label8.grid(row = 2, column = 3)
label9.grid(row = 2, column = 4)

# Entries

entry1 = tk.Entry(window, borderwidth=1)
entry2 = tk.Entry(window, borderwidth=1)
entry3 = tk.Entry(window, borderwidth=1)
entry4 = tk.Entry(window, borderwidth=1)
entry5 = tk.Entry(window, borderwidth=1)
entry6 = tk.Entry(window, borderwidth=1)

# Entry Grid

entry1.grid(row=3, column = 0)
entry2.grid(row=3, column = 1)
entry3.grid(row=3, column = 2)
entry4.grid(row=3, column = 3)
entry5.grid(row=3, column = 4)
entry6.grid(row=0, column = 4)

# Buttons

button1 = tk.Button(window,text="Clash Royale")
button2 = tk.Button(window,text="<Previous")
button3 = tk.Button(window,text="Next>")
button4 = tk.Button(window,text="Search By Name")

# Button Grid

button1.grid(row = 4, column = 2)
button2.grid(row = 4, column = 0)
button2.grid(sticky=W)
button3.grid(row = 4, column = 4)
button3.grid(sticky=E)
button4.grid(row = 0, column = 3)
button4.grid(sticky=E)

window.mainloop()