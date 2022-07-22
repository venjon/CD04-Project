#This is the final merge of all programs
#RUN TO LAUNCH FINAL APP 
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox,messagebox
import os
root = tk.Tk()
#FRONTEND 
rockDict = {}
multi=[]
param=[]
solvr=[]
gener=[]
indom=[]
diffu=[]
selec=[]
times=[]
foft=[]
coft=[]
goft=[]


lcanvas = tk.Canvas(root, width=340, height=800, bg="#f0f0f0")
lcanvas.pack(side="left")
rcanvas = tk.Canvas(root, width=460, height=800, bg="white",)
rcanvas.pack(side="right")
rightPanels=[]
def clear():
  for x in range(len(rightPanels)):
    rightPanels[x].pack_forget()


#TITLE
titleLabel = tk.Label(lcanvas, text="Document Title:").place(x=10, y=10)
var0 = tk.StringVar()
titleEntry = tk.Entry(lcanvas, textvariable=var0)
titleEntry.place(x=207,y=10)
title = var0.get()

#ROCKS
def RocksOptionMenu_SelectionEvent(event):
    global RockChoice
    RockChoice = var1.get()
    clear()
    if RockChoice == "Add Material":
        rc=-1
        newMat = tk.Toplevel(root)
        newMat.geometry("200x100")
        tk.Label(newMat,text="""Enter a name for your new sample
        (preferably 5 characters)
        DO NOT INCLUDE SPACES""").pack()
        global newMatName
        newMatName = tk.StringVar()
        tk.Entry(newMat, width=30, textvariable=newMatName).pack()
        def var3():
            rockoptions.append(newMatName.get())
            newMat.destroy()
            rockList = tk.OptionMenu(lcanvas, var1, *(rockoptions), command = RocksOptionMenu_SelectionEvent).place(x=10,y=50)
            newrockscanvas = tk.Canvas(rcanvas, width=460, height=800, bg="#c1e2fe")
            rockoptionscanvas.append(newrockscanvas)
            rightPanels.append(newrockscanvas)
            rockDict[rockoptions[rc]] = []
            #MAT
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Name of Material - MAT").grid(column=0,row=1)
            global MAT
            MAT = (rockoptions[rc])[0:5]
            tk.Label(rockoptionscanvas[rc],text=MAT, bg="white").grid(column=1,row=1)
            #NAD
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text=" - NAD").grid(column=0,row=2)
            global NAD
            NAD = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=NAD).grid(column=1,row=2)
            #DROK
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Rock Grain Density (kg/m^3) - DROK").grid(column=0,row=3)
            global DROK
            DROK = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=DROK).grid(column=1,row=3)
            #POR
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Porosity (if not included in INCON) - POR").grid(column=0,row=4)
            global POR
            POR = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=POR).grid(column=1,row=4)
            #PER(1)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Absolute Permeability Along Principal Axis 1 - PER(1)").grid(column=0,row=5)
            global PER1
            PER1 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=PER1).grid(column=1,row=5)
            #PER(2)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Absolute Permeability Along Principal Axis 2 - PER(2)").grid(column=0,row=6)
            global PER2
            PER2 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=PER2).grid(column=1,row=6)
            #PER(3)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Absolute Permeability Along Principal Axis 3 - PER(3)").grid(column=0,row=7)
            global PER3
            PER3 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=PER3).grid(column=1,row=7)
            #CWET
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Formation Heat Conductivity in Liquid (W/m°C)- CWET").grid(column=0,row=8)
            global CWET
            CWET = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CWET).grid(column=1,row=8)
            #SPHT
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Rock Grain Specific Heat (J/kg°C) - SPHT").grid(column=0,row=9)
            global SPHT
            SPHT = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=SPHT).grid(column=1,row=9)
            #COM
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Pore Compressibility - COM").grid(column=0,row=10)
            global COM
            COM = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=COM).grid(column=1,row=10)
            #EXPAN
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Pore Expansivity - EXPAN").grid(column=0,row=11)
            global EXPAN
            EXPAN = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=EXPAN).grid(column=1,row=11)
            #CDRY
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Formation Heat Conductivity w/o Liquid (W/m°C) - CDRY").grid(column=0,row=12)
            global CDRY
            CDRY = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CDRY).grid(column=1,row=12)
            #TORTX
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Tortuosity Factor - TORTX").grid(column=0,row=13)
            global TORTX
            TORTX = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=TORTX).grid(column=1,row=13)
            #GK
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Klinkenberg Parameter B [k*(1+b/P)] - GK").grid(column=0,row=14)
            global GK
            GK = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=GK).grid(column=1,row=14)
            #XKD3
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Distribution Coefficient of Parent Radionuclide - XKD3").grid(column=0,row=15)
            global XKD3
            XKD3 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=XKD3).grid(column=1,row=15)
            #XKD4
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Distribution Coefficient of Daughter Radionuclide - XKD4").grid(column=0,row=16)
            global XKD4
            XKD4 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=XKD4).grid(column=1,row=16)
            #RPCAP
            tk.Label(rockoptionscanvas[rc],bg="#bd0505",fg="white",text="Relative Permeability/Capillary Pressure Functions - RPCAP").grid(column=0,row=17,columnspan=2)
            #IRP
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Type of Relative Permeability Function (see Appendix G) - IRP").grid(column=0,row=18)
            global IRP
            IRP = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=IRP).grid(column=1,row=18)
            #RP(1)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 1 for Relative Permeability Function - RP(1)").grid(column=0,row=19)
            global RP1
            RP1 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=RP1).grid(column=1,row=19)
            #RP(2)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 2 for Relative Permeability Function - RP(2)").grid(column=0,row=20)
            global RP2
            RP2 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=RP2).grid(column=1,row=20)
            #RP(3)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 3 for Relative Permeability Function - RP(3)").grid(column=0,row=21)
            global RP3
            RP3 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=RP3).grid(column=1,row=21)
            #RP(4)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 4 for Relative Permeability Function - RP(4)").grid(column=0,row=22)
            global RP4
            RP4 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=RP4).grid(column=1,row=22)
            #RP(5)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 5 for Relative Permeability Function - RP(5)").grid(column=0,row=23)
            global RP5
            RP5 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=RP5).grid(column=1,row=23)
            #RP(6)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 6 for Relative Permeability Function - RP(6)").grid(column=0,row=24)
            global RP6
            RP6 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=RP6).grid(column=1,row=24)
            #RP(7)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 7 for Relative Permeability Function - RP(7)").grid(column=0,row=25)
            global RP7
            RP7 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=RP7).grid(column=1,row=25)
            #ICP
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Type of Capillary Pressure Function (see Appendix G) - ICP").grid(column=0,row=26)
            global ICP
            ICP = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=ICP).grid(column=1,row=26)
            #CP(1)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 1 for Capillary Pressure Function - CP(1)").grid(column=0,row=27)
            global CP1
            CP1 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP1).grid(column=1,row=27)
            #CP(2)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 2 for Capillary Pressure Function - CP(2)").grid(column=0,row=28)
            global CP2
            CP2 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP2).grid(column=1,row=28)
            #CP(3)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 3 for Capillary Pressure Function - CP(3)").grid(column=0,row=29)
            global CP3
            CP3 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP3).grid(column=1,row=29)
            #CP(4)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 4 for Capillary Pressure Function - CP(4)").grid(column=0,row=30)
            global CP4
            CP4 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP4).grid(column=1,row=30)
            #CP(5)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 5 for Capillary Pressure Function - CP(5)").grid(column=0,row=31)
            global CP5
            CP5 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP5).grid(column=1,row=31)
            #CP(6)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 6 for Capillary Pressure Function - CP(6)").grid(column=0,row=32)
            global CP6
            CP6 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP6).grid(column=1,row=32)
            #CP(7)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 7 for Capillary Pressure Function - CP(7)").grid(column=0,row=33)
            global CP7
            CP7= tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP7).grid(column=1,row=33)
            #SAVE
            def rockSave():
                rockDict[rockoptions[rc]] = []
                rockDict[rockoptions[rc]] = [MAT,NAD.get(),DROK.get(), POR.get(), PER1.get(), PER2.get(), PER3.get(), CWET.get(), SPHT.get(), COM.get(), EXPAN.get(), CDRY.get(), TORTX.get(), GK.get(), XKD3.get(), XKD4.get(), IRP.get(), RP1.get(), RP2.get(), RP3.get(), RP4.get(), RP5.get(), RP6.get(), RP7.get(), ICP.get(), CP1.get(), CP2.get(), CP3.get(), CP4.get(), CP5.get(), CP6.get(), CP7.get()]
                print(rockDict)
            global saverock
            saverock = tk.Button(rockoptionscanvas[rc],text="Click to Save When FINISHED (do not return after switching page)", command=rockSave, bg="#00ff00")
            saverock.grid(column=0,row=0,columnspan=2)
        tk.Button(newMat, text="Enter", command=lambda:var3()).pack()
    else:
        rc = rockoptions.index(RockChoice)
        for x in range(1, len(rockoptionscanvas)):
            rockoptionscanvas[x].pack_forget()
        saverock.grid_forget()
        def rockSave2():
            print(rc)
            rockDict[rockoptions[rc]] = [MAT,NAD.get(),DROK.get(), POR.get(), PER1.get(), PER2.get(), PER3.get(), CWET.get(), SPHT.get(), COM.get(), EXPAN.get(), CDRY.get(), TORTX.get(), GK.get(), XKD3.get(), XKD4.get(), IRP.get(), RP1.get(), RP2.get(), RP3.get(), RP4.get(), RP5.get(), RP6.get(), RP7.get(), ICP.get(), CP1.get(), CP2.get(), CP3.get(), CP4.get(), CP5.get(), CP6.get(), CP7.get()]
            print(rockDict)
        saverock.config(command=rockSave2)
        saverock.grid(column=0,row=0,columnspan=2)
        rockoptionscanvas[rc].pack()
        print(rc)

