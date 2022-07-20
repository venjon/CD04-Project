#This is the final merge of all programs
#RUN TO LAUNCH FINAL APP 
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
root = tk.Tk()
#FRONTEND 
#ROCKS------------------------------------------------------

#MULTI------------------------------------------------------

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

#BACKEND RUNS------ONLY PLACE WHERE PRINTING SHOULD HAPPEN
#all the for loops checking if lists are empty
