from ui import Interface
from devices import Motor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
OUTPUT1 = 14  
OUTPUT2 = 15
ENABLE1 = 18
OUTPUT3 = 2
OUTPUT4 = 3
ENABLE2 = 4

def update_value_motor1(event):
    motor1.change_speed(interface.slider1.get())

def update_value_motor2(event):
    motor2.change_speed(interface.slider2.get())
    

interface = Interface()
interface.slider1.bind("<ButtonRelease-1>",update_value_motor1)
interface.slider2.bind("<ButtonRelease-1>",update_value_motor2)

motor1 = Motor(OUTPUT1,OUTPUT2,ENABLE1)
motor2 = Motor(OUTPUT3,OUTPUT4,ENABLE2)

interface.window.mainloop()