var1 = tk.StringVar()
var1.set("Materials")
rockoptions = ["Add Material"]
rockoptionscanvas = ["placeholder"]
rockList = tk.OptionMenu(lcanvas, var1, *(rockoptions), command = RocksOptionMenu_SelectionEvent)
rockDict = {}
rockList.place(x=10,y=50)

#MULTI
def multiclick():
    global multiCanvas
    clear()
    multiCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#b1fbbd")
    rightPanels.append(multiCanvas)
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
        global multi
        multi = []
        multi = [NK.get(),NEQ.get(),NPH.get(),NB.get(),NKIN.get()]
        multilist=multi
        print(multi)
    global savemulti
    savemulti = tk.Button(multiCanvas,text="Save BEFORE Switching Page", command=multiSave, bg="#00ff00")
    savemulti.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="MULTI", command=multiclick).place(x=10,y=90)
multilist=[]

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
        global param
        param = []
        param = [NOITE.get(),KDATA.get(),MCYC.get(),MSEC.get(),MCYPR.get(),MOPII124.get(),TEXP.get(),BE.get(),TSTART.get(),TIMAX.get(),DELTENORNDLT.get(),DELTMX.get(),ELST.get(),GF.get(),REDLT.get(),SCALE.get(),DLTI.get(),RE1.get(),RE2.get(),U.get(),WUP.get(),WNR.get(),DFAC.get(),DEP1.get(),DEP2.get(),DEP3.get(),DEP4.get()]
        print(param)
    global saveparam
    saveparam = tk.Button(paramCanvas,text="Save BEFORE Switching Page", command=paramSave, bg="#00ff00")
    saveparam.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="PARAM", command=paramclick).place(x=10,y=130)

