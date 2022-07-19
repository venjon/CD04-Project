#import statements
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
#create root
root = tk.Tk()
#create two canvases
lcanvas = tk.Canvas(root, width=400, height=800, bg="#f0f0f0")
lcanvas.pack(side="left")
rcanvas = tk.Canvas(root, width=400, height=800, bg="white",)
rcanvas.pack(side="right")

#Left-Side Menus ========================================================================
titleLabel = tk.Label(lcanvas, text="Document Title (max 80 char):").place(x=10, y=10)
var0 = tk.StringVar()
titleEntry = tk.Entry(lcanvas, textvariable=var0)
titleEntry.place(x=207,y=10)
#TITLE VARIABLE:
TITLE = var0.get()



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


#add ROCKS dropdown ========================================================================
var1 = tk.StringVar()
var1.set("Materials")
rockoptions = ["Add Material"]
rockoptionscanvas = ["placeholder"]
#rockList = tk.OptionMenu(lcanvas, var1, *(rockoptions), command = RocksOptionMenu_SelectionEvent)
rockDict = {}
#rockList.place(x=10,y=50)


#done with root!
root.mainloop()