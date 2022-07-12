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

#Right-Side Menus
#ROCKS
def createRockRight():
    #MAT
    tk.Label(rockoptionscanvas[-1],text="Name of Material - MAT").grid(column=0,row=0)
    mat = tk.Label(rockoptionscanvas[-1],text=rockoptions[-1], bg="white")
    mat.grid(column=1,row=0)
    #NAD
    tk.Label(rockoptionscanvas[-1],text="- NAD").grid(column=0,row=1)
    nad = tk.StringVar()
    tk.Entry(rockoptionscanvas[-1],textvariable=nad).grid(column=1,row=1)
    #DROK
    tk.Label(rockoptionscanvas[-1],text="Rock Grain Density (kg/m^3)- DROK").grid(column=0,row=2)
    drok = tk.StringVar()
    tk.Entry(rockoptionscanvas[-1],textvariable=drok).grid(column=1,row=2)

#Left-Side Menus
#TITLE
titleLabel = tk.Label(lcanvas, text="Document Title (max 80 characters):").place(x=10, y=10)
var0 = tk.StringVar()
titleEntry = tk.Entry(lcanvas, textvariable=var0)
titleEntry.place(x=207,y=10)
title = titleEntry.get()

#ROCKS
def RocksOptionMenu_SelectionEvent(event):
    RockChoice = var1.get()
    if RockChoice == "Add Material":
        addMaterial()
    else:
        for x in range(1, len(rockoptionscanvas)):
            rockoptionscanvas[x].pack_forget()
        rockoptionscanvas[rockoptions.index(RockChoice)].pack()
    pass

def addMaterial():
    newMat = tk.Toplevel(root)
    newMat.geometry("200x100")
    tk.Label(newMat,text="""Enter a name for your new sample
    (preferably 5 characters)
    DO NOT INCLUDE SPACES""").pack()
    global newMatName
    newMatName = tk.StringVar()
    tk.Entry(newMat, width=30, textvariable=newMatName).pack()
    def var3():
        rockoptions.append(newMatName.get())
        newMat.destroy()
        rockList = tk.OptionMenu(lcanvas, var1, *(rockoptions), command = RocksOptionMenu_SelectionEvent).place(x=10,y=50)
        newrockscanvas = tk.Canvas(rcanvas, width=400, height=800, bg="#c1e2fe")
        rockoptionscanvas.append(newrockscanvas)
        createRockRight()
    tk.Button(newMat, text="Enter", command=lambda:var3()).pack()

var1 = tk.StringVar()
var1.set("Materials")
rockoptions = ["Add Material"]
rockoptionscanvas = ["placeholder"]
rockList = tk.OptionMenu(lcanvas, var1, *(rockoptions), command = RocksOptionMenu_SelectionEvent)
rockList.place(x=10,y=50)

#MULTI

root.mainloop()