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
        print("bad")
    pass

def addMaterial():
    newMat = tk.Toplevel(root)
    newMat.geometry("200x100")
    tk.Label(newMat,text="""Enter a name for your new sample
    (preferably 5 characters)
    DO NOT INCLUDE SPACES""").pack()
    newMatName = tk.StringVar()
    tk.Entry(newMat, width=30, textvariable=newMatName).pack()
    def var3():
        global options
        options.append(newMatName.get())
        newMat.destroy()
        rockList = tk.OptionMenu(lcanvas, var1, *(options), command = RocksOptionMenu_SelectionEvent).place(x=10,y=50)
    tk.Button(newMat, text="Enter", command=lambda:var3()).pack()

var1 = tk.StringVar()
var1.set("Materials")
options = ["Add Material"]
rockList = tk.OptionMenu(lcanvas, var1, *(options), command = RocksOptionMenu_SelectionEvent)
rockList.place(x=10,y=50)

#MULTI

root.mainloop()