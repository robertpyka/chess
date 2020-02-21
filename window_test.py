from tkinter import *
import tkinter as tk

window = tk.Tk()

#adding pictures
back1 = PhotoImage(file = r"C:\Users\rpyka\Desktop\Nauka programowania\Python\programiki\repozytorium\chess\light.png" )
back2 = PhotoImage(file = r"C:\Users\rpyka\Desktop\Nauka programowania\Python\programiki\repozytorium\chess\dark.png" )
# creating a chess board
for i in range(7):
    for j in range(7):
        #function if used to set color of button with modulo
        if (i+j)%2 == 0:
            back = back1
        else:
            back = back2
        button = tk.Button(
            master = window,
            relief=tk.FLAT,
            width=80,
            height=80,
            image = back,
            )
        button.grid(row=i, column=j)

window. mainloop()

