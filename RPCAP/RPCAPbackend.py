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
    tk.Label(rockoptionscanvas[rc],text=" - CP(3)").grid(column=0,row=29)
    global CP3
    CP3 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP3).grid(column=1,row=29)
    #CP(4)
    tk.Label(rockoptionscanvas[rc],text=" - CP(4)").grid(column=0,row=30)
    global CP4
    CP4 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP4).grid(column=1,row=30)
    #CP(5)
    tk.Label(rockoptionscanvas[rc],text=" - CP(5)").grid(column=0,row=31)
    global CP5
    CP5 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP5).grid(column=1,row=31)
    #CP(6)
    tk.Label(rockoptionscanvas[rc],text=" - CP(6)").grid(column=0,row=32)
    global CP6
    CP6 = tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP6).grid(column=1,row=32)
    #CP(7)
    tk.Label(rockoptionscanvas[rc],text=" - CP(7)").grid(column=0,row=33)
    global CP7
    CP7= tk.StringVar()
    tk.Entry(rockoptionscanvas[rc],textvariable=CP7).grid(column=1,row=33)
    #SAVE
    def rockSave():
        rockDict[rockoptions[rc]] = [TITLE, MAT,NAD.get(),DROK.get(), POR.get(), PER1.get(), PER2.get(), PER3.get(), CWET.get(), SPHT.get(), COM.get(), EXPAN.get(), CDRY.get(), TORTX.get(), GK.get(), XKD3.get(), XKD4.get(), IRP.get(), RP1.get(), RP2.get(), RP3.get(), RP4.get(), RP5.get(), RP6.get(), RP7.get(), ICP.get(), CP1.get(), CP2.get(), CP3.get(), CP4.get(), CP5.get(), CP6.get(), CP7.get()]
        print(rockDict)
    global saverock
    saverock = tk.Button(rockoptionscanvas[rc],text="Save BEFORE Switching Page", command=rockSave, bg="#00ff00")
    saverock.grid(column=0,row=0,columnspan=2)

#Left-Side Menus
#TITLE
titleLabel = tk.Label(lcanvas, text="Document Title (max 80 characters):").place(x=10, y=10)
var0 = tk.StringVar()
titleEntry = tk.Entry(lcanvas, textvariable=var0)
titleEntry.place(x=207,y=10)
TITLE = var0.get()

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

root.mainloop()


#BACKEND FUNCTIONS++++++++++++++++++++++++++++
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
 
#BACKEND FUNCTIONS++++++++++++++++++++++++++++


def addrpcap(elements):
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
        
rpcapline="RPCAP----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
print (rpcapline)      
for key in rockDict:
  dummy = rockDict[key]
  addrpcap(dummy)
  break
