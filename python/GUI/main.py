from ui import Interface
from devices import Robot
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
OUTPUT1 = 14  
OUTPUT2 = 15
ENABLE1 = 18
OUTPUT3 = 3
OUTPUT4 = 2
ENABLE2 = 4


interface = Interface()
robot = Robot(OUTPUT1,OUTPUT2,ENABLE1,OUTPUT3,OUTPUT4,ENABLE2)

def go_forward(event):
    if not interface.up_pressed:
        interface.up_pressed = True
        interface.up.config(relief="sunken")
        robot.forward()
        
def stop_forward(event):
    interface.up_pressed = False
    interface.up.config(relief="raised")
    robot.stop()

interface.window.bind("<KeyPress-w>",go_forward)
interface.window.bind("<KeyRelease-w>",stop_forward)


def go_backward(event):
    if not interface.down_pressed:
        interface.down_pressed = True
        interface.down.config(relief="sunken")
        robot.backward()

def stop_backward(event):
    interface.down_pressed = False
    interface.down.config(relief="raised")
    robot.stop()

interface.window.bind("<KeyPress-s>",go_backward)
interface.window.bind("<KeyRelease-s>",stop_backward)


def go_right(event):
    if not interface.right_pressed:
        interface.right_pressed = True
        interface.right.config(relief="sunken")
        robot.right()

def stop_right(event):
    interface.right_pressed = False
    interface.right.config(relief="raised")
    robot.stop_right()

interface.window.bind("<KeyPress-d>",go_right)
interface.window.bind("<KeyRelease-d>",stop_right)


def go_left(event):
    if not interface.left_pressed:
        interface.left_pressed = True
        interface.left.config(relief="sunken")
        robot.left()

def stop_left(event):
    interface.left_pressed = False
    interface.left.config(relief="raised")
    robot.stop_left()

interface.window.bind("<KeyPress-a>",go_left)
interface.window.bind("<KeyRelease-a>",stop_left)

interface.window.mainloop()
GPIO.cleanup()