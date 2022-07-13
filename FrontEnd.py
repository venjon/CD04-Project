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

#Right-Side Menus
#ROCKS
def createRockRight():
    rockDict[rockoptions[rc]] = []
    #MAT
    tk.Label(rockoptionscanvas[rc],text="Name of Material - MAT").grid(column=0,row=1)
    global MAT
    MAT = (rockoptions[rc])[0:5]
    tk.Label(rockoptionscanvas[rc],text=MAT, bg="white").grid(column=1,row=1)
    #NAD
    tk.Label(rockoptionscanvas[rc],text=" - NAD").grid(column=0,row=2)
    global NAD
    NAD = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=NAD).grid(column=1,row=2)
    #DROK
    tk.Label(rockoptionscanvas[rc],text="Rock Grain Density (kg/m^3) - DROK").grid(column=0,row=3)
    global DROK
    DROK = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=DROK).grid(column=1,row=3)
    #POR
    tk.Label(rockoptionscanvas[rc],text=" - POR").grid(column=0,row=4)
    global POR
    POR = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=POR).grid(column=1,row=4)
    #PER(1)
    tk.Label(rockoptionscanvas[rc],text=" - PER(1)").grid(column=0,row=5)
    global PER1
    PER1 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=PER1).grid(column=1,row=5)
    #PER(2)
    tk.Label(rockoptionscanvas[rc],text=" - PER(2)").grid(column=0,row=6)
    global PER2
    PER2 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=PER2).grid(column=1,row=6)
    #PER(3)
    tk.Label(rockoptionscanvas[rc],text=" - PER(3)").grid(column=0,row=7)
    global PER3
    PER3 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=PER3).grid(column=1,row=7)
    #CWET
    tk.Label(rockoptionscanvas[rc],text=" - CWET").grid(column=0,row=9)
    global CWET
    CWET = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CWET).grid(column=1,row=9)
    #SPHT
    tk.Label(rockoptionscanvas[rc],text=" - SPHT").grid(column=0,row=10)
    global SPHT
    SPHT = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=SPHT).grid(column=1,row=10)
    #COM
    tk.Label(rockoptionscanvas[rc],text="COM").grid(column=0,row=11)
    global COM
    COM = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=COM).grid(column=1,row=11)
    #EXPAN
    tk.Label(rockoptionscanvas[rc],text=" - EXPAN").grid(column=0,row=12)
    global EXPAN
    EXPAN = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=EXPAN).grid(column=1,row=12)
    #CDRY
    tk.Label(rockoptionscanvas[rc],text=" - CDRY").grid(column=0,row=13)
    global CDRY
    CDRY = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CDRY).grid(column=1,row=13)
    #TORTX
    tk.Label(rockoptionscanvas[rc],text=" - TORTX").grid(column=0,row=14)
    global TORTX
    TORTX = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=TORTX).grid(column=1,row=14)
    #GK
    tk.Label(rockoptionscanvas[rc],text=" - GK").grid(column=0,row=15)
    global GK
    GK = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=GK).grid(column=1,row=15)
    #XKD3
    tk.Label(rockoptionscanvas[rc],text=" - XKD3").grid(column=0,row=16)
    global XKD3
    XKD3 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=XKD3).grid(column=1,row=16)
    #XKD4
    tk.Label(rockoptionscanvas[rc],text=" - XKD4").grid(column=0,row=17)
    global XKD4
    XKD4 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=XKD4).grid(column=1,row=17)
    #IRP
    tk.Label(rockoptionscanvas[rc],text=" - IRP").grid(column=0,row=18)
    global IRP
    IRP = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=IRP).grid(column=1,row=18)
    #RP(1)
    tk.Label(rockoptionscanvas[rc],text=" - RP(1)").grid(column=0,row=19)
    global RP1
    RP1 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=RP1).grid(column=1,row=19)
    #RP(2)
    tk.Label(rockoptionscanvas[rc],text=" - RP(2)").grid(column=0,row=20)
    global RP2
    RP2 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=RP2).grid(column=1,row=20)
    #RP(3)
    tk.Label(rockoptionscanvas[rc],text=" - RP(3)").grid(column=0,row=21)
    global RP3
    RP3 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=RP3).grid(column=1,row=21)
    #RP(4)
    tk.Label(rockoptionscanvas[rc],text=" - RP(4)").grid(column=0,row=22)
    global RP4
    RP4 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=RP4).grid(column=1,row=22)
    #RP(5)
    tk.Label(rockoptionscanvas[rc],text=" - RP(5)").grid(column=0,row=23)
    global RP5
    RP5 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=RP5).grid(column=1,row=23)
    #RP(6)
    tk.Label(rockoptionscanvas[rc],text=" - RP(6)").grid(column=0,row=24)
    global RP6
    RP6 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=RP6).grid(column=1,row=24)
    #RP(7)
    tk.Label(rockoptionscanvas[rc],text=" - RP(7)").grid(column=0,row=25)
    global RP7
    RP7 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=RP7).grid(column=1,row=25)
    #ICP
    tk.Label(rockoptionscanvas[rc],text=" - ICP").grid(column=0,row=26)
    global ICP
    ICP = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=ICP).grid(column=1,row=26)
    #CP(1)
    tk.Label(rockoptionscanvas[rc],text=" - CP(1)").grid(column=0,row=27)
    global CP1
    CP1 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP1).grid(column=1,row=27)
    #CP(2)
    tk.Label(rockoptionscanvas[rc],text=" - CP(2)").grid(column=0,row=28)
    global CP2
    CP2 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP2).grid(column=1,row=28)
    #CP(3)
    tk.Label(rockoptionscanvas[rc],text=" - CP(3)").grid(column=0,row=28)
    global CP3
    CP3 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP3).grid(column=1,row=28)
    #CP(4)
    tk.Label(rockoptionscanvas[rc],text=" - CP(4)").grid(column=0,row=29)
    global CP4
    CP4 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP4).grid(column=1,row=29)
    #CP(5)
    tk.Label(rockoptionscanvas[rc],text=" - CP(5)").grid(column=0,row=30)
    global CP5
    CP5 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP5).grid(column=1,row=30)
    #CP(6)
    tk.Label(rockoptionscanvas[rc],text=" - CP(6)").grid(column=0,row=31)
    global CP6
    CP6 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP6).grid(column=1,row=31)
    #CP(7)
    tk.Label(rockoptionscanvas[rc],text=" - CP(7)").grid(column=0,row=32)
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

