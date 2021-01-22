from test import Pwm
import RPI.GPIO as GPIO
from time import sleep
from contextlib import closing
import struct

BatuBottamLeave = {"value":0,"Index":1,"code":0}
MaruBottamLeave = {"value":0,"Index":1,"code":1}
TriangleBottamLeave = {"value":0,"Index":1,"code":2}
SquqreBottamLeave = {"value":0,"Index":1,"code":3}


ArmPWMTopR = int
ArmDirectionTopR = int

ArmPWMTopL = int
ArmDirectionTopL = int

ArmPWMBotoomR = int
ArmDirectionBotoomR = int

ArmPWMBotoomL = int
ArmDirectionBotoomL = int

MotorPWMList = [ArmPWMTopR,ArmPWMTopL,ArmPWMBotoomR,ArmPWMBotoomL]
MotorDirectionList = [ArmDirectionTopR,ArmDirectionTopL,ArmDirectionBotoomR,ArmDirectionBotoomL]

Direction = bool #Judge the direction

print("please input Rotate speed")
RotateSpeed = int(input())

GPIO.setup(MotorPWMList,GPIO.OUT)
GPIO.setup(MotorDirectionList,GPIO.OUT)
GPIO.SetWarnings(False)

GPIO.PWM(MotorPWMList,100)

GPIO.output(MotorDirectionList,Direction)

MotorPWMList.start(0)
            
def HundMove(MotorPWMName,UseBottam):
    BottanName = UseBottam
    while True:
        MotorPWMName.ChangeDutyCycle(RotateSpeed)
        if (code ==  BottanName("code") and value == BottanName["value"]):
            print("Stop")
            break
            
def ChangeDirection():
    if Direction == True:
        GPIO.output(MotorDirectionList,False)
        print("Change Direction True → False")
    
    if Direction == False:
        GPIO.output(MotorDirectionList,True)
        print("Change Direction False → True")


with open("/dev/input/js0","rb")as f:
    while True:
        a = f.read(8)
        t,value,code,index=struct.unpack("<ihbb",a)

        if index == 0 and code == 1 :
            HundMove(ArmPWMBotoomL,BatuBottamLeave)
        
        if index == 1 and code == 1 :
            HundMove(ArmPWMBotoomR,MaruBottamLeave)
        
        if index == 2 and code == 1 :
            HundMove(ArmPWMTopL,TriangleBottamLeave)

        if index == 3 and code == 1 :
            HundMove(ArmPWMTopR,SquqreBottamLeave)
        
        if index == 10:
            print("push Change Direction Bottan")
            ChangeDirection()

