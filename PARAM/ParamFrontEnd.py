from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import messagebox,messagebox
from tkinter import ttk
import os
import tkinter
root = tk.Tk()
lcanvas = tk.Canvas(root, width=340, height=800, bg="#f0f0f0")
lcanvas.pack(side="left")
rcanvas = tk.Canvas(root, width=460, height=800, bg="white",)
rcanvas.pack(side="right")

#PARAM
def paramclick():
    global paramCanvas
    clear()
    paramCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffffc5")
    rightPanels.append(paramCanvas)
    paramCanvas.pack()
    #NOITE
    tk.Label(paramCanvas,text="Max Newtonian Iterations per Time Step - NOITE",bg="#ffffc5").grid(column=0,row=1)
    global NOITE
    NOITE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=NOITE).grid(column=1,row=1)
    #KDATA
    tk.Label(paramCanvas,text="Amount to Print (0/1: Select, 2: +Mass/Heat Flux/Flow V, 3: +Prim Vars & Changes) - KDATA",bg="#ffffc5").grid(column=0,row=2)
    global KDATA
    KDATA= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=KDATA).grid(column=1,row=2)
    #MCYC
    tk.Label(paramCanvas,text="Max Time Steps to Calculate - MCYC",bg="#ffffc5").grid(column=0,row=3)
    global MCYC
    MCYC = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MCYC).grid(column=1,row=3)
    #MSEC
    tk.Label(paramCanvas,text="Max Simulation Duration (CPU seconds) - MSEC",bg="#ffffc5").grid(column=0,row=4)
    global MSEC
    MSEC = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MSEC).grid(column=1,row=4)
    #MCYPR
    tk.Label(paramCanvas,text="Printout Interval - MCYPR",bg="#ffffc5").grid(column=0,row=5)
    global MCYPR
    MCYPR = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MCYPR).grid(column=1,row=5)
    #MOP (I) I=1,24
    def mop():
        tk.messagebox.showinfo(title="MOP Descriptions",message="""1: If not 0, short printout for non-convergent iterations will be generated.
2: Main Subroutine - CYCIT
3: Flow and accumulation terms - MULTI
4: Sinks/Sources - QU
5: Equation of State - EOS
6: Linear Equations - LINEQ
7: If not 0, will printout input data w/ calculational choices from MOP(9+)
9: Enter 0 to determine composition of fluid according to relative mobilities in source element, or 1 for source fluid to have same phase composition
10: Interpolation Formulas - Enter 0 for C(S)=CDRY+SPRT(S1)*|CWET-CDRY|, or 1 for CDRY+S1*(CWET-CDRY)
11: 0 for upstream-weighted (WUP) mobilities and permeability, 1 for WUP permeability and mobilities average between adjacent elements, 2 for WUP mobilities and harmonic-weighted perm, 3 for averaged mob and harmonic perm, 4 for harmonic mob and perm
12: 0 for 
*Under Construction*
""")
    tk.Button(paramCanvas,text="MOP (I) I=1 to 24; separate by commas (click for more info)",command=mop,bg="#ffffc5").grid(column=0,row=6)
    global MOPII124
    MOPII124 = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MOPII124).grid(column=1,row=6)
    #TEXP
    tk.Label(paramCanvas,text="Temperature Dependence of Gas Phase Diffusion Coefficient - TEXP",bg="#ffffc5").grid(column=0,row=7)
    global TEXP
    TEXP = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TEXP).grid(column=1,row=7)
    #BE
    tk.Label(paramCanvas,text="Effective Strength of Enhanced Vapor Diffusion - BE",bg="#ffffc5").grid(column=0,row=8)
    global BE
    BE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=BE).grid(column=1,row=8)
    #TSTART
    tk.Label(paramCanvas,text="Start Time of Simulation (seconds) - TSTART",bg="#ffffc5").grid(column=0,row=9)
    global TSTART
    TSTART= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TSTART).grid(column=1,row=9)
    #TIMAX
    tk.Label(paramCanvas,text="End Time of Simulation (seconds) - TIMAX",bg="#ffffc5").grid(column=0,row=10)
    global TIMAX
    TIMAX= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TIMAX).grid(column=1,row=10)
    #DELTEN OR NDLT
    tk.Label(paramCanvas,text="Length of Time Steps (seconds) - DELTEN",bg="#ffffc5").grid(column=0,row=11)
    global DELTENORNDLT
    DELTENORNDLT = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DELTENORNDLT).grid(column=1,row=11)
    #DELTMX
    tk.Label(paramCanvas,text="Upper Limit of Time Step (seconds) - DELTMX",bg="#ffffc5").grid(column=0,row=12)
    global DELTMX
    DELTMX = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DELTMX).grid(column=1,row=12)
    #ELST
    tk.Label(paramCanvas,text="Element to Get Printout of After Time Step - ELST",bg="#ffffc5").grid(column=0,row=13)
    global ELST
    ELST = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=ELST).grid(column=1,row=13)
    #GF
    tk.Label(paramCanvas,text="Magnitude of Gravitational Acceleration (m/sec^2) - GF",bg="#ffffc5").grid(column=0,row=14)
    global GF
    GF = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=GF).grid(column=1,row=14)
    #REDLT
    tk.Label(paramCanvas,text="Time Step Reduction Factor at error - REDLT",bg="#ffffc5").grid(column=0,row=15)
    global REDLT
    REDLT = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=REDLT).grid(column=1,row=15)
    #SCALE
    tk.Label(paramCanvas,text="Size Factor for Mesh - SCALE",bg="#ffffc5").grid(column=0,row=16)
    global SCALE
    SCALE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=SCALE).grid(column=1,row=16)
    #DLTI
    tk.Label(paramCanvas,text="Duration of Step I (separate by commas) - DLT(I)",bg="#ffffc5").grid(column=0,row=17)
    global DLTI
    DLTI = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DLTI).grid(column=1,row=17)
    #RE1
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Mass Components - RE1").grid(column=0,row=18)
    global RE1
    RE1 = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=RE1).grid(column=1,row=18)
    #RE2
    tk.Label(paramCanvas,bg="#ffffc5",text="Balance Equations per Grid Block - RE2").grid(column=0,row=19)
    global RE2
    RE2= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=RE2).grid(column=1,row=19)
    #U
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Phases - U").grid(column=0,row=20)
    global U
    U = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=U).grid(column=1,row=20)
    #WUP
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Secondary Parameters w/o Component Mass Fractions - WUP").grid(column=0,row=21)
    global WUP
    WUP = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=WUP).grid(column=1,row=21)
    #WNR
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Mass Components in INCON - WNR").grid(column=0,row=22)
    global WNR
    WNR = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=WNR).grid(column=1,row=22)
    #DFAC
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Mass Components - DFAC").grid(column=0,row=23)
    global DFAC
    DFAC = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DFAC).grid(column=1,row=23)
    #DEP1
    tk.Label(paramCanvas,bg="#ffffc5",text="Balance Equations per Grid Block - DEP(1)").grid(column=0,row=24)
    global DEP1
    DEP1= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DEP1).grid(column=1,row=24)
    #DEP2
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Phases - DEP(2)").grid(column=0,row=25)
    global DEP2
    DEP2 = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DEP2).grid(column=1,row=25)
    #DEP3
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Secondary Parameters w/o Component Mass Fractions - DEP(3)").grid(column=0,row=26)
    global DEP3
    DEP3 = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DEP3).grid(column=1,row=26)
    #DEP4
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Mass Components in INCON - DEP(4)").grid(column=0,row=27)
    global DEP4
    DEP4 = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DEP4).grid(column=1,row=27)
    #SAVE
    def paramSave():
        param = []
        param = [NOITE.get(),KDATA.get(),MCYC.get(),MSEC.get(),MCYPR.get(),MOPII124.get(),TEXP.get(),BE.get(),TSTART.get(),TIMAX.get(),DELTENORNDLT.get(),DELTMX.get(),ELST.get(),GF.get(),REDLT.get(),SCALE.get(),DLTI.get(),RE1.get(),RE2.get(),U.get(),WUP.get(),WNR.get(),DFAC.get(),DEP1.get(),DEP2.get(),DEP3.get(),DEP4.get()]
        print(param)
    global saveparam
    saveparam = tk.Button(paramCanvas,text="Save BEFORE Switching Page", command=paramSave, bg="#00ff00")
    saveparam.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="PARAM", command=paramclick).place(x=10,y=130)

root.mainloop()