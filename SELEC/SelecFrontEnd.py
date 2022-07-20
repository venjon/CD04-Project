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
    selecCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ceae8f")
    #rightPanels.append(selecCanvas)
    selecCanvas.pack()
    #IEI
    tk.Label(selecCanvas,text="""Number of Records w/ Floating Point Numbers That Will Be Read
(separate by commas) - IE(I) - I=1 to 16""",bg="#ceae8f").grid(column=0,row=1)
    global IEI
    IEI = tk.StringVar()
    tk.Entry(selecCanvas,textvariable=IEI).grid(column=1,row=1)
    #FEI
    tk.Label(selecCanvas,text="""Records w/ Floating Point Numbers
as specified in IE(1) (separate by commas) - FE(I) - I=1 to 8*IE(1)""",bg="#ceae8f").grid(column=0,row=2)
    global FEI
    FEI= tk.StringVar()
    tk.Entry(selecCanvas,textvariable=FEI).grid(column=1,row=2)
    #SAVE
    def selecSave():
        selec = []
        selec = [IEI.get(),FEI.get()]
        print(selec)
    global saveselec
    saveselec = tk.Button(selecCanvas,text="Save BEFORE Switching Page", command=selecSave, bg="#00ff00")
    saveselec.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="SELEC", command=selecclick).place(x=10,y=330)

root.mainloop()