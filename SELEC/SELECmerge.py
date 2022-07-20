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

def selecclick():
    global selecCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    selecCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#ceae8f")
    #rightPanels.append(selecCanvas)
    selecCanvas.pack()
    #IEI
    tk.Label(selecCanvas,text="""Number of Records w/ Floating Point Numbers That Will Be Read
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
        selec = []
        selec = [IEI.get(),FEI.get()]
        print(selec)
    global saveselec
    saveselec = tk.Button(selecCanvas,text="Save BEFORE Switching Page", command=selecSave, bg="#00ff00")
    saveselec.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="SELEC", command=selecclick).place(x=10,y=330)

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
#BACKEND FUNCTIONS++++++++++++++++++++++++++++
def addselec():
    selecline="SELEC----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(selecline)    
    '''print(fillstring(IE1.get(),5), end="")
    print(fillstring(IE2.get(),5), end="")
    print(fillstring(IE3.get(),5), end="")
    print(fillstring(IE4.get(),5), end="")
    print(fillstring(IE5.get(),5), end="")
    print(fillstring(IE6.get(),5), end="")
    print(fillstring(IE7.get(),5), end="")
    print(fillstring(IE8.get(),5), end="")
    print(fillstring(IE9.get(),5), end="")
    print(fillstring(IE10.get(),5), end="")
    print(fillstring(IE11.get(),5), end="")
    print(fillstring(IE12.get(),5), end="")
    print(fillstring(IE13.get(),5), end="")
    print(fillstring(IE14.get(),5), end="")
    print(fillstring(IE15.get(),5), end="")
    print()'''
    separateselec1(IEI.get(),5)
    print()
    separate(FEI.get(),10)
    print()
    
    #PRINT FE1-FE [8*IE1]
    print()
    #WRITE SEPARATION PROGRAM
    

#print variables
addselec()