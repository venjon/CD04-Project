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

def coftclick():
    global coftCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    coftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#b1fbbd")
    #rightPanels.append(coftCanvas)
    coftCanvas.pack()
    #ECOFT
    tk.Label(coftCanvas,bg="#b1fbbd",text="Connection Name - ECOFT").grid(column=0,row=1)
    global ECOFT
    ECOFT = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT).grid(column=1,row=1)
    #SAVE
    def coftSave():
        coft = []
        coft = [ECOFT.get()]
        print(coft)
    global savecoft
    savecoft = tk.Button(coftCanvas,text="Save BEFORE Switching Page", command=coftSave, bg="#00ff00")
    savecoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="COFT", command=coftclick).place(x=10,y=90)

root.mainloop()