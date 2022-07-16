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

def goftclick():
    global goftCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    goftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#b1fbbd")
    #rightPanels.append(goftCanvas)
    goftCanvas.pack()
    #EGOFT
    tk.Label(goftCanvas,bg="#b1fbbd",text="Element that has Sink/Source Defined - EGOFT").grid(column=0,row=1)
    global EGOFT
    EGOFT = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT).grid(column=1,row=1)
    #SAVE
    def goftSave():
        goft = []
        goft = [EGOFT.get()]
        print(goft)
    global savegoft
    savegoft = tk.Button(goftCanvas,text="Save BEFORE Switching Page", command=goftSave, bg="#00ff00")
    savegoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="GOFT", command=goftclick).place(x=10,y=90)

root.mainloop()