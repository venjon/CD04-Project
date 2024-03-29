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

def diffuclick():
    global diffuCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    diffuCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#c5ffff")
    #rightPanels.append(diffuCanvas)
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
        diffu = []
        diffu = [FDDIAGI1.get(),FDDIAGI2.get()]
        print(diffu)
    global savediffu
    savediffu = tk.Button(diffuCanvas,text="Save BEFORE Switching Page", command=diffuSave, bg="#00ff00")
    savediffu.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="DIFFU", command=diffuclick).place(x=10,y=170)

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
 
def addDiffu():
    diffuline="DIFFU----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(diffuline)    
    separate(FDDIAGI1.get(),10)
    separate(FDDIAGI2.get(),10)
    print()

addDiffu()