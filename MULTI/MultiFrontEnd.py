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

def multiclick():
    global multiCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    multiCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#b1fbbd")
    #rightPanels.append(multiCanvas)
    multiCanvas.pack()
    #NK
    tk.Label(multiCanvas,bg="#b1fbbd",text="Number of Mass Components - NK").grid(column=0,row=1)
    global NK
    NK = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NK).grid(column=1,row=1)
    #NEQ
    tk.Label(multiCanvas,bg="#b1fbbd",text="Balance Equations per Grid Block - NEQ").grid(column=0,row=2)
    global NEQ
    NEQ= tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NEQ).grid(column=1,row=2)
    #NPH
    tk.Label(multiCanvas,bg="#b1fbbd",text="Number of Phases - NPH").grid(column=0,row=3)
    global NPH
    NPH = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NPH).grid(column=1,row=3)
    #NB
    tk.Label(multiCanvas,bg="#b1fbbd",text="Number of Secondary Parameters w/o Component Mass Fractions - NB").grid(column=0,row=4)
    global NB
    NB = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NB).grid(column=1,row=4)
    #NKIN
    tk.Label(multiCanvas,bg="#b1fbbd",text="Number of Mass Components in INCON - NKIN").grid(column=0,row=5)
    global NKIN
    NKIN = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NKIN).grid(column=1,row=5)
    #SAVE
    def multiSave():
        multi = []
        multi = [NK.get(),NEQ.get(),NPH.get(),NB.get(),NKIN.get()]
        multilist=multi
        print(multi)
    global savemulti
    savemulti = tk.Button(multiCanvas,text="Save BEFORE Switching Page", command=multiSave, bg="#00ff00")
    savemulti.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="MULTI", command=multiclick).place(x=10,y=90)
multilist=[]

root.mainloop()
