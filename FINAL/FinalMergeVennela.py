#This is the final merge of all programs
#RUN TO LAUNCH FINAL APP 
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
root = tk.Tk()
#FRONTEND 


#THARUKA EDITS

root.mainloop()

#BACKEND MAIN FUNCTIONS++++++++++++++++++++++++++++
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
#BACKEND INDIVIDUAL FUNCTIONS++++++++++++++++++++++++++++
#VENNELA EDITS

def addrocks(elements):
    rockline="ROCKS----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print (rockline)
    for i in range(1,len(elements)):
        if i==1 or i==2:
            print(fillstring(elements[i],5), end="")
        elif i<=9:
            print(fillstring(elements[i],10), end="")
        elif i<=10:#
            print()
            print(fillstring(elements[i],10), end="")
        elif i<=16:
            print(fillstring(elements[i],10), end="")
        elif i<=17:
            print()
            print(fillstring("",5), end="")
        elif i<=18:
            print(fillstring("",5), end ="")
            print(fillstring(elements[i],10), end="")
        elif i<=24:
            print(fillstring("",10), end="")
        elif i<=25:
            print()
            print(fillstring("",5), end="")
        elif(i<=26):
            print(fillstring("",5), end ="")
            print(fillstring(elements[i],10), end="")
        elif(i<=32):
            print(fillstring(elements[i],10), end="")		
    print()


def addmulti():
    multiline="MULTI----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(multiline)    
    print(fillstring(NK.get(),5), end="")
    print(fillstring(NEQ.get(), 5), end="")
    print(fillstring(NPH.get(), 5), end="")
    print(fillstring(NB.get(), 5), end="")
    print(fillstring(NKIN.get(), 5), end="")
    print()


def addparam():
    paramline="PARAM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(paramline)    
    print(fillstring(NOITE.get(),2), end="")
    print(fillstring(KDATA.get(),2), end="")
    print(fillstring(MCYC.get(),4), end="")
    print(fillstring(MSEC.get(),4), end="")
    print(fillstring(MCYPR.get(),4 ), end="")
    print(fillstring(MOPII124.get(),24), end="")
    print(fillstring("",10), end="")
    print(fillstring(TEXP.get(), 10), end="")
    print(fillstring(BE.get(), 10), end="")
    print(fillstring("",10), end="")
    print()
    print(fillstring(TSTART.get(), 10), end="")
    print(fillstring(TIMAX.get(), 10), end="")
    print(fillstring(DELTENORNDLT.get(), 10), end="")
    print(fillstring(DELTMX.get(), 10), end="")
    print(fillstring(ELST.get(), 5), end="")
    print(fillstring("", 5), end="")
    print(fillstring(GF.get(),10), end="")
    print(fillstring(REDLT.get(), 10), end="")
    print(fillstring(SCALE.get(), 10), end="")
    print()
    separate(DLTI.get(),10)
    print()
    print(fillstring(RE1.get(), 10), end="")
    print(fillstring(RE2.get(), 10), end="")
    print(fillstring(U.get(), 10), end="")
    print(fillstring(WUP.get(), 10), end="")
    print(fillstring(WNR.get(), 10), end="")
    print(fillstring(DFAC.get(), 10), end="")
    print()
    print(fillstring(DEP1.get(), 20), end="")
    print(fillstring(DEP2.get(), 20), end="")
    print(fillstring(DEP3.get(), 20), end="")
    print(fillstring(DEP4.get(), 20), end="")
    print()
  

def addsolvr():
    solvrline="SOLVR----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(solvrline) 
    print(fillstring(MATSLV.get(),1), end="")
    print(fillstring("",2), end="")
    print(fillstring(ZPROCS.get(),2), end="")
    print(fillstring("",3), end="")
    print(fillstring(OPROCS.get(),2), end="")
    print(fillstring(RITMAX.get(),10), end="")
    print(fillstring(CLOSUR.get(),10), end="")
    print()


def addrpcap(elements):
    rpcapline="RPCAP----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print (rpcapline)
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
      
#single gener: 
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

def addindom():
    indomline="INDOM----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(indomline)    
    print(fillstring(MATindom.get(),5), end="")
    print()
    separate(X.get(),20)
    print()


def addDiffu():
    diffuline="DIFFU----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(diffuline)    
    separate(FDDIAGI1.get(),10)
    separate(FDDIAGI2.get(),10)
    print()

def addselec():
    selecline="SELEC----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(selecline)    
    separateselec1(IEI.get(),5)
    print()
    separate(FEI.get(),10)
    print()
    print()
  
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
    
def addFOFT():
    FOFTline="FOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(FOFTline)    
    print(fillstring(EOFT.get(),5), end="")
    print()


def addCOFT():
    COFTline="COFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(COFTline)    
    print(fillstring(ECOFT.get(),10), end="")
    print()

def addGOFT():
    GOFTline="GOFT-----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8"
    print(GOFTline)    
    print(fillstring(EGOFT.get(),5), end="")
    print()

#BACKEND RUNS------ONLY PLACE WHERE PRINTING SHOULD HAPPEN
#all the for loops checking if lists are empty

#print title
print(var0.get())

#print ending line
print("ENDCY----1----*----2----*----3----*----4----*----5----*----6----*----7----*----8")
#PROGRAM OVER---------------------