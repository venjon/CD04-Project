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

def coftclick():
    global coftCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    coftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#c0c0c0")
    #rightPanels.append(coftCanvas)
    coftCanvas.pack()
    #ECOFT
    tk.Label(coftCanvas,bg="#c0c0c0",text="Connection Name (pair of element names) - ECOFT").grid(column=0,row=1)
    global ECOFT
    ECOFT = tk.StringVar()
    tk.Entry(coftCanvas,textvariable=ECOFT).grid(column=1,row=1)
    #SAVE
    def coftSave():
        coft = []
        coft = [ECOFT.get()]
        print(coft)
    global savecoft
    savecoft = tk.Button(coftCanvas,text="Save BEFORE Switching Page", command=coftSave, bg="#00ff00")
    savecoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="COFT", command=coftclick).place(x=10,y=450)

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
#BACKEND FUNCTIONS++++++++++++++++++++++++++++

def addCOFT():
    COFTline="COFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(COFTline)    
    print(fillstring(ECOFT.get(),10), end="")
    print()

#print variables
addCOFT()