#This is the final merge of all programs
#RUN TO LAUNCH FINAL APP 
from operator import truediv
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import os
root = tk.Tk()
#FRONTEND 
rockDict = {}
multi=[]
param=[]
solvr=[]
#gener=[]
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
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 3 for Capillary Pressure Function - CP(3)").grid(column=0,row=28)
            global CP3
            CP3 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP3).grid(column=1,row=28)
            #CP(4)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 4 for Capillary Pressure Function - CP(4)").grid(column=0,row=29)
            global CP4
            CP4 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP4).grid(column=1,row=29)
            #CP(5)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 5 for Capillary Pressure Function - CP(5)").grid(column=0,row=30)
            global CP5
            CP5 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP5).grid(column=1,row=30)
            #CP(6)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 6 for Capillary Pressure Function - CP(6)").grid(column=0,row=31)
            global CP6
            CP6 = tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP6).grid(column=1,row=31)
            #CP(7)
            tk.Label(rockoptionscanvas[rc],bg="#c1e2fe",text="Parameter 7 for Capillary Pressure Function - CP(7)").grid(column=0,row=32)
            global CP7
            CP7= tk.StringVar()
            tk.Entry(rockoptionscanvas[rc],textvariable=CP7).grid(column=1,row=32)
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
    def neq():
        tk.messagebox.showinfo(message="Number of balance equations per grid block. Usually we have NEQ = NK + 1, for solving NK mass and one energy balance equation. Some EOS modules allow the option NEQ = NK, in which case only NK mass balances and no energy equation will be solved.")
    tk.Button(multiCanvas,bg="#b1fbbd",text="Balance Equations per Grid Block - NEQ (click for more info)", command=neq).grid(column=0,row=2)
    global NEQ
    NEQ= tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NEQ).grid(column=1,row=2)
    #NPH
    def nph():
        tk.messagebox.showinfo(message="Number of phases that can be present (2 for most EOS modules).")
    tk.Button(multiCanvas,command=nph,bg="#b1fbbd",text="Number of Phases - NPH (click for more info)").grid(column=0,row=3)
    global NPH
    NPH = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NPH).grid(column=1,row=3)
    #NB
    def nb():
        tk.messagebox.showinfo(message="Number of secondary parameters in the PAR-array (see Fig. 3) other than component mass fractions. Available options include NB = 6 (no diffusion) and NB = 8 (include diffusion).")
    tk.Button(multiCanvas,bg="#b1fbbd",text="Number of Secondary Parameters w/o Component Mass Fractions - NB (click for more info)", command=nb).grid(column=0,row=4)
    global NB
    NB = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NB).grid(column=1,row=4)
    #NKIN
    def nkin():
        tk.messagebox.showinfo(message="Number of mass components in INCON data (default is NKIN = NK). This parameter can be used, for example, to initialize an EOS7R simulation (NK = 4 or 5) from data generated by EOS7 (NK = 2 or 3). If a value other than the default is to be used, then data block MULTI must appear before any initial conditions in data blocks PARAM, INDOM, or INCON.")
    tk.Button(multiCanvas,command=nkin,bg="#b1fbbd",text="Number of Mass Components in INCON - NKIN").grid(column=0,row=5)
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
    def noite():
        tk.messagebox.showinfo(message="Specifies the maximum number of Newtonian iterations per time step (default is 8)")
    tk.Button(paramCanvas,command=noite,text="Max Newtonian Iterations per Time Step - NOITE (?)",bg="#ffffc5").grid(column=0,row=1)
    global NOITE
    NOITE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=NOITE).grid(column=1,row=1)
    #KDATA
    def kdata():
        tk.messagebox.showinfo(message="""Specifies amount of printout (default is 1).
0 or 1: print a selection of the most important variables.
2: in addition, print mass and heat fluxes and flow velocities.
3: in addition, print primary variables and their changes.
If the above values for KDATA are increased by 10, printout will occur after each Newton-Raphson iteration (not just after convergence).""")
    tk.Button(paramCanvas,command=kdata,text="Amount to Print - KDATA (?)",bg="#ffffc5").grid(column=0,row=2)
    global KDATA
    KDATA= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=KDATA).grid(column=1,row=2)
    #MCYC
    tk.Label(paramCanvas,text="Max Time Steps to Calculate - MCYC",bg="#ffffc5").grid(column=0,row=3)
    global MCYC
    MCYC = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MCYC).grid(column=1,row=3)
    #MSEC
    def msec():
        tk.messagebox.showinfo(message="Maximum duration, in CPU seconds, of the simulation (default is infinite).")
    tk.Button(paramCanvas,command=msec,text="Max Simulation Duration (CPU seconds) - MSEC (?)",bg="#ffffc5").grid(column=0,row=4)
    global MSEC
    MSEC = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=MSEC).grid(column=1,row=4)
    #MCYPR
    def mcypr():
        tk.messagebox.showinfo(message="Printout will occur for every multiple of MCYPR steps (default is 1).")
    tk.Button(paramCanvas,command=mcypr,text="Printout Interval - MCYPR (?)",bg="#ffffc5").grid(column=0,row=5)
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
12: 0 for triple linear interpolation, 1 for step function option (rates and enthalpies are taken as averages of the table values corresponding to the beginning and end of the time step), 2 for rigorous step rate capability for time dependent generation data
13: Used by dispersion module T2DM (see manual)
14: (void)
15: 0 for heat exchange being off, 1 for it on
16: provides automatic time step control. Time step size will be doubled if convergence occurs within ITER # MOP(16) Newton-Raphson iterations. It is recommended to set MOP(16) in the range of 2 - 4.
17: (void)
18: 0 for performing upstream weighting for interface density, >0 for average interface density between the two grid blocks. However, when one of the two phase saturations is zero, upstream weighting will be performed.
19: Switch used by different EOS modules for conversion of primary variables; see EOS description, section 6.
20: Switch for vapor pressure lowering in EOS4; see Table 10.
21: Selects the linear equation solver; 0 for defaulting to MOP(21)=3, DSLUCS, Lanczos-tyhpe preconditioned bi-conjugate gradient solver; 1 for (void); 2 for DSLUBC, bi-conjugate gradient solver; 3 for DSLUCS (default); 4 for DLSUGM, generalized minimum residual preconditioned conjugate gradient solver; 5 for DLUSTB, stabilized bi-conjugate gradient solver; 6 for LUBAND, banded direct solver
22: Used by dispersion module T2DM
23: Used by dispersion module T2DM
24: Determines handling of multiphase diffusive fluxes at interfaces; 0 for harmonic weighting of fully coupled effective multiphase
diffusivity, 1 for separate harmonic weighting of gas and liquid phase diffusivities""")
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
    def be():
        tk.messagebox.showinfo(message="(optional) Parameter for effective strength of enhanced vapor diffusion; if set to a non-zero value, will replace the parameter group )000, for vapor diffusion (see Eq. D.3 and section D.4).")
    tk.Button(paramCanvas,text="Effective Strength of Enhanced Vapor Diffusion - BE (?)",command=be,bg="#ffffc5").grid(column=0,row=8)
    global BE
    BE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=BE).grid(column=1,row=8)
    #TSTART
    def tstart():
        tk.messagebox.showinfo(message="Starting time of simulation in seconds (default is 0).")
    tk.Button(paramCanvas,command=tstart,text="Start Time of Simulation (seconds) - TSTART (?)",bg="#ffffc5").grid(column=0,row=9)
    global TSTART
    TSTART= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TSTART).grid(column=1,row=9)
    #TIMAX
    def timax():
        tk.messagebox.showinfo(message="Time in seconds at which simulation should stop (default is infinite).")
    tk.Button(paramCanvas,command=timax,text="End Time of Simulation (seconds) - TIMAX (?)",bg="#ffffc5").grid(column=0,row=10)
    global TIMAX
    TIMAX= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=TIMAX).grid(column=1,row=10)
    #DELTEN OR NDLT
    def deltenorndlt():
        tk.messagebox.showinfo(message="Length of time steps in seconds. If DELTEN is a negative integer, DELTEN = -NDLT, the program will proceed to read NDLT records with time step information. Note that - NDLT must be provided as a floating point number, with decimal point.")
    tk.Button(paramCanvas,command=deltenorndlt,text="Length of Time Steps (seconds) - DELTEN (?)",bg="#ffffc5").grid(column=0,row=11)
    global DELTENORNDLT
    DELTENORNDLT = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DELTENORNDLT).grid(column=1,row=11)
    #DELTMX
    def deltmx():
        tk.messagebox.showinfo(message="Upper limit for time step size in seconds (default is infinite)")
    tk.Button(paramCanvas,command=deltmx,text="Upper Limit of Time Step (seconds) - DELTMX (?)",bg="#ffffc5").grid(column=0,row=12)
    global DELTMX
    DELTMX = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DELTMX).grid(column=1,row=12)
    #ELST
    tk.Label(paramCanvas,text="Element to Get Printout of After Time Step - ELST",bg="#ffffc5").grid(column=0,row=13)
    global ELST
    ELST = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=ELST).grid(column=1,row=13)
    #GF
    def gf():
        tk.messagebox.showinfo(message="Magnitude (m/sec^2) of the gravitational acceleration vector. Blank or zero gives \"no gravity\" calculation.")
    tk.Button(paramCanvas,command=gf,text="Magnitude of Gravitational Acceleration (m/sec^2) - GF (?)",bg="#ffffc5").grid(column=0,row=14)
    global GF
    GF = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=GF).grid(column=1,row=14)
    #REDLT
    def redlt():
        tk.messagebox.showinfo(message="Factor by which time step is reduced in case of convergence failure or other problems (default is 4).")
    tk.Button(paramCanvas,command=redlt,text="Time Step Reduction Factor at error - REDLT (?)",bg="#ffffc5").grid(column=0,row=15)
    global REDLT
    REDLT = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=REDLT).grid(column=1,row=15)
    #SCALE
    tk.Label(paramCanvas,text="Size Factor for Mesh - SCALE",bg="#ffffc5").grid(column=0,row=16)
    global SCALE
    SCALE = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=SCALE).grid(column=1,row=16)
    #DLTI
    def dlti():
        tk.messagebox.showinfo(message="Length (in seconds) of time step I. This set of records is optional for DELTEN = - NDLT, a negative integer. Up to 13 records can be read, each containing 8 time step data. If the number of simulated time steps exceeds the number of DLT(I), the simulation will continue with time steps equal to the last non-zero DLT(I) encountered. When automatic time step control is chosen (MOP(16) > 0), time steps following the last DLT(I) input by the user will increase according to the convergence rate of the Newton-Raphson iteration. Automatic time step reduction will occur if the maximum number of Newton-Raphson iterations is exceeded (parameter NOITE, record PARAM.1)")
    tk.Button(paramCanvas,command=dlti,text="Duration of Step I (separate by commas) - DLT(I) (?)",bg="#ffffc5").grid(column=0,row=17)
    global DLTI
    DLTI = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=DLTI).grid(column=1,row=17)
    #RE1
    def re1():
        tk.messagebox.showinfo(message="Convergence criterion for relative error, see Appendix B (default= 10^-5).")
    tk.Button(paramCanvas,command=re1,bg="#ffffc5",text="Number of Mass Components - RE1 (?)").grid(column=0,row=18)
    global RE1
    RE1 = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=RE1).grid(column=1,row=18)
    #RE2
    def re2():
        tk.messagebox.showinfo(message="Convergence criterion for absolute error, see Appendix B (default= 1).")
    tk.Button(paramCanvas,command=re2,bg="#ffffc5",text="Balance Equations per Grid Block - RE2 (?)").grid(column=0,row=19)
    global RE2
    RE2= tk.StringVar()
    tk.Entry(paramCanvas,textvariable=RE2).grid(column=1,row=19)
    #U
    tk.Label(paramCanvas,bg="#ffffc5",text="Number of Phases - U").grid(column=0,row=20)
    global U
    U = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=U).grid(column=1,row=20)
    #WUP
    def wup():
        tk.messagebox.showinfo(message="Upstream weighting factor for mobilities and enthalpies at interfaces (default = 1.0 is recommended). 0 ≤ WUP ≤ 1.")
    tk.Button(paramCanvas,command=wup,bg="#ffffc5",text="Number of Secondary Parameters w/o Component Mass Fractions - WUP (?)").grid(column=0,row=21)
    global WUP
    WUP = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=WUP).grid(column=1,row=21)
    #WNR
    def wnr():
        tk.messagebox.showinfo(message="Weighting factor for increments in Newton/Raphson - iteration (default = 1.0 is recommended). 0 < WNR ≤ 1.")
    tk.Button(paramCanvas,command=wnr,bg="#ffffc5",text="Number of Mass Components in INCON - WNR (?)").grid(column=0,row=22)
    global WNR
    WNR = tk.StringVar()
    tk.Entry(paramCanvas,textvariable=WNR).grid(column=1,row=22)
    #DFAC
    def dfac():
        tk.messagebox.showinfo(message="Increment factor for numerically computing derivatives (default value is DFAC = 10^-k/2, where k, evaluated internally, is the number of significant digits of the floating point processor used; for 64-bit arithmetic, DFAC ≈ 10^-8).")
    tk.Button(paramCanvas,command=dfac,bg="#ffffc5",text="Number of Mass Components - DFAC (?)").grid(column=0,row=23)
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
    def iei():
        tk.messagebox.showinfo(message="Number of records with floating point numbers that will be read (default is IE(1) = 1; maximum values is 64).")
    tk.Button(selecCanvas,command=iei,text="""Number of Records w/ Floating Point Numbers That Will Be Read
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
    def iti():
        tk.messagebox.showinfo(message="Number of times provided on records TIMES.2, TIMES.3, etc., (restriction: ITI ≤ 100).")
    tk.Button(timesCanvas,command=iti,text="Number of Times Provided on Records - ITI (?)",bg="#e9d1ff").grid(column=0,row=1)
    global ITI
    ITI = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=ITI).grid(column=1,row=1)
    #ITE
    def ite():
        tk.messagebox.showinfo(message="Total number of times desired (ITI # ITE # 100; default is ITE = ITI).")
    tk.Button(timesCanvas,command=ite,text="Desired Number of Times - ITE (?)",bg="#e9d1ff").grid(column=0,row=2)
    global ITE
    ITE= tk.StringVar()
    tk.Entry(timesCanvas,textvariable=ITE).grid(column=1,row=2)
    #DELAF
    def delaf():
        tk.messagebox.showinfo(message="Maximum time step size after any of the prescribed times have been reached (default is infinite).")
    tk.Button(timesCanvas,command=delaf,text="Max Time Step After Prescribed Times are Reached - DELAF (?)",bg="#e9d1ff").grid(column=0,row=3)
    global DELAF
    DELAF = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=DELAF).grid(column=1,row=3)
    #TINTER
    def tinter():
        tk.messagebox.showinfo(message="Time increment for times with index ITI, ITI+1, ..., ITE.")
    tk.Button(timesCanvas,command=tinter,text="Time Increment for Times w/ Index ITI to ITE- TINTER",bg="#e9d1ff").grid(column=0,row=4)
    global TINTER
    TINTER = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=TINTER).grid(column=1,row=4)
    #TISI
    def tisi():
        tk.messagebox.showinfo(message="List of times (in ascending order) at which printout is desired.")
    tk.Button(timesCanvas,command=tisi,text="List of Times at Which Printout is Desired (separate by commas) - TIS(I) - 1 to ITI (?)",bg="#e9d1ff").grid(column=0,row=5)
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
    def eoft():
        tk.messagebox.showinfo(message="EOFT is an element name. Repeat for up to 100 elements, one per record. Enter each individual element in each entry box. After the eighth, enter all additional elements in the ninth box, separated by commas.")
    tk.Button(foftCanvas,command=eoft,bg="#96fff0",text="Element Name(s) - EOFT").grid(column=0,row=1)
    global EOFT1
    EOFT1 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT1).grid(column=1,row=1)
    global EOFT2
    EOFT2 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT2).grid(column=0,row=2)
    global EOFT3
    EOFT3 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT3).grid(column=1,row=2)
    global EOFT4
    EOFT4 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT4).grid(column=0,row=3)
    global EOFT5
    EOFT5 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT5).grid(column=1,row=3)
    global EOFT6
    EOFT6 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT6).grid(column=0,row=4)
    global EOFT7
    EOFT7 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT7).grid(column=1,row=4)
    global EOFT8
    EOFT8 = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT8).grid(column=0,row=5)
    global EOFT9
    EOFT9 = tk.StringVar()
    EOFT9.set("separate by commas")
    tk.Entry(foftCanvas,textvariable=EOFT9).grid(column=1,row=5)
    #SAVE
    def foftSave():
        global foft
        foft = []
        foft = [EOFT1.get(),EOFT2.get(),EOFT3.get(),EOFT4.get(),EOFT5.get(),EOFT6.get(),EOFT7.get(),EOFT8.get(),EOFT9.get()]
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
    def ecoft():
        tk.messagebox.showinfo(message="ECOFT is a connection name, i.e., an ordered pair of two element names. Repeat for up to 100 connections, one per record. Enter each individual element in each entry box. After the eighth, enter all additional elements in the ninth box, separated by commas.")
    tk.Button(coftCanvas,command=ecoft,bg="#c0c0c0",text="Element Name(s) - ECOFT").grid(column=0,row=1)
    global ECOFT1
    ECOFT1 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT1).grid(column=1,row=1)
    global ECOFT2
    ECOFT2 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT2).grid(column=0,row=2)
    global ECOFT3
    ECOFT3 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT3).grid(column=1,row=2)
    global ECOFT4
    ECOFT4 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT4).grid(column=0,row=3)
    global ECOFT5
    ECOFT5 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT5).grid(column=1,row=3)
    global ECOFT6
    ECOFT6 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT6).grid(column=0,row=4)
    global ECOFT7
    ECOFT7 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT7).grid(column=1,row=4)
    global ECOFT8
    ECOFT8 = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT8).grid(column=0,row=5)
    global ECOFT9
    ECOFT9 = tk.StringVar()
    ECOFT9.set("separate by commas")
    tk.Entry(coftCanvas,textvariable=ECOFT9).grid(column=1,row=5)
    #SAVE
    def coftSave():
        global coft
        coft = []
        coft = [ECOFT1.get(),ECOFT2.get(),ECOFT3.get(),ECOFT4.get(),ECOFT5.get(),ECOFT6.get(),ECOFT7.get(),ECOFT8.get(),ECOFT9.get()]
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

