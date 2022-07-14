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

#TITLE
titleLabel = tk.Label(lcanvas, text="Document Title (max 80 characters):").place(x=10, y=10)
title = tk.StringVar()
titleEntry = tk.Entry(lcanvas, textvariable=title)
titleEntry.place(x=207,y=10)
test = title.get()
print(test)
root.mainloop()
#print(var0.get())