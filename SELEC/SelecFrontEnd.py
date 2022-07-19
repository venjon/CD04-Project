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

def selecclick():
    global selecCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    selecCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffbebe")
    #rightPanels.append(selecCanvas)
    selecCanvas.pack()
    #MATSLV
    tk.Label(selecCanvas,text="Linear Equation Solver - MATSLV",bg="#ffbebe").grid(column=0,row=1)
    global MATSLV
    MATSLV = tk.StringVar()
    tk.Entry(selecCanvas,textvariable=MATSLV).grid(column=1,row=1)
    #ZPROCS
    tk.Label(selecCanvas,text="Z-preconditioning - ZPROCS",bg="#ffbebe").grid(column=0,row=2)
    global ZPROCS
    ZPROCS= tk.StringVar()
    tk.Entry(selecCanvas,textvariable=ZPROCS).grid(column=1,row=2)
    #OPROCS
    tk.Label(selecCanvas,text="O-preconditioning - OPROCS",bg="#ffbebe").grid(column=0,row=3)
    global OPROCS
    OPROCS = tk.StringVar()
    tk.Entry(selecCanvas,textvariable=OPROCS).grid(column=1,row=3)
    #RITMAX
    tk.Label(selecCanvas,text="Max # of CG Iterations / Total # of Equations - RITMAX",bg="#ffbebe").grid(column=0,row=4)
    global RITMAX
    RITMAX = tk.StringVar()
    tk.Entry(selecCanvas,textvariable=RITMAX).grid(column=1,row=4)
    #CLOSUR
    tk.Label(selecCanvas,text="Convergence Criterion for CG Iterations - CLOSUR",bg="#ffbebe").grid(column=0,row=5)
    global CLOSUR
    CLOSUR = tk.StringVar()
    tk.Entry(selecCanvas,textvariable=CLOSUR).grid(column=1,row=5)
    #SAVE
    def selecSave():
        selec = []
        selec = [MATSLV.get(),ZPROCS.get(),OPROCS.get(),RITMAX.get(),CLOSUR.get()]
        print(selec)
    global saveselec
    saveselec = tk.Button(selecCanvas,text="Save BEFORE Switching Page", command=selecSave, bg="#00ff00")
    saveselec.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="SELEC", command=selecclick).place(x=10,y=170)

root.mainloop()