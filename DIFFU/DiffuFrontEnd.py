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

def diffuclick():
    global diffuCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    diffuCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#b1fbbd")
    #rightPanels.append(diffuCanvas)
    diffuCanvas.pack()
    #NK
    tk.Label(diffuCanvas,text=" - NK").grid(column=0,row=1)
    global NK
    NK = tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=NK).grid(column=1,row=1)
    #NEQ
    tk.Label(diffuCanvas,text=" - NEQ").grid(column=0,row=2)
    global NEQ
    NEQ= tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=NEQ).grid(column=1,row=2)
    #NPH
    tk.Label(diffuCanvas,text=" - NPH").grid(column=0,row=3)
    global NPH
    NPH = tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=NPH).grid(column=1,row=3)
    #NB
    tk.Label(diffuCanvas,text=" - NB").grid(column=0,row=4)
    global NB
    NB = tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=NB).grid(column=1,row=4)
    #NKIN
    tk.Label(diffuCanvas,text=" - NKIN").grid(column=0,row=5)
    global NKIN
    NKIN = tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=NKIN).grid(column=1,row=5)
    #SAVE
    def diffuSave():
        diffu = []
        diffu = [NK.get(),NEQ.get(),NPH.get(),NB.get(),NKIN.get()]
        print(diffu)
    global savediffu
    savediffu = tk.Button(diffuCanvas,text="Save BEFORE Switching Page", command=diffuSave, bg="#00ff00")
    savediffu.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="DIFFU", command=diffuclick).place(x=10,y=170)

root.mainloop()