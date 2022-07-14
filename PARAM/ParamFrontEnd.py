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

def paramclick():
    global paramCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    paramCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#ffffc5")
    #rightPanels.append(paramCanvas)
    paramCanvas.pack()
    #NOITE
    tk.Label(paramCanvas,text=" - NOITE").grid(column=0,row=1)
    global NOITE
    NOITE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=NOITE).grid(column=1,row=1)
    #KDATA
    tk.Label(paramCanvas,text=" - KDATA").grid(column=0,row=2)
    global KDATA
    KDATA= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=KDATA).grid(column=1,row=2)
    #MCYC
    tk.Label(paramCanvas,text=" - MCYC").grid(column=0,row=3)
    global MCYC
    MCYC = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MCYC).grid(column=1,row=3)
    #MESC
    tk.Label(paramCanvas,text=" - MESC").grid(column=0,row=4)
    global MESC
    MESC = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MESC).grid(column=1,row=4)
    #MCYPR
    tk.Label(paramCanvas,text=" - MCYPR").grid(column=0,row=5)
    global MCYPR
    MCYPR = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MCYPR).grid(column=1,row=5)
    #MOP (I) I=1,24
    tk.Label(paramCanvas,text=" - MOP (I) I=1,24").grid(column=0,row=6)
    global MOPII124
    MOPII124 = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MOPII124).grid(column=1,row=6)
    #TEXP
    tk.Label(paramCanvas,text=" - TEXP").grid(column=0,row=7)
    global TEXP
    TEXP = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TEXP).grid(column=1,row=7)
    #BE
    tk.Label(paramCanvas,text=" - BE").grid(column=0,row=8)
    global BE
    BE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=BE).grid(column=1,row=8)
    #TSTART
    tk.Label(paramCanvas,text=" - TSTART").grid(column=0,row=9)
    global TSTART
    TSTART= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TSTART).grid(column=1,row=9)
    #TIMAX
    tk.Label(paramCanvas,text=" - TIMAX").grid(column=0,row=10)
    global TIMAX
    TIMAX= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TIMAX).grid(column=1,row=10)
    #DELTEN OR NDLT
    tk.Label(paramCanvas,text="DELTEN or NDLT?").grid(column=0,row=11)
    global DELTENORNDLT
    DELTENORNDLT = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DELTENORNDLT).grid(column=1,row=11)
    #DELTMX
    tk.Label(paramCanvas,text=" - DELTMX").grid(column=0,row=12)
    global DELTMX
    DELTMX = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DELTMX).grid(column=1,row=12)
    #ELST
    tk.Label(paramCanvas,text=" - ELST").grid(column=0,row=13)
    global ELST
    ELST = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=ELST).grid(column=1,row=13)
    #GF
    tk.Label(paramCanvas,text=" - GF").grid(column=0,row=14)
    global GF
    GF = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=GF).grid(column=1,row=14)
    #REDLT
    tk.Label(paramCanvas,text=" - REDLT").grid(column=0,row=15)
    global REDLT
    REDLT = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=REDLT).grid(column=1,row=15)
    #SCALE
    tk.Label(paramCanvas,text=" - SCALE").grid(column=0,row=16)
    global SCALE
    SCALE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=SCALE).grid(column=1,row=16)
    #SAVE
    def paramSave():
        param = []
        param = [NOITE.get(),KDATA.get(),MCYC.get(),MESC.get(),MCYPR.get(),MOPII124.get(),TEXP.get(),BE.get(),TSTART.get(),TIMAX.get(),DELTENORNDLT.get(),DELTMX.get(),ELST.get(),GF.get(),REDLT.get(),SCALE.get()]
        print(param)
    global saveparam
    saveparam = tk.Button(paramCanvas,text="Save BEFORE Switching Page", command=paramSave, bg="#00ff00")
    saveparam.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="PARAM", command=paramclick).place(x=10,y=130)

root.mainloop()