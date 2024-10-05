import tkinter as tk
import RPi.GPIO as GPIO
from devices import Robot

GPIO.setmode(GPIO.BCM)
OUTPUT1 = 14  
OUTPUT2 = 15
ENABLE1 = 18
OUTPUT3 = 3
OUTPUT4 = 2
ENABLE2 = 4
FONT = ("Ariel",20,"normal")

class Interface:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Robot')
        
        self.up = tk.Button(self.window,text="↑",font=FONT,width=2)
        self.up.grid(row=0,column=1,padx=2,pady=2)
        
        self.down = tk.Button(self.window,text="↓",font=FONT,width=2)
        self.down.grid(row=1,column=1,padx=2,pady=2)
        
        self.left = tk.Button(self.window,text="←",font=FONT,width=2)
        self.left.grid(row=1,column=0,padx=2,pady=2)
        
        self.right = tk.Button(self.window,text="→",font=FONT,width=2)
        self.right.grid(row=1,column=2,padx=2,pady=2)
        
        self.window.grid_columnconfigure((0, 1), weight=1)
        self.window.resizable(False,False)

interface = Interface()
robot = Robot(OUTPUT1,OUTPUT2,ENABLE1,OUTPUT3,OUTPUT4,ENABLE2)

def go_forward(event):
    interface.up.config(relief="sunken")
    robot.forward()
        
def stop_forward(event):
    interface.up.config(relief="raised")
    robot.stop()

interface.window.bind("<KeyPress-w>",go_forward)
interface.window.bind("<KeyRelease-w>",stop_forward)


def go_backward(event):
    interface.down.config(relief="sunken")
    robot.backward()

def stop_backward(event):
    interface.down.config(relief="raised")
    robot.stop()

interface.window.bind("<KeyPress-s>",go_backward)
interface.window.bind("<KeyRelease-s>",stop_backward)


def go_right(event):
    interface.right.config(relief="sunken")
    robot.right()

def stop_right(event):
    interface.right.config(relief="raised")
    robot.stop_right()

interface.window.bind("<KeyPress-d>",go_right)
interface.window.bind("<KeyRelease-d>",stop_right)


def go_left(event):
    interface.left.config(relief="sunken")
    robot.left()

def stop_left(event):
    interface.left.config(relief="raised")
    robot.stop_left()

interface.window.bind("<KeyPress-a>",go_left)
interface.window.bind("<KeyRelease-a>",stop_left)

interface.window.mainloop()
GPIO.cleanup()