rightPanels = []

#Left-Side Menus
#TITLE
titleLabel = tk.Label(lcanvas, text="Document Title (max 80 characters):").place(x=10, y=10)
var0 = tk.StringVar()
titleEntry = tk.Entry(lcanvas, textvariable=var0)
titleEntry.place(x=207,y=10)
title = titleEntry.get()

#ROCKS
def RocksOptionMenu_SelectionEvent(event):
    global RockChoice
    RockChoice = var1.get()
    if RockChoice == "Add Material":
        global rc
        rc=-1
        addMaterial()
    else:
        for x in range(1, len(rockoptionscanvas)):
            rockoptionscanvas[x].pack_forget()
        rockoptionscanvas[rockoptions.index(RockChoice)].pack()
        rc = rockoptions.index(RockChoice)
        print(rc)
    pass

def addMaterial():
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
        newrockscanvas = tk.Canvas(rcanvas, width=400, height=800, bg="#c1e2fe")
        rockoptionscanvas.append(newrockscanvas)
        rightPanels.append(newrockscanvas)
        createRockRight()
    tk.Button(newMat, text="Enter", command=lambda:var3()).pack()

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
    for x in range():
        rightPanels[x].pack_forget()
    multiCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#b1fbbd")
    rightPanels.append(multiCanvas)
    multiCanvas.pack()
    #NK
    tk.Label(multiCanvas,text=" - NK").grid(column=0,row=1)
    global NK
    NK = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NK).grid(column=1,row=1)
    #NEQ
    tk.Label(multiCanvas,text=" - NEQ").grid(column=0,row=2)
    global NEQ
    NEQ= tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NEQ).grid(column=1,row=2)
    #NPH
    tk.Label(multiCanvas,text=" - NPH").grid(column=0,row=3)
    global NPH
    NPH = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NPH).grid(column=1,row=3)
    #NB
    tk.Label(multiCanvas,text=" - NB").grid(column=0,row=4)
    global NB
    NB = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NB).grid(column=1,row=4)
    #NKIN
    tk.Label(multiCanvas,text=" - NKIN").grid(column=0,row=5)
    global NKIN
    NKIN = tk.StringVar()
    tk.Entry(multiCanvas,textvariable=NKIN).grid(column=1,row=5)
    #SAVE
    def multiSave():
        multi = []
        multi = [NK.get(),NEQ.get(),NPH.get(),NB.get(),NKIN.get()]
        print(multi)
    global savemulti
    savemulti = tk.Button(multiCanvas,text="Save BEFORE Switching Page", command=multiSave, bg="#00ff00")
    savemulti.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="MULTI", command=multiclick).place(x=10,y=90)

#PARAM
def paramclick():
    global paramCanvas
    for x in range():
        rightPanels[x].pack_forget()
    paramCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#ffffc5")
    rightPanels.append(paramCanvas)
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
        param = [NOITE.get(),KDATA.get(),MCYC.get(),MESC.get(),MCYPR.get(),MOPII124.get(),TXP.get(),BE.get(),TSTART.get(),TIMAX.get(),DELTENORNDLT.get(),DELTMX.get(),ELST.get(),GF.get(),REDLT.get(),SCALE.get()]
        print(param)
    global saveparam
    saveparam = tk.Button(paramCanvas,text="Save BEFORE Switching Page", command=paramSave, bg="#00ff00")
    saveparam.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="PARAM", command=paramclick).place(x=10,y=130)

root.mainloop()