#SOLVR
def solvrclick():
    global solvrCanvas
    clear()
    solvrCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffbebe")
    rightPanels.append(solvrCanvas)
    solvrCanvas.pack()
    #MATSLV
    tk.Label(solvrCanvas,text="Linear Equation Solver - MATSLV",bg="#ffbebe").grid(column=0,row=1)
    global MATSLV
    MATSLV = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=MATSLV).grid(column=1,row=1)
    #ZPROCS
    tk.Label(solvrCanvas,text="Z-preconditioning - ZPROCS",bg="#ffbebe").grid(column=0,row=2)
    global ZPROCS
    ZPROCS= tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=ZPROCS).grid(column=1,row=2)
    #OPROCS
    tk.Label(solvrCanvas,text="O-preconditioning - OPROCS",bg="#ffbebe").grid(column=0,row=3)
    global OPROCS
    OPROCS = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=OPROCS).grid(column=1,row=3)
    #RITMAX
    tk.Label(solvrCanvas,text="Max # of CG Iterations / Total # of Equations - RITMAX",bg="#ffbebe").grid(column=0,row=4)
    global RITMAX
    RITMAX = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=RITMAX).grid(column=1,row=4)
    #CLOSUR
    tk.Label(solvrCanvas,text="Convergence Criterion for CG Iterations - CLOSUR",bg="#ffbebe").grid(column=0,row=5)
    global CLOSUR
    CLOSUR = tk.StringVar()
    tk.Entry(solvrCanvas,textvariable=CLOSUR).grid(column=1,row=5)
    #SAVE
    def solvrSave():
        global solvr
        solvr = []
        solvr = [MATSLV.get(),ZPROCS.get(),OPROCS.get(),RITMAX.get(),CLOSUR.get()]
        print(solvr)
    global savesolvr
    savesolvr = tk.Button(solvrCanvas,text="Save BEFORE Switching Page", command=solvrSave, bg="#00ff00")
    savesolvr.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="SOLVR", command=solvrclick).place(x=10,y=170)

