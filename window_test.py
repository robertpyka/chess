from tkinter import *
import tkinter as tk

window = tk.Tk()

#adding pictures
back1 = "#FFF8DC" 	
back2 = "#D2691E"
e = tk.PhotoImage(width=1, height=1)
bP = tk.PhotoImage(file = "images/bP.png")
bR = tk.PhotoImage(file = "images/bR.png")
bQ = tk.PhotoImage(file = "images/bQ.png")
bK = tk.PhotoImage(file = "images/bK.png")
bN = tk.PhotoImage(file = "images/bN.png")
bB = tk.PhotoImage(file = "images/bB.png")
wP = tk.PhotoImage(file = "images/wP.png")
wR = tk.PhotoImage(file = "images/wR.png")
wQ = tk.PhotoImage(file = "images/wQ.png")
wK = tk.PhotoImage(file = "images/wK.png")
wN = tk.PhotoImage(file = "images/wN.png")
wB = tk.PhotoImage(file = "images/wB.png")
tiles={}

pieces = [[bR,bN,bB,bK,bQ,bB,bN,bR],
        [bP,bP,bP,bP,bP,bP,bP,bP],
        [e,e,e,e,e,e,e,e],
        [e,e,e,e,e,e,e,e],
        [e,e,e,e,e,e,e,e],
        [e,e,e,e,e,e,e,e],
        [wP,wP,wP,wP,wP,wP,wP,wP],
        [wR,wN,wB,wK,wQ,wB,wN,wR]]
# creating a chess board
for i in range(8):
    for j in range(8):
        #function if used to set color of button with modulo
        if (i+j)%2 == 0:
            back = back1
        else:
            back = back2
        tiles[(i,j)] = tk.Button(
            master = window,
            relief=tk.FLAT,
            width=80,
            height=80,
            bg = back,
            image= pieces[i][j]
            )
        tiles[i,j].grid(row=i, column=j)

# list of poles
##tiles = [[['a8','b8','c8','d8','e8','f8','g8','h8'],\
##        ['a7','b7','c7','d7','e7','f7','g7','h7'],\
##        ['a6','b6','c6','d6','e6','f6','g6','h6'],\
##        ['a5','b5','c5','d5','e5','f5','g5','h5'],\
##        ['a4','b4','c4','d4','e4','f4','g4','h4'],\
##        ['a3','b3','c3','d3','e3','f3','g3','h3'],\
##        ['a2','b2','c2','d2','e2','f2','g2','h2'],\
##        ['a1','b1','c1','d1','e1','f1','g1','h1']]]
# placing pieces
						
#placing pieces on board

window. mainloop()

