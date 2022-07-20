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

#DIFFU
def diffuclick():
    global diffuCanvas
    clear()
    diffuCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#c5ffff")
    rightPanels.append(diffuCanvas)
    diffuCanvas.pack()
    #FDDIAG(I1)
    tk.Label(diffuCanvas,text="""Diffusion Coefficients for Mass Component 1
(separate by commas) - FDDIAG(I1) - 1 to NPH""",bg="#c5ffff").grid(column=0,row=1)
    global FDDIAGI1
    FDDIAGI1 = tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=FDDIAGI1).grid(column=1,row=1)
    #FDDIAG(I2)
    tk.Label(diffuCanvas,text="""Diffusion Coefficients for Mass Component 2
(separate by commas) - FDDIAG(I2) - 1 to NPH""",bg="#c5ffff").grid(column=0,row=2)
    global FDDIAGI2
    FDDIAGI2= tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=FDDIAGI2).grid(column=1,row=2)
    #NPH
    #SAVE
    def diffuSave():
        diffu = []
        diffu = [FDDIAGI1.get(),FDDIAGI2.get()]
        print(diffu)
    global savediffu
    savediffu = tk.Button(diffuCanvas,text="Save BEFORE Switching Page", command=diffuSave, bg="#00ff00")
    savediffu.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="DIFFU", command=diffuclick).place(x=10,y=290)

root.mainloop()