def goftclick():
    global goftCanvas
    clear()
    goftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffec85")
    rightPanels.append(goftCanvas)
    goftCanvas.pack()
    #EGOFT
    def egoft():
        tk.messagebox.showinfo(message="EGOFT is the name of an element in which a sink/source is defined. Repeat for up to 100 sinks/sources, one per record. When no sinks or sources are specified here, by default tabulation will be made for all. Enter each individual element in each entry box. After the eighth, enter all additional elements in the ninth box, separated by commas.")
    tk.Button(goftCanvas,command=egoft,bg="#ffec85",text="Element Name(s) - EGOFT").grid(column=0,row=1)
    global EGOFT1
    EGOFT1 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT1).grid(column=1,row=1)
    global EGOFT2
    EGOFT2 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT2).grid(column=0,row=2)
    global EGOFT3
    EGOFT3 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT3).grid(column=1,row=2)
    global EGOFT4
    EGOFT4 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT4).grid(column=0,row=3)
    global EGOFT5
    EGOFT5 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT5).grid(column=1,row=3)
    global EGOFT6
    EGOFT6 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT6).grid(column=0,row=4)
    global EGOFT7
    EGOFT7 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT7).grid(column=1,row=4)
    global EGOFT8
    EGOFT8 = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT8).grid(column=0,row=5)
    global EGOFT9
    EGOFT9 = tk.StringVar()
    EGOFT9.set("separate by commas")
    tk.Entry(goftCanvas,textvariable=EGOFT9).grid(column=1,row=5)
    #SAVE
    def goftSave():
        global goft
        goft = []
        goft = [EGOFT1.get(),EGOFT2.get(),EGOFT3.get(),EGOFT4.get(),EGOFT5.get(),EGOFT6.get(),EGOFT7.get(),EGOFT8.get(),EGOFT9.get()]
        print(goft)
    global savegoft
    savegoft = tk.Button(goftCanvas,text="Save BEFORE Switching Page", command=goftSave, bg="#00ff00")
    savegoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="GOFT", command=goftclick).place(x=10,y=490)