#GENER

def generclick():
    global generCanvas
    clear()
    #for x in range():
        #rightPanels[x].pack_forget()
    generCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffc5ff")
    rightPanels.append(generCanvas)
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
        global gener
        gener = []
        gener = [EL.get(),NE.get(),SL.get(),NS.get(),NSEQ.get(),NADD.get(),NADS.get(),LTAB.get(),TYPE.get(),ITAB.get(),GX.get(),EX.get(),EX.get(),HG.get(),F1.get(),F2.get(),F3.get()]
        print(gener)
    global savegener
    savegener = tk.Button(generCanvas,text="Save BEFORE Switching Page", command=generSave, bg="#00ff00")
    savegener.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="GENER", command=generclick).place(x=10,y=210)

#INDOM
def indomclick():
    global indomCanvas
    clear()
    indomCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#ffdfa5")
    rightPanels.append(indomCanvas)
    indomCanvas.pack()
    #MAT1
    tk.Label(indomCanvas,text="Material Name(s) - MAT1",bg="#ffdfa5").grid(column=0,row=1)
    global MAT1
    MAT1= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=MAT1).grid(column=1,row=1)
    #X
    tk.Label(indomCanvas,text="Primary Variables; quantity depends on EOS (separate by commas) - X",bg="#ffdfa5").grid(column=0,row=2)
    global X
    X= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=X).grid(column=1,row=2)
    #SAVE
    def indomSave():
        global indom
        indom = []
        indom = [MAT1.get(),X.get()]
        print(indom)
    global saveindom
    saveindom = tk.Button(indomCanvas,text="Save BEFORE Switching Page", command=indomSave, bg="#00ff00")
    saveindom.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="INDOM", command=indomclick).place(x=10,y=250)

#DIFFU
def diffuclick():
    global diffuCanvas
    clear()
    diffuCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#c5ffff")
    rightPanels.append(diffuCanvas)
    diffuCanvas.pack()
    #FDDIAG(I1)
    tk.Label(diffuCanvas,text="""Diffusion Coefficients for Mass Component 1
(separate by commas) - FDDIAG(I1) - 1 to NPH""",bg="#c5ffff").grid(column=0,row=1)
    global FDDIAGI1
    FDDIAGI1 = tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=FDDIAGI1).grid(column=1,row=1)
    #FDDIAG(I2)
    tk.Label(diffuCanvas,text="""Diffusion Coefficients for Mass Component 2
(separate by commas) - FDDIAG(I2) - 1 to NPH""",bg="#c5ffff").grid(column=0,row=2)
    global FDDIAGI2
    FDDIAGI2= tk.StringVar()
    tk.Entry(diffuCanvas,textvariable=FDDIAGI2).grid(column=1,row=2)
    #NPH
    #SAVE
    def diffuSave():
        global diffu
        diffu = []
        diffu = [FDDIAGI1.get(),FDDIAGI2.get()]
        print(diffu)
    global savediffu
    savediffu = tk.Button(diffuCanvas,text="Save BEFORE Switching Page", command=diffuSave, bg="#00ff00")
    savediffu.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="DIFFU", command=diffuclick).place(x=10,y=290)

