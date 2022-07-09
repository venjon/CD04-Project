import tkinter as tk
from tkinter import BOTH, Y, filedialog, Text, messagebox
import os
from tkinter.ttk import PanedWindow
root = tk.Tk()
lcanvas = tk.Canvas(root, width=400, height=800, bg="#f0f0f0")
lcanvas.pack(side="left")
rcanvas = tk.Canvas(root, width=400, height=800, bg="white",)
rcanvas.pack(side="right")

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
        print("good")
        addMaterial()
    else:
        print("bad")
    pass

def addMaterial():
    print("hello world")
    newMat = tk.Toplevel(root)
    newMat.geometry("200x100")
    tk.Label(newMat,text="""Enter a name for your new sample
    (preferably 5 characters)""").pack()
    newMatName0 = tk.StringVar()
    newMatName = tk.Entry(newMat, width=30, textvariable=newMatName0).pack()
    options.append(newMatName0.get())
    def var3():
        print("hello world")
        rockList.set('')
    var2=tk.Button(newMat, text="Enter", command=lambda:var3())
    var2.pack()
    tk.Label(lcanvas, text=options).pack()

var1 = tk.StringVar()
var1.set("Materials")
options = ["Add Material"]
rockList = tk.OptionMenu(lcanvas, var1, *(options), command = RocksOptionMenu_SelectionEvent).place(x=10, y=50)


root.mainloop()