root.mainloop()


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
			print(curstring,end="")
			curnum+=1
			if(curnum%8==0):
				print()
			curstring=""
		else:
			curstring+=bigline[i]
	print(fillstring(curstring,full_len),end="")
	curnum+=1
	if(curnum*8==0):
		print()
def separateselec1(bigline,full_len):
    curnum=0
    curstring=""
    for i in range(len(bigline)):
        if(bigline[i]==','):
            curstring=fillstring(curstring,full_len)
            print(curstring,end="")
            curnum+=1
            if(curnum%16==0):
                print()
            curstring=""
        else:
            curstring+=bigline[i]
    print(fillstring(curstring,full_len),end="")
    curnum+=1
    if(curnum*16==0):
        print()
#BACKEND INDIVIDUAL FUNCTIONS++++++++++++++++++++++++++++
#VENNELA EDITS

def addrocks(elements):
    rockline="ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print (rockline)
    elements.insert(0,"")
    for i in range(1,len(elements)):
        if i==1 or i==2:
            print(fillstring(elements[i],5), end="")
        elif i<=9:
            print(fillstring(elements[i],10), end="")
        elif i<=10:#
            print()
            print(fillstring(elements[i],10), end="")
        elif i<=16:
            print(fillstring(elements[i],10), end="")
        elif i<=17:
            print()
            print(fillstring("",5), end="")
        elif i<=18:
            print(fillstring("",5), end ="")
            print(fillstring(elements[i],10), end="")
        elif i<=24:
            print(fillstring("",10), end="")
        elif i<=25:
            print()
            print(fillstring("",5), end="")
        elif(i<=26):
            print(fillstring("",5), end ="")
            print(fillstring(elements[i],10), end="")
        elif(i<=32):
            print(fillstring(elements[i],10), end="")		
    print()


