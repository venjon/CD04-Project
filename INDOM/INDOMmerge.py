from difflib import Match
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

def indomclick():
    global indomCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    indomCanvas = tk.Canvas(rcanvas,width=400,height=800,bg="#ffdfa5")
    #rightPanels.append(indomCanvas)
    indomCanvas.pack()
    #MAT
    tk.Label(indomCanvas,text="Material Name(s) - MAT",bg="#ffdfa5").grid(column=0,row=1)
    global MATindom
    MATindom= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=MATindom).grid(column=1,row=1)
    #X
    tk.Label(indomCanvas,text="Primary Variables; quantity depends on EOS (separate by commas) - X",bg="#ffdfa5").grid(column=0,row=2)
    global X
    X= tk.StringVar()
    tk.Entry(indomCanvas,textvariable=X).grid(column=1,row=2)
    #SAVE
    def indomSave():
        indom = []
        indom = [MATindom.get(),X.get()]
        print(indom)
    global saveindom
    saveindom = tk.Button(indomCanvas,text="Save BEFORE Switching Page", command=indomSave, bg="#00ff00")
    saveindom.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="INDOM", command=indomclick).place(x=10,y=250)

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
			if(curnum%4==0):
				print()
			curstring=""
		else:
			curstring+=bigline[i]
	print(fillstring(curstring,full_len))
	curnum+=1
	if(curnum*8==0):
		print()
 
#BACKEND FUNCTIONS++++++++++++++++++++++++++++
 
def addindom():
    indomline="INDOM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(indomline)    
    print(fillstring(MATindom.get(),5), end="")
    print()
    separate(X.get(),20)
    print()

#print variables
addindom()