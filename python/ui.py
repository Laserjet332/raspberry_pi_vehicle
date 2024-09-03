import tkinter as tk
from tkinter import ttk


class Interface:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Motors Control')
        
        self.label1 = tk.Label(self.window,text="Motor 1")
        self.label1.grid(row=0,column=0,padx=10,pady=10) 
        
        self.value1 = tk.IntVar()
        self.slider1 = tk.Scale(self.window,
                                from_=100,
                                to=0,
                                orient="vertical",
                                variable=self.value1)
        self.slider1.grid(row=1,column=0,padx=50,pady=20)
        
        self.value2 = tk.IntVar()
        self.slider2 = tk.Scale(self.window,
                                from_=100,
                                to=0,
                                orient="vertical",
                                variable=self.value2)
        self.slider2.grid(row=1,column=1,padx=50,pady=20)
        
        self.label2 = tk.Label(self.window,text="Motor 2")
        self.label2.grid(row=0,column=1,padx=10,pady=10) 
        
        self.window.grid_columnconfigure((0, 1), weight=1)
        self.window.resizable(False,False)
    
    def get_slider1_value(self):
        return self.value_1
    
    def get_slider2_value(self):
        return self.value_2
        