def addmulti():
    multiline="MULTI----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(multiline)    
    print(fillstring(NK.get(),5), end="")
    print(fillstring(NEQ.get(), 5), end="")
    print(fillstring(NPH.get(), 5), end="")
    print(fillstring(NB.get(), 5), end="")
    print(fillstring(NKIN.get(), 5), end="")
    print()


def addparam():
    paramline="PARAM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(paramline)    
    print(fillstring(NOITE.get(),2), end="")
    print(fillstring(KDATA.get(),2), end="")
    print(fillstring(MCYC.get(),4), end="")
    print(fillstring(MSEC.get(),4), end="")
    print(fillstring(MCYPR.get(),4 ), end="")
    print(fillstring(MOPII124.get(),24), end="")
    print(fillstring("",10), end="")
    print(fillstring(TEXP.get(), 10), end="")
    print(fillstring(BE.get(), 10), end="")
    print(fillstring("",10), end="")
    print()
    print(fillstring(TSTART.get(), 10), end="")
    print(fillstring(TIMAX.get(), 10), end="")
    print(fillstring(DELTENORNDLT.get(), 10), end="")
    print(fillstring(DELTMX.get(), 10), end="")
    print(fillstring(ELST.get(), 5), end="")
    print(fillstring("", 5), end="")
    print(fillstring(GF.get(),10), end="")
    print(fillstring(REDLT.get(), 10), end="")
    print(fillstring(SCALE.get(), 10), end="")
    print()
    separate(DLTI.get(),10)
    print()
    print(fillstring(RE1.get(), 10), end="")
    print(fillstring(RE2.get(), 10), end="")
    print(fillstring(U.get(), 10), end="")
    print(fillstring(WUP.get(), 10), end="")
    print(fillstring(WNR.get(), 10), end="")
    print(fillstring(DFAC.get(), 10), end="")
    print()
    print(fillstring(DEP1.get(), 20), end="")
    print(fillstring(DEP2.get(), 20), end="")
    print(fillstring(DEP3.get(), 20), end="")
    print(fillstring(DEP4.get(), 20), end="")
    print()
  

