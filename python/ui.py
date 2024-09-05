import tkinter as tk
from tkinter import ttk

FONT = ("Ariel",20,"normal")

class Interface:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Robot')
        
        self.up = tk.Button(self.window,text="↑",font=FONT,width=2)
        self.up.grid(row=0,column=1,padx=2,pady=2)
        self.up_pressed = False
        
        self.down = tk.Button(self.window,text="↓",font=FONT,width=2)
        self.down.grid(row=1,column=1,padx=2,pady=2)
        self.down_pressed = False
        
        self.left = tk.Button(self.window,text="←",font=FONT,width=2)
        self.left.grid(row=1,column=0,padx=2,pady=2)
        self.left_pressed = False
        
        self.right = tk.Button(self.window,text="→",font=FONT,width=2)
        self.right.grid(row=1,column=2,padx=2,pady=2)
        self.right_pressed = False
        
        self.window.grid_columnconfigure((0, 1), weight=1)
        self.window.resizable(False,False)
        