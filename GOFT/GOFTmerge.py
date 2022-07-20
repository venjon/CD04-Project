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

def goftclick():
    global goftCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    goftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ffec85")
    #rightPanels.append(goftCanvas)
    goftCanvas.pack()
    #EGOFT
    tk.Label(goftCanvas,bg="#ffec85",text="Element that has Sink/Source Defined - EGOFT").grid(column=0,row=1)
    global EGOFT
    EGOFT = tk.StringVar()
    tk.Entry(goftCanvas,textvariable=EGOFT).grid(column=1,row=1)
    #SAVE
    def goftSave():
        goft = []
        goft = [EGOFT.get()]
        print(goft)
    global savegoft
    savegoft = tk.Button(goftCanvas,text="Save BEFORE Switching Page", command=goftSave, bg="#00ff00")
    savegoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="GOFT", command=goftclick).place(x=10,y=490)

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
	print(fillstring(curstring,full_len))
	curnum+=1
	if(curnum*8==0):
		print()
 
#BACKEND FUNCTIONS++++++++++++++++++++++++++++
def addGOFT():
    GOFTline="GOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(GOFTline)    
    print(fillstring(EGOFT.get(),5), end="")
    print()

#print variables
addGOFT()