def addsolvr():
    solvrline="SOLVR----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(solvrline) 
    print(fillstring(MATSLV.get(),1), end="")
    print(fillstring("",2), end="")
    print(fillstring(ZPROCS.get(),2), end="")
    print(fillstring("",3), end="")
    print(fillstring(OPROCS.get(),2), end="")
    print(fillstring(RITMAX.get(),10), end="")
    print(fillstring(CLOSUR.get(),10), end="")
    print()


def addrpcap(elements):
    rpcapline="RPCAP----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print (rpcapline)
    if(len(elements)<17):
        return
    elements.insert(0,"")
    
    print (fillstring(elements[17],5),end="")
    print(fillstring("",5), end ="")
    print (fillstring(elements[18],10),end="")
    print (fillstring(elements[19],10),end="")
    print (fillstring(elements[20],10),end="")
    print (fillstring(elements[21],10),end="")
    print (fillstring(elements[22],10),end="")
    print (fillstring(elements[23],10),end="")
    print (fillstring(elements[24],10),end="")
    print()
    print (fillstring(elements[25],5),end="")
    print(fillstring("",5), end ="")
    print (fillstring(elements[26],10),end="")
    print (fillstring(elements[27],10),end="")
    print (fillstring(elements[28],10),end="")
    print (fillstring(elements[29],10),end="")
    print (fillstring(elements[30],10),end="")
    print (fillstring(elements[31],10),end="")
    print (fillstring(elements[32],10),end="")
    print()
