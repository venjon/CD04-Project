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
    indomCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#ffdfa5")
    #rightPanels.append(indomCanvas)
    indomCanvas.pack()
    #MAT
    rockoptions = ["placeholder", "chicken"]
    tk.Label(indomCanvas,text="Material Names - MAT",bg="#ffdfa5").grid(column=0,row=1)
    tk.Label(indomCanvas,text=rockoptions).grid(column=1,row=1)
    #X1
    tk.Label(indomCanvas,text="Primary Variable 1, depending on EOS - X1",bg="#ffdfa5").grid(column=0,row=2)
    global X1
    X1= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=X1).grid(column=1,row=2)
    #X2
    tk.Label(indomCanvas,text="Primary Variable 2, depending on EOS - X2",bg="#ffdfa5").grid(column=0,row=3)
    global X2
    X2 = tk.StringVar()
    tk.Entry(indomCanvas,textvariable=X2).grid(column=1,row=3)
    #X3
    tk.Label(indomCanvas,text="Primary Variable 3, depending on EOS - X3",bg="#ffdfa5").grid(column=0,row=4)
    global X3
    X3 = tk.StringVar()
    tk.Entry(indomCanvas,textvariable=X3).grid(column=1,row=4)
    #X4
    tk.Label(indomCanvas,text="Primary Variable 4, depending on EOS - X4",bg="#ffdfa5").grid(column=0,row=5)
    global X4
    X4 = tk.StringVar()
    tk.Entry(indomCanvas,textvariable=X4).grid(column=1,row=5)
    #SAVE
    def indomSave():
        indom = []
        indom = [rockoptions,X1.get(),X2.get(),X3.get(),X4.get()]
        print(indom)
    global saveindom
    saveindom = tk.Button(indomCanvas,text="Save BEFORE Switching Page", command=indomSave, bg="#00ff00")
    saveindom.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="INDOM", command=indomclick).place(x=10,y=250)

root.mainloop()