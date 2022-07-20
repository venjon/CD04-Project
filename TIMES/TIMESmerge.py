from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import messagebox,messagebox
from tkinter import ttk
import os
import tkinter
root = tk.Tk()
lcanvas = tk.Canvas(root, width=340, height=800, bg="#f0f0f0")
lcanvas.pack(side="left")
rcanvas = tk.Canvas(root, width=460, height=800, bg="white",)
rcanvas.pack(side="right")

def timesclick():
    global timesCanvas
    #for x in range():
        #rightPanels[x].pack_forget()
    timesCanvas = tk.Canvas(rcanvas,width=460,height=800,bg="#e9d1ff")
    #rightPanels.append(timesCanvas)
    timesCanvas.pack()
    #ITI
    tk.Label(timesCanvas,text="Number of Times Provided on Records - ITI",bg="#e9d1ff").grid(column=0,row=1)
    global ITI
    ITI = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=ITI).grid(column=1,row=1)
    #ITE
    tk.Label(timesCanvas,text="Desired Number of Times - ITE",bg="#e9d1ff").grid(column=0,row=2)
    global ITE
    ITE= tk.StringVar()
    tk.Entry(timesCanvas,textvariable=ITE).grid(column=1,row=2)
    #DELAF
    tk.Label(timesCanvas,text="Max Time Step After Prescribed Times are Reached - DELAF",bg="#e9d1ff").grid(column=0,row=3)
    global DELAF
    DELAF = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=DELAF).grid(column=1,row=3)
    #TINTER
    tk.Label(timesCanvas,text="Time Increment for Times w/ Index ITI to ITE- TINTER",bg="#e9d1ff").grid(column=0,row=4)
    global TINTER
    TINTER = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=TINTER).grid(column=1,row=4)
    #TISI
    tk.Label(timesCanvas,text="List of Times at Which Printout is Desired (separate by commas) - TIS(I) - 1 to ITI",bg="#e9d1ff").grid(column=0,row=5)
    global TISI
    TISI = tk.StringVar()
    tk.Entry(timesCanvas,textvariable=TISI).grid(column=1,row=5)
    #SAVE
    def timesSave():
        times = []
        times = [ITI.get(),ITE.get(),DELAF.get(),TINTER.get(),TISI.get()]
        print(times)
    global savetimes
    savetimes = tk.Button(timesCanvas,text="Save BEFORE Switching Page", command=timesSave, bg="#00ff00")
    savetimes.grid(column=0,row=0,columnspan=2)
tk.Button(lcanvas, text="TIMES", command=timesclick).place(x=10,y=370)

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
def addTimes():
    Timesline="TIMES----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(Timesline)    
    print(fillstring(ITI.get(),5), end="")
    print(fillstring(ITE.get(),5), end="")
    print(fillstring(DELAF.get(),10), end="")
    print(fillstring(TINTER.get(),10), end="")
    print()
    separate(TISI.get(),10)
    #print TIS(1)-TIS(ITI)

    print()

#print variables
addTimes()