#SELEC
def selecclick():
    global selecCanvas
    clear()
    selecCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ceae8f")
    rightPanels.append(selecCanvas)
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
        global selec
        selec = []
        selec = [IEI.get(),FEI.get()]
        print(selec)
    global saveselec
    saveselec = tk.Button(selecCanvas,text="Save BEFORE Switching Page", command=selecSave, bg="#00ff00")
    saveselec.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="SELEC", command=selecclick).place(x=10,y=330)

#TIMES
def timesclick():
    global timesCanvas
    clear()
    timesCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#e9d1ff")
    rightPanels.append(timesCanvas)
    timesCanvas.pack()
    #ITI
    tk.Label(timesCanvas,text="Number of Times Provided on Records - ITI",bg="#e9d1ff").grid(column=0,row=1)
    global ITI
    ITI = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=ITI).grid(column=1,row=1)
    #ITE
    tk.Label(timesCanvas,text="Desired Number of Times - ITE",bg="#e9d1ff").grid(column=0,row=2)
    global ITE
    ITE= tk.StringVar()
    tk.Entry(timesCanvas,textvariable=ITE).grid(column=1,row=2)
    #DELAF
    tk.Label(timesCanvas,text="Max Time Step After Prescribed Times are Reached - DELAF",bg="#e9d1ff").grid(column=0,row=3)
    global DELAF
    DELAF = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=DELAF).grid(column=1,row=3)
    #TINTER
    tk.Label(timesCanvas,text="Time Increment for Times w/ Index ITI to ITE- TINTER",bg="#e9d1ff").grid(column=0,row=4)
    global TINTER
    TINTER = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=TINTER).grid(column=1,row=4)
    #TISI
    tk.Label(timesCanvas,text="List of Times at Which Printout is Desired (separate by commas) - TIS(I) - 1 to ITI",bg="#e9d1ff").grid(column=0,row=5)
    global TISI
    TISI = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=TISI).grid(column=1,row=5)
    #SAVE
    def timesSave():
        global times
        times = []
        times = [ITI.get(),ITE.get(),DELAF.get(),TINTER.get(),TISI.get()]
        print(times)
    global savetimes
    savetimes = tk.Button(timesCanvas,text="Save BEFORE Switching Page", command=timesSave, bg="#00ff00")
    savetimes.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="TIMES", command=timesclick).place(x=10,y=370)

#FOFT
def foftclick():
    global foftCanvas
    clear()
    foftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#96fff0")
    rightPanels.append(foftCanvas)
    foftCanvas.pack()
    #EOFT
    tk.Label(foftCanvas,bg="#96fff0",text="Element Name - EOFT").grid(column=0,row=1)
    global EOFT
    EOFT = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT).grid(column=1,row=1)
    #SAVE
    def foftSave():
        global foft
        foft = []
        foft = [EOFT.get()]
        print(foft)
    global savefoft
    savefoft = tk.Button(foftCanvas,text="Save BEFORE Switching Page", command=foftSave, bg="#00ff00")
    savefoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="FOFT", command=foftclick).place(x=10,y=410)

#COFT
def coftclick():
    global coftCanvas
    clear()
    coftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#c0c0c0")
    rightPanels.append(coftCanvas)
    coftCanvas.pack()
    #ECOFT
    tk.Label(coftCanvas,bg="#c0c0c0",text="Connection Name (pair of element names) - ECOFT").grid(column=0,row=1)
    global ECOFT
    ECOFT = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT).grid(column=1,row=1)
    #SAVE
    def coftSave():
        global coft
        coft = []
        coft = [ECOFT.get()]
        print(coft)
    global savecoft
    savecoft = tk.Button(coftCanvas,text="Save BEFORE Switching Page", command=coftSave, bg="#00ff00")
    savecoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="COFT", command=coftclick).place(x=10,y=450)

