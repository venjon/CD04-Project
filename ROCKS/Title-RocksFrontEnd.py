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

#TITLE
titleLabel = tk.Label(lcanvas, text="Document Title (max 80 characters):").place(x=10, y=10)
var0 = tk.StringVar()
titleEntry = tk.Entry(lcanvas, textvariable=var0)
titleEntry.place(x=207,y=10)
title = var0.get()

#ROCKS
def RocksOptionMenu_SelectionEvent(event):
    global RockChoice
    RockChoice = var1.get()
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
            saverock = tk.Button(rockoptionscanvas[rc],text="Save BEFORE Switching Page", command=rockSave, bg="#00ff00")
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

root.mainloop()