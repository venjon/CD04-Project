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

def foftclick():
    global foftCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    foftCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#96fff0")
    #rightPanels.append(foftCanvas)
    foftCanvas.pack()
    #EOFT
    tk.Label(foftCanvas,bg="#96fff0",text="Element Name - EOFT").grid(column=0,row=1)
    global EOFT
    EOFT = tk.StringVar()
    tk.Entry(foftCanvas,textvariable=EOFT).grid(column=1,row=1)
    #SAVE
    def foftSave():
        foft = []
        foft = [EOFT.get()]
        print(foft)
    global savefoft
    savefoft = tk.Button(foftCanvas,text="Save BEFORE Switching Page", command=foftSave, bg="#00ff00")
    savefoft.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="FOFT", command=foftclick).place(x=10,y=410)

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
def addFOFT():
    FOFTline="FOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(FOFTline)    
    print(fillstring(EOFT.get(),5), end="")
    print()

#print variables
addFOFT()