#GOFT
def goftclick():
    global goftCanvas
    clear()
    goftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffec85")
    rightPanels.append(goftCanvas)
    goftCanvas.pack()
    #EGOFT
    tk.Label(goftCanvas,bg="#ffec85",text="Element that has Sink/Source Defined - EGOFT").grid(column=0,row=1)
    global EGOFT
    EGOFT = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT).grid(column=1,row=1)
    #SAVE
    def goftSave():
        global goft
        goft = []
        goft = [EGOFT.get()]
        print(goft)
    global savegoft
    savegoft = tk.Button(goftCanvas,text="Save BEFORE Switching Page", command=goftSave, bg="#00ff00")
    savegoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="GOFT", command=goftclick).place(x=10,y=490)

root.mainloop()

f=open(var0.get()+".txt","w")
#BACKEND MAIN FUNCTIONS++++++++++++++++++++++++++++
def fillstring(initial,full_len):
	charsLeft=full_len - len(initial)
	finalstring=""
	if charsLeft < 0:
		for i in range(full_len):
			finalstring+=initial[i]
	else:
		for i in range(charsLeft):
			finalstring+=" "
		finalstring += initial
	return finalstring
def separate(bigline, full_len):
	curnum=0
	curstring=""
	for i in range(len(bigline)):
		if(bigline[i]==','):
			curstring=fillstring(curstring,full_len)
			f.write(curstring )
			curnum+=1
			if(curnum%8==0):
				f.write("\n")
			curstring=""
		else:
			curstring+=bigline[i]
	f.write(fillstring(curstring,full_len) )
	curnum+=1
	if(curnum*8==0):
		f.write("\n")
def separateselec1(bigline,full_len):
    curnum=0
    curstring=""
    for i in range(len(bigline)):
        if(bigline[i]==','):
            curstring=fillstring(curstring,full_len)
            f.write(curstring )
            curnum+=1
            if(curnum%16==0):
                f.write("\n")
            curstring=""
        else:
            curstring+=bigline[i]
    f.write(fillstring(curstring,full_len) )
    curnum+=1
    if(curnum*16==0):
        f.write("\n")
def checkfull(listname):
  for x in range(len(listname)):
    if listname[x]!="":
        return True
  return False
#BACKEND INDIVIDUAL FUNCTIONS++++++++++++++++++++++++++++
#VENNELA EDITS

def addrocks(elements):
   # rockline="ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    #f.write (rockline+"\n")
    if(len(elements)==0):
        pass
    else:
        elements.insert(0,"")
        f.write(fillstring(elements[1],5))
        f.write(fillstring(elements[2],5))
        f.write(fillstring(elements[3],10))
        f.write(fillstring(elements[4],10))
        f.write(fillstring(elements[5],10))
        f.write(fillstring(elements[6],10))
        f.write(fillstring(elements[7],10))
        f.write(fillstring(elements[8],10))
        f.write(fillstring(elements[9],10))
        f.write("\n")
        f.write(fillstring(elements[10],10))
        f.write(fillstring(elements[11],10))
        f.write(fillstring(elements[12],10))
        f.write(fillstring(elements[13],10))
        f.write(fillstring(elements[14],10))
        f.write(fillstring(elements[15],10))
        f.write(fillstring(elements[16],10))
        f.write("\n")
        f.write(fillstring(elements[17],5))
        f.write(fillstring("",5))
        f.write(fillstring(elements[18],10))
        f.write(fillstring(elements[19],10))
        f.write(fillstring(elements[20],10))
        f.write(fillstring(elements[21],10))
        f.write(fillstring(elements[22],10))
        f.write(fillstring(elements[23],10))
        f.write(fillstring(elements[24],10))
        f.write("\n")
        f.write(fillstring(elements[25],5))
        f.write(fillstring("",5))
        f.write(fillstring(elements[26],10))
        f.write(fillstring(elements[27],10))
        f.write(fillstring(elements[28],10))
        f.write(fillstring(elements[29],10))
        f.write(fillstring(elements[30],10))
        f.write(fillstring(elements[31],10))
        f.write(fillstring(elements[32],10))
        f.write("\n")


def addmulti():
    multiline="MULTI----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(multiline+"\n")    
    f.write(fillstring(NK.get(),5) )
    f.write(fillstring(NEQ.get(), 5) )
    f.write(fillstring(NPH.get(), 5) )
    f.write(fillstring(NB.get(), 5) )
    f.write(fillstring(NKIN.get(), 5) )
    f.write("\n")


def addparam():
    paramline="PARAM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(paramline+"\n")    
    f.write(fillstring(NOITE.get(),2) )
    f.write(fillstring(KDATA.get(),2) )
    f.write(fillstring(MCYC.get(),4) )
    f.write(fillstring(MSEC.get(),4) )
    f.write(fillstring(MCYPR.get(),4 ) )
    
    charsLeft=24- len(MOPII124.get())
    finalstring=""
    if charsLeft < 0:
        for i in range(24):
            finalstring+=MOPII124.get()[i]
    else:
        finalstring += MOPII124.get()
        for i in range(charsLeft):
            finalstring+=" "
         
    f.write(finalstring) 
    f.write(fillstring("",10) )
    f.write(fillstring(TEXP.get(), 10) )
    f.write(fillstring(BE.get(), 10) )
    f.write(fillstring("",10) )
    f.write("\n")
    f.write(fillstring(TSTART.get(), 10) )
    f.write(fillstring(TIMAX.get(), 10) )
    f.write(fillstring(DELTENORNDLT.get(), 10) )
    f.write(fillstring(DELTMX.get(), 10) )
    f.write(fillstring(ELST.get(), 5) )
    f.write(fillstring("", 5) )
    f.write(fillstring(GF.get(),10) )
    f.write(fillstring(REDLT.get(), 10) )
    f.write(fillstring(SCALE.get(), 10) )
    f.write("\n")
    separate(DLTI.get(),10)
    f.write("\n")
    f.write(fillstring(RE1.get(), 10) )
    f.write(fillstring(RE2.get(), 10) )
    f.write(fillstring(U.get(), 10) )
    f.write(fillstring(WUP.get(), 10) )
    f.write(fillstring(WNR.get(), 10) )
    f.write(fillstring(DFAC.get(), 10) )
    f.write("\n")
    f.write(fillstring(DEP1.get(), 20) )
    f.write(fillstring(DEP2.get(), 20) )
    f.write(fillstring(DEP3.get(), 20) )
    f.write(fillstring(DEP4.get(), 20) )
    f.write("\n")
  

def addsolvr():
    solvrline="SOLVR----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(solvrline+"\n") 
    f.write(fillstring(MATSLV.get(),1) )
    f.write(fillstring("",2) )
    f.write(fillstring(ZPROCS.get(),2) )
    f.write(fillstring("",3) )
    f.write(fillstring(OPROCS.get(),2) )
    f.write(fillstring(RITMAX.get(),10) )
    f.write(fillstring(CLOSUR.get(),10) )
    f.write("\n")


def addrpcap(elements):
    rpcapline="RPCAP----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write (rpcapline+"\n")
    #elements.insert(0,"")
    if(len(elements)<17):
        return
    f.write (fillstring(elements[17],5) )
    f.write(fillstring("",5) )
    f.write (fillstring(elements[18],10) )
    f.write (fillstring(elements[19],10) )
    f.write (fillstring(elements[20],10) )
    f.write (fillstring(elements[21],10) )
    f.write (fillstring(elements[22],10) )
    f.write (fillstring(elements[23],10) )
    f.write (fillstring(elements[24],10) )
    f.write("\n")
    f.write (fillstring(elements[25],5) )
    f.write(fillstring("",5) )
    f.write (fillstring(elements[26],10) )
    f.write (fillstring(elements[27],10) )
    f.write (fillstring(elements[28],10) )
    f.write (fillstring(elements[29],10) )
    f.write (fillstring(elements[30],10) )
    f.write (fillstring(elements[31],10) )
    f.write (fillstring(elements[32],10) )
    f.write("\n")
  
#single gener: 
def addGener():
    generline="GENER----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(generline+"\n")    
    f.write(fillstring(EL.get(),3))
    f.write(fillstring(NE.get(),2))
    f.write(fillstring(SL.get(),3))
    f.write(fillstring(NS.get(),2))
    f.write(fillstring(NSEQ.get(),5))
    f.write(fillstring(NADD.get(),5))
    f.write(fillstring(NADS.get(),5))
    f.write(fillstring(LTAB.get(),5))
    f.write(fillstring("",5))
    f.write(fillstring(TYPE.get(),4))
    f.write(fillstring(ITAB.get(),1))
    f.write(fillstring(GX.get(),10))
    f.write(fillstring(EX.get(),10))
    f.write(fillstring(HG.get(),10))#HX??
    f.write("\n")
    separate(F1.get(),10)
    f.write("\n")
    separate(F2.get(),10)
    f.write("\n")
    separate(F3.get(),10)
    f.write("\n")
#multiple gener
def addgener2(elements):
    generline="GENER----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(generline)    
    f.write(fillstring(elements[0],3) )
    f.write(fillstring(elements[1],2) )
    f.write(fillstring(elements[2],3) )
    f.write(fillstring(elements[3],2) )
    f.write(fillstring(elements[4],5) )
    f.write(fillstring(elements[5],5) )
    f.write(fillstring(elements[6],5) )
    f.write(fillstring(elements[7],5) )
    f.write(fillstring("",5) )
    f.write(fillstring(elements[8],4) )
    f.write(fillstring(elements[9],1) )
    f.write(fillstring(elements[10],10) )
    f.write(fillstring(elements[11],10) )
    f.write(fillstring(elements[12],10) )
    f.write("\n")
    separate(elements[13],14)
    f.write("\n")
    separate(elements[14],14)
    f.write("\n")
    separate(elements[15],14)
    f.write("\n")

def addindom():
    indomline="INDOM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(indomline +"\n")    
    f.write(fillstring(MAT1.get(),5) )
    f.write("\n")
    separate(X.get(),20)
    f.write("\n")


def addDiffu():
    diffuline="DIFFU----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(diffuline+"\n")    
    separate(FDDIAGI1.get(),10)
    separate(FDDIAGI2.get(),10)
    f.write("\n")

def addselec():
    selecline="SELEC----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(selecline+"\n")    
    separateselec1(IEI.get(),5)
    f.write("\n")
    separate(FEI.get(),10)
    f.write("\n")
    f.write("\n")
  
def addTimes():
    Timesline="TIMES----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(Timesline+"\n")    
    f.write(fillstring(ITI.get(),5) )
    f.write(fillstring(ITE.get(),5) )
    f.write(fillstring(DELAF.get(),10) )
    f.write(fillstring(TINTER.get(),10) )
    f.write("\n")
    separate(TISI.get(),10)
    #f.write TIS(1)-TIS(ITI)

    f.write("\n")
    
def addFOFT():
    FOFTline="FOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(FOFTline+"\n")    
    f.write(fillstring(EOFT.get(),5) )
    f.write("\n")


def addCOFT():
    COFTline="COFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(COFTline+"\n")    
    f.write(fillstring(ECOFT.get(),10) )
    f.write("\n")

def addGOFT():
    GOFTline="GOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    f.write(GOFTline+"\n")    
    f.write(fillstring(EGOFT.get(),5) )
    f.write("\n")

#BACKEND RUNS------ONLY PLACE WHERE PRINTING SHOULD HAPPEN
#all the for loops checking if lists are empty

#f.write title

f.write(var0.get()[0:80] + "\n")

rockline="ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
f.write (rockline+"\n")

for key in rockDict:
  dummy = rockDict[key]
  addrocks(dummy)

startline='''START----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8
----*----1-MOP: 123456789*123456789*1234----*----5----*----6----*----7----*----8'''

f.write(startline+"\n")

if(checkfull(multi)):
  addmulti()

if(checkfull(param)):
  addparam()
  
if(checkfull(solvr)):
  addsolvr()

if(bool(rockDict)==False):
    pass
else:
    for key in rockDict:
        dummy = rockDict[key]
        addrpcap(dummy)
        break

#GENER
if(checkfull(gener)):
  addGener()
    
if(checkfull(indom)):
  addindom()
  
if(checkfull(diffu)):
  addDiffu()

if(checkfull(times)):
  addTimes()

if(checkfull(selec)):
  addselec()
  
if(checkfull(foft)):
  addFOFT()
   
if(checkfull(coft)):
  addCOFT()

if(checkfull(goft)):
  addGOFT()
  

#f.write ending line
f.write("ENDCY----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8")
#PROGRAM OVER---------------------

f.close()