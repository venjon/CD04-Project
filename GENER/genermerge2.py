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

#GENER
def GenerOptionMenu_SelectionEvent(event):
    global GenerChoice
    GenerChoice = var1.get()
    if GenerChoice == "Add Generator":
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
            generoptions.append(newMatName.get())
            newMat.destroy()
            generList = tk.OptionMenu(lcanvas, var1, *(generoptions), command = GenerOptionMenu_SelectionEvent).place(x=10,y=50)
            newgenercanvas = tk.Canvas(rcanvas, width=460, height=800, bg="#c1e2fe")
            generoptionscanvas.append(newgenercanvas)
            generDict[generoptions[rc]] = []
            #EL
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text=" - EL").grid(column=0,row=1)
            global EL
            EL = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=EL).grid(column=1,row=1)
            #NE
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text=" - NE").grid(column=0,row=2)
            global NE
            NE = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=NE).grid(column=1,row=2)
            #SL
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Gener Grain Density (kg/m^3) - SL").grid(column=0,row=3)
            global SL
            SL = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=SL).grid(column=1,row=3)
            #NS
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Porosity (if not included in INCON) - NS").grid(column=0,row=4)
            global NS
            NS = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=NS).grid(column=1,row=4)
            #PER(1)
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Absolute Permeability Along Principal Axis 1 - PER(1)").grid(column=0,row=5)
            global NSEQ
            NSEQ = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=NSEQ).grid(column=1,row=5)
            #PER(2)
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Absolute Permeability Along Principal Axis 2 - PER(2)").grid(column=0,row=6)
            global NADD
            NADD = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=NADD).grid(column=1,row=6)
            #PER(3)
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Absolute Permeability Along Principal Axis 3 - PER(3)").grid(column=0,row=7)
            global NADS
            NADS = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=NADS).grid(column=1,row=7)
            #LTAB
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Formation Heat Conductivity in Liquid (W/m°C)- LTAB").grid(column=0,row=8)
            global LTAB
            LTAB = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=LTAB).grid(column=1,row=8)
            #TYPE
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Gener Grain Specific Heat (J/kg°C) - TYPE").grid(column=0,row=9)
            global TYPE
            TYPE = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=TYPE).grid(column=1,row=9)
            #ITAB
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Pore Compressibility - ITAB").grid(column=0,row=10)
            global ITAB
            ITAB = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=ITAB).grid(column=1,row=10)
            #GX
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Pore Expansivity - GX").grid(column=0,row=11)
            global GX
            GX = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=GX).grid(column=1,row=11)
            #EX
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Formation Heat Conductivity w/o Liquid (W/m°C) - EX").grid(column=0,row=12)
            global EX
            EX = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=EX).grid(column=1,row=12)
            #HG
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Tortuosity Factor - HG").grid(column=0,row=13)
            global HG
            HG = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=HG).grid(column=1,row=13)
            #F1
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Klinkenberg Parameter B [k*(1+b/P)] - F1").grid(column=0,row=14)
            global F1
            F1 = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=F1).grid(column=1,row=14)
            #F2
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Distribution Coefficient of Parent Radionuclide - F2").grid(column=0,row=15)
            global F2
            F2 = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=F2).grid(column=1,row=15)
            #F3
            tk.Label(generoptionscanvas[rc],bg="#c1e2fe",text="Distribution Coefficient of Daughter Radionuclide - F3").grid(column=0,row=16)
            global F3
            F3 = tk.StringVar()
            tk.Entry(generoptionscanvas[rc],textvariable=F3).grid(column=1,row=16)
            #SAVE
            def generSave():
                generDict[generoptions[rc]] = []
                generDict[generoptions[rc]] = [EL,NE.get(),SL.get(), NS.get(), NSEQ.get(), NADD.get(), NADS.get(), LTAB.get(), TYPE.get(), ITAB.get(), GX.get(), EX.get(), HG.get(), F1.get(), F2.get(), F3.get()]
                print(generDict)
            global savegener
            savegener = tk.Button(generoptionscanvas[rc],text="Save BEFORE Switching Page", command=generSave, bg="#00ff00")
            savegener.grid(column=0,row=0,columnspan=2)
        tk.Button(newMat, text="Enter", command=lambda:var3()).pack()
    else:
        rc = generoptions.index(GenerChoice)
        for x in range(1, len(generoptionscanvas)):
            generoptionscanvas[x].pack_forget()
        savegener.grid_forget()
        def generSave2():
            print(rc)
            generDict[generoptions[rc]] = [EL.get(),NE.get(),SL.get(), NS.get(), NSEQ.get(), NADD.get(), NADS.get(), LTAB.get(), TYPE.get(), ITAB.get(), GX.get(), EX.get(), HG.get(), F1.get(), F2.get(), F3.get()]
            print(generDict)
        savegener.config(command=generSave2)
        savegener.grid(column=0,row=0,columnspan=2)
        generoptionscanvas[rc].pack()
        print(rc)

var1 = tk.StringVar()
var1.set("Generators")
generoptions = ["Add Generator"]
generoptionscanvas = ["placeholder"]
generList = tk.OptionMenu(lcanvas, var1, *(generoptions), command = GenerOptionMenu_SelectionEvent)
generDict = {}
generList.place(x=10,y=50)

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
 
#backend RUN
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


#print(generline)
for key in generDict:
  dummy = generDict[key]
  addgener2(dummy)
