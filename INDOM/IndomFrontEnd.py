from difflib import Match
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
root = tk.Tk()
lcanvas = tk.Canvas(root, width=400, height=800, bg="#f0f0f0")
lcanvas.pack(side="left")
rcanvas = tk.Canvas(root, width=400, height=800, bg="white",)
rcanvas.pack(side="right")

#INDOM
def indomclick():
    global indomCanvas
    clear()
    indomCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#ffdfa5")
    rightPanels.append(indomCanvas)
    indomCanvas.pack()
    #MAT1
    tk.Label(indomCanvas,text="Material Name(s) - MAT1",bg="#ffdfa5").grid(column=0,row=1)
    global MAT1
    MAT1= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=MAT1).grid(column=1,row=1)
    #X
    tk.Label(indomCanvas,text="Primary Variables; quantity depends on EOS (separate by commas) - X",bg="#ffdfa5").grid(column=0,row=2)
    global X
    X= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=X).grid(column=1,row=2)
    #SAVE
    def indomSave():
        indom = []
        indom = [MAT1.get(),X.get()]
        print(indom)
    global saveindom
    saveindom = tk.Button(indomCanvas,text="Save BEFORE Switching Page", command=indomSave, bg="#00ff00")
    saveindom.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="INDOM", command=indomclick).place(x=10,y=250)

root.mainloop()