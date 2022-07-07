import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800, bg="#f0f0f0")
canvas.pack()

#Name of Sample
a = tk.Label(root, text="Name of Sample (5 characters)")
canvas.create_window(300, 100, window=a)

rockName = tk.Entry(root)
canvas.create_window(500,100,window=rockName)

def rockNameCheck():
    rockNameLetters = list(rockName)
    if len(rockNameLetters) != 5:
        tk.messagebox.showerror(message="Sample name must be 5 letters long!")
        

root.mainloop()