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

def generclick():
    global generCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    generCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffc5ff")
    #rightPanels.append(generCanvas)
    generCanvas.pack()
    #EL
    tk.Label(generCanvas,text="Element Code Name w/ source (Part 1) - EL",bg="#ffc5ff").grid(column=0,row=1)
    global EL
    EL = tk.StringVar()
    tk.Entry(generCanvas,textvariable=EL).grid(column=1,row=1)
    #NE
    tk.Label(generCanvas,text="Element Code Name w/ source (Part 2) - NE",bg="#ffc5ff").grid(column=0,row=2)
    global NE
    NE= tk.StringVar()
    tk.Entry(generCanvas,textvariable=NE).grid(column=1,row=2)
    #SL
    tk.Label(generCanvas,text="Sink Code Name (Part 1) - SL",bg="#ffc5ff").grid(column=0,row=3)
    global SL
    SL = tk.StringVar()
    tk.Entry(generCanvas,textvariable=SL).grid(column=1,row=3)
    #NS
    tk.Label(generCanvas,text="Sink Code Name (Part 2) - NS",bg="#ffc5ff").grid(column=0,row=4)
    global NS
    NS = tk.StringVar()
    tk.Entry(generCanvas,textvariable=NS).grid(column=1,row=4)
    #NSEQ
    tk.Label(generCanvas,text="Additional Sink Quantity w/ Equal Injection Rate - NSEQ",bg="#ffc5ff").grid(column=0,row=5)
    global NSEQ
    NSEQ = tk.StringVar()
    tk.Entry(generCanvas,textvariable=NSEQ).grid(column=1,row=5)
    #NADD
    tk.Label(generCanvas,text="Increment Between Code Numbers of Successive Elements w/ Same Sink - NADD",bg="#ffc5ff").grid(column=0,row=6)
    global NADD
    NADD = tk.StringVar()
    tk.Entry(generCanvas,textvariable=NADD).grid(column=1,row=6)
    #NADS
    tk.Label(generCanvas,text="Increment Between Code Numbers of Successive Sinks- NADS",bg="#ffc5ff").grid(column=0,row=7)
    global NADS
    NADS = tk.StringVar()
    tk.Entry(generCanvas,textvariable=NADS).grid(column=1,row=7)
    #LTAB
    tk.Label(generCanvas,text="No. of Pts in Generation Table / Time. 0 or 1 = constant rate - LTAB",bg="#ffc5ff").grid(column=0,row=8)
    global LTAB
    LTAB = tk.StringVar()
    tk.Entry(generCanvas,textvariable=LTAB).grid(column=1,row=8)
    #TYPE
    tk.Label(generCanvas,text="Fluid/Heat Production Options - TYPE",bg="#ffc5ff").grid(column=0,row=9)
    global TYPE
    TYPE= tk.StringVar()
    tk.Entry(generCanvas,textvariable=TYPE).grid(column=1,row=9)
    #ITAB
    tk.Label(generCanvas,text="Specific Enthalpies - ITAB",bg="#ffc5ff").grid(column=0,row=10)
    global ITAB
    ITAB= tk.StringVar()
    tk.Entry(generCanvas,textvariable=ITAB).grid(column=1,row=10)
    #GX
    tk.Label(generCanvas,text="Constant Generation Rate, - for production, + for injection - GX",bg="#ffc5ff").grid(column=0,row=11)
    global GX
    GX = tk.StringVar()
    tk.Entry(generCanvas,textvariable=GX).grid(column=1,row=11)
    #EX
    tk.Label(generCanvas,text="Fixed Specific Enthalpy of Fluid for Injection (J/kg) - EX",bg="#ffc5ff").grid(column=0,row=12)
    global EX
    EX = tk.StringVar()
    tk.Entry(generCanvas,textvariable=EX).grid(column=1,row=12)
    #HG
    tk.Label(generCanvas,text="Layer Thickness (m) - HG",bg="#ffc5ff").grid(column=0,row=13)
    global HG
    HG = tk.StringVar()
    tk.Entry(generCanvas,textvariable=HG).grid(column=1,row=13)
    #F1
    tk.Label(generCanvas,text="Generation Times (separate by commas) - F1 - 1 to LTAB",bg="#ffc5ff").grid(column=0,row=14)
    global F1
    F1 = tk.StringVar()
    tk.Entry(generCanvas,textvariable=F1).grid(column=1,row=14)
    #F2
    tk.Label(generCanvas,text="Generation Rates (separate by commas) - F2 - 1 to LTAB",bg="#ffc5ff").grid(column=0,row=15)
    global F2
    F2 = tk.StringVar()
    tk.Entry(generCanvas,textvariable=F2).grid(column=1,row=15)
    #F3
    tk.Label(generCanvas,text="Specific Enthalpy of Fluid (separate by commas) - F3 - 1 to LTAB",bg="#ffc5ff").grid(column=0,row=16)
    global F3
    F3 = tk.StringVar()
    tk.Entry(generCanvas,textvariable=F3).grid(column=1,row=16)
    #SAVE
    def generSave():
        gener = []
        gener = [EL.get(),NE.get(),SL.get(),NS.get(),NSEQ.get(),NADD.get(),NADS.get(),LTAB.get(),TYPE.get(),ITAB.get(),GX.get(),EX.get(),EX.get(),HG.get(),F1.get(),F2.get(),F3.get()]
        print(gener)
    global savegener
    savegener = tk.Button(generCanvas,text="Save BEFORE Switching Page", command=generSave, bg="#00ff00")
    savegener.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="GENER", command=generclick).place(x=10,y=210)

root.mainloop()