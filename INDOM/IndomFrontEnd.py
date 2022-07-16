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

def indomclick():
    global indomCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    indomCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#b1fbbd")
    #rightPanels.append(indomCanvas)
    indomCanvas.pack()
    #NK
    tk.Label(indomCanvas,text=" - NK").grid(column=0,row=1)
    global NK
    NK = tk.StringVar()
    tk.Entry(indomCanvas,textvariable=NK).grid(column=1,row=1)
    #NEQ
    tk.Label(indomCanvas,text=" - NEQ").grid(column=0,row=2)
    global NEQ
    NEQ= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=NEQ).grid(column=1,row=2)
    #NPH
    tk.Label(indomCanvas,text=" - NPH").grid(column=0,row=3)
    global NPH
    NPH = tk.StringVar()
    tk.Entry(indomCanvas,textvariable=NPH).grid(column=1,row=3)
    #NB
    tk.Label(indomCanvas,text=" - NB").grid(column=0,row=4)
    global NB
    NB = tk.StringVar()
    tk.Entry(indomCanvas,textvariable=NB).grid(column=1,row=4)
    #NKIN
    tk.Label(indomCanvas,text=" - NKIN").grid(column=0,row=5)
    global NKIN
    NKIN = tk.StringVar()
    tk.Entry(indomCanvas,textvariable=NKIN).grid(column=1,row=5)
    #SAVE
    def indomSave():
        indom = []
        indom = [NK.get(),NEQ.get(),NPH.get(),NB.get(),NKIN.get()]
        print(indom)
    global saveindom
    saveindom = tk.Button(indomCanvas,text="Save BEFORE Switching Page", command=indomSave, bg="#00ff00")
    saveindom.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="indom", command=indomclick).place(x=10,y=170)

root.mainloop()