'''  
#single gener: 
def addgener2(elements):
    generline="GENER----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(generline)    
    print(fillstring(elements[0],3), end="")
    print(fillstring(elements[1],2), end="")
    print(fillstring(elements[2],3), end="")
    print(fillstring(elements[3],2), end="")
    print(fillstring(elements[4],5), end="")
    print(fillstring(elements[5],5), end="")
    print(fillstring(elements[6],5), end="")
    print(fillstring(elements[7],5), end="")
    print(fillstring("",5), end="")
    print(fillstring(elements[8],4), end="")
    print(fillstring(elements[9],1), end="")
    print(fillstring(elements[10],10), end="")
    print(fillstring(elements[11],10), end="")
    print(fillstring(elements[12],10), end="")
    print()
    separate(elements[13],10)
    print()
    separate(elements[14],10)
    print()
    separate(elements[15],10)
    print()
'''
def addindom():
    indomline="INDOM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(indomline)    
    print(fillstring(MAT1.get(),5), end="")
    print()
    separate(X.get(),20)
    print()


def addDiffu():
    diffuline="DIFFU----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(diffuline)    
    separate(FDDIAGI1.get(),10)
    separate(FDDIAGI2.get(),10)
    print()

def addselec():
    selecline="SELEC----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(selecline)    
    separateselec1(IEI.get(),5)
    print()
    separate(FEI.get(),10)
    print()
    print()
  
