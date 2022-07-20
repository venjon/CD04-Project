from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
root = tk.Tk()
lcanvas = tk.Canvas(root, width=340, height=800, bg="#f0f0f0")
lcanvas.pack(side="left")
rcanvas = tk.Canvas(root, width=460, height=800, bg="white",)
rcanvas.pack(side="right")

def solvrclick():
    global solvrCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    solvrCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffbebe")
    #rightPanels.append(solvrCanvas)
    solvrCanvas.pack()
    #MATSLV
    tk.Label(solvrCanvas,text="Linear Equation Solver - MATSLV",bg="#ffbebe").grid(column=0,row=1)
    global MATSLV
    MATSLV = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=MATSLV).grid(column=1,row=1)
    #ZPROCS
    tk.Label(solvrCanvas,text="Z-preconditioning - ZPROCS",bg="#ffbebe").grid(column=0,row=2)
    global ZPROCS
    ZPROCS= tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=ZPROCS).grid(column=1,row=2)
    #OPROCS
    tk.Label(solvrCanvas,text="O-preconditioning - OPROCS",bg="#ffbebe").grid(column=0,row=3)
    global OPROCS
    OPROCS = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=OPROCS).grid(column=1,row=3)
    #RITMAX
    tk.Label(solvrCanvas,text="Max # of CG Iterations / Total # of Equations - RITMAX",bg="#ffbebe").grid(column=0,row=4)
    global RITMAX
    RITMAX = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=RITMAX).grid(column=1,row=4)
    #CLOSUR
    tk.Label(solvrCanvas,text="Convergence Criterion for CG Iterations - CLOSUR",bg="#ffbebe").grid(column=0,row=5)
    global CLOSUR
    CLOSUR = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=CLOSUR).grid(column=1,row=5)
    #SAVE
    def solvrSave():
        solvr = []
        solvr = [MATSLV.get(),ZPROCS.get(),OPROCS.get(),RITMAX.get(),CLOSUR.get()]
        print(solvr)
    global savesolvr
    savesolvr = tk.Button(solvrCanvas,text="Save BEFORE Switching Page", command=solvrSave, bg="#00ff00")
    savesolvr.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="SOLVR", command=solvrclick).place(x=10,y=170)

root.mainloop()


#BACKEND!
def fillstring(initial,full_len):
	charsLeft=full_len - len(initial)
	finalstring=""
	if charsLeft < 0:
		for i in range(5):
			finalstring+=initial[i]
	for i in range(charsLeft):
		finalstring+=" "
	finalstring += initial
	return finalstring

#print variables
def addsolvr():
    solvrline="SOLVR----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(solvrline) 
    print(fillstring(MATSLV.get(),1), end="")
    print(fillstring("",2), end="")
    print(fillstring(ZPROCS.get(),2), end="")
    print(fillstring("",3), end="")
    print(fillstring(OPROCS.get(),2), end="")
    print(fillstring(RITMAX.get(),10), end="")
    print(fillstring(CLOSUR.get(),10), end="")
    print()
    
    
#print variables
addsolvr()


