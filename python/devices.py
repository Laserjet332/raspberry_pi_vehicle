import RPi.GPIO as GPIO
import time


class DistanceSensor():
    def __init__(self,echo: int,trigger: int) -> None:
        self.echo = echo
        GPIO.setup(echo,GPIO.IN)
        self.trigger = trigger
        GPIO.setup(trigger,GPIO.OUT)
    
    def check_distance(self):
        GPIO.output(self.trigger,GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger,GPIO.LOW)
        while GPIO.input(self.echo) == 0:
            start = time.perf_counter()
        while GPIO.input(self.echo) == 1:
            end = time.perf_counter()
        t = end-start
        return 17150*t
        

class Motor():
    def __init__(self,output1: int,output2: int,enable: int,speed: int) -> None:
        self.output1 = output1
        GPIO.setup(self.output1,GPIO.OUT,initial=GPIO.LOW)
        
        self.output2 = output2
        GPIO.setup(self.output2,GPIO.OUT,initial=GPIO.LOW)
        
        GPIO.setup(enable,GPIO.OUT)
        self.enable = GPIO.PWM(enable,100)
        self.enable.start(speed)       
        self.speed = speed
    
    def forward(self) -> None:
        GPIO.output(self.output1,GPIO.HIGH)
        GPIO.output(self.output2,GPIO.LOW)
    
    def backward(self) -> None:
        GPIO.output(self.output1,GPIO.LOW)
        GPIO.output(self.output2,GPIO.HIGH)
    
    def stop(self) -> None:
        GPIO.output(self.output1,GPIO.LOW)
        GPIO.output(self.output2,GPIO.LOW)
    
    def change_speed(self,speed: int) -> None:
        if speed > 100:
            speed = 100
        elif speed < 0:
            speed = 0
        self.speed = speed
        self.enable.ChangeDutyCycle(self.speed)


class Robot():
    def __init__(self,output1: int,output2: int,enable1: int,output3: int,output4: int,enable2: int) -> None:
        self.motor_left = Motor(output1 ,output2,enable1,80)
        self.motor_right = Motor(output3,output4,enable2,80)
        self.moving_forward = False
        self.moving_backward = False
        self.turning_left = False
        self.turning_right = False
        self.speed = 80
        self.distance_sensors = []
    
    def forward(self):
        if not self.moving_backward:
            self.moving_forward = True
            self.motor_left.forward()
            self.motor_right.forward()
            
        elif self.turning_right:
            self.moving_forward = True
            self.motor_left.forward()
            self.motor_left.change_speed(self.speed-60)
            self.motor_right.change_speed(self.speed+20)
            
        elif self.turning_left:
            self.moving_forward = True
            self.motor_right.forward()
            self.motor_right.change_speed(self.speed-60)
            self.motor_left.change_speed(self.speed+20)
    
    def backward(self):
        if not self.moving_forward:
            self.moving_backward = True
            self.motor_left.backward()
            self.motor_right.backward()
    
    def stop(self):
        if self.moving_forward:
            self.moving_forward = False
            if self.turning_right:
                self.right()
            elif self.turning_left:
                self.left()
            else:
                self.motor_left.stop()
                self.motor_right.stop()
                self.motor_left.change_speed(self.speed)
                self.motor_right.change_speed(self.speed)
        elif self.moving_backward:
            self.moving_backward = False
            self.motor_left.stop()
            self.motor_right.stop()
            self.motor_left.change_speed(self.speed)
            self.motor_right.change_speed(self.speed)
    
    def right(self):
        if not self.moving_forward and not self.moving_backward and not self.turning_left:
            self.motor_right.forward()
            self.motor_left.backward()
            self.turning_right = True
        elif self.turning_left:
            pass
        else:
            self.motor_left.change_speed(self.speed-60)
            self.motor_right.change_speed(self.speed+20)
            self.turning_right = True
    
    def stop_right(self):
        if self.moving_forward:
            self.motor_left.change_speed(self.speed)
            self.motor_right.change_speed(self.speed)
            self.turning_right = False
        else:
            self.motor_right.stop()
            self.motor_left.stop()
            self.motor_left.change_speed(self.speed)
            self.motor_right.change_speed(self.speed)
            self.turning_right = False
    
    def left(self):
        if not self.moving_forward and not self.moving_backward and not self.turning_right:
            self.motor_right.backward()
            self.motor_left.forward()
            self.turning_left = True
        elif self.turning_right:
            pass
        else:
            self.motor_right.change_speed(self.speed-60)
            self.motor_left.change_speed(self.speed+20)
            self.turning_left = True
    
    def stop_left(self):
        if self.moving_forward:
            self.motor_right.change_speed(self.speed)
            self.motor_left.change_speed(self.speed)
            self.turning_left = False
        else:
            self.motor_right.stop()
            self.motor_left.stop()
            self.motor_left.change_speed(self.speed)
            self.motor_right.change_speed(self.speed)
            self.turning_left = False
    
    def change_speed(self,speed):
        self.speed = speed
        self.motor_left.change_speed(self.speed)
        self.motor_right.change_speed(self.speed)
    
    def add_distance_sensor(self,echo: int,trigger: int) -> None:
        sensor = DistanceSensor(echo,trigger)
        self.distance_sensors.append(sensor)
    
    def check_distance_sensors(self):
        sensors_readings = []
        for sensor in self.distance_sensors:
            sensors_readings.append(sensor.check_distance())
        return sensors_readings