def addTimes():
    Timesline="TIMES----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(Timesline)    
    print(fillstring(ITI.get(),5), end="")
    print(fillstring(ITE.get(),5), end="")
    print(fillstring(DELAF.get(),10), end="")
    print(fillstring(TINTER.get(),10), end="")
    print()
    separate(TISI.get(),10)
    #print TIS(1)-TIS(ITI)

    print()
    
def checkexists(examplestring):
    if (examplestring=="" or examplestring=="separate by commas"):
        return False
    return True
    
def addFOFT():
    FOFTline="FOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(FOFTline) 
    if(checkexists(EOFT1.get())):   
        print(fillstring(EOFT1.get(),5))
    if(checkexists(EOFT2.get())):
        print(fillstring(EOFT2.get(),5))
    if(checkexists(EOFT3.get())):
        print(fillstring(EOFT3.get(),5))
    if(checkexists(EOFT4.get())):
        print(fillstring(EOFT4.get(),5))
    if(checkexists(EOFT5.get())):
        print(fillstring(EOFT5.get(),5))
    if(checkexists(EOFT6.get())):
        print(fillstring(EOFT6.get(),5))
    if(checkexists(EOFT7.get())):
        print(fillstring(EOFT7.get(),5))
    if(checkexists(EOFT8.get())):
        print(fillstring(EOFT8.get(),5))
    if(checkexists(EOFT9.get())):
        curnum=0
        curstring=""
        for i in range(len(EOFT9.get())):
            if(EOFT9.get()[i]==','):
                curstring=fillstring(curstring,5)
                print(curstring)
                curstring=""
            else:
                curstring+=EOFT9.get()[i]
        print(fillstring(curstring,5))
    


def addCOFT():
    COFTline="COFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(COFTline)    
    if(checkexists(ECOFT1.get())): 
        print(fillstring(ECOFT1.get(),5))
    if(checkexists(ECOFT2.get())):
        print(fillstring(ECOFT2.get(),5))
    if(checkexists(ECOFT3.get())):
        print(fillstring(ECOFT3.get(),5))
    if(checkexists(ECOFT4.get())):
        print(fillstring(ECOFT4.get(),5))
    if(checkexists(ECOFT5.get())):
        print(fillstring(ECOFT5.get(),5))
    if(checkexists(ECOFT6.get())):
        print(fillstring(ECOFT6.get(),5))
    if(checkexists(ECOFT7.get())):
        print(fillstring(ECOFT7.get(),5))
    if(checkexists(ECOFT8.get())):
        print(fillstring(ECOFT8.get(),5))
    if(checkexists(ECOFT9.get())):
        curnum=0
        curstring=""
        for i in range(0,len(ECOFT9.get())):
            if(ECOFT9.get()[i]==','):
                curstring=fillstring(curstring,5)
                print(curstring)
                curstring=""
            else:
                curstring+=ECOFT9.get()[i]
        print(fillstring(curstring,5))
    

def addGOFT():
    GOFTline="GOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(GOFTline)    
    if(checkexists(EGOFT1.get())): 
        print(fillstring(EGOFT1.get(),5))
    if(checkexists(EGOFT2.get())):
        print(fillstring(EGOFT2.get(),5))
    if(checkexists(EGOFT3.get())):
        print(fillstring(EGOFT3.get(),5))
    if(checkexists(EGOFT4.get())):
        print(fillstring(EGOFT4.get(),5))
    if(checkexists(EGOFT5.get())):
        print(fillstring(EGOFT5.get(),5))
    if(checkexists(EGOFT6.get())):
        print(fillstring(EGOFT6.get(),5))
    if(checkexists(EGOFT7.get())):
        print(fillstring(EGOFT7.get(),5))
    if(checkexists(EGOFT8.get())):
        print(fillstring(EGOFT8.get(),5))
    if(checkexists(EGOFT9.get())):
        curnum=0
        curstring=""
        for i in range(0,len(EGOFT9.get())):
            if(EGOFT9.get()[i]==','):
                curstring=fillstring(curstring,5)
                print(curstring)
                curstring=""
            else:
                curstring+=EGOFT9.get()[i]
        print(fillstring(curstring,5))
    
    
def checkfull(listname):
  for x in range(len(listname)):
    if listname[x]!="":
        return True
  return False
#BACKEND RUNS------ONLY PLACE WHERE PRINTING SHOULD HAPPEN
#all the for loops checking if lists are empty

#print title
print(var0.get()[0:80])

for key in rockDict:
  dummy = rockDict[key]
  addrocks(dummy)

if(checkfull(multi)):
  addmulti()

if(checkfull(param)):
  addparam()
  
if(checkfull(solvr)):
  addsolvr()
  
for key in rockDict:
  dummy = rockDict[key]
  addrpcap(dummy)

#GENER

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
  

#print ending line
print("ENDCY----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8")
#PROGRAM OVER---------------------