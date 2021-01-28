#raspberry piをつかってロボット制御をするときの雛形
from pandas.io.parsers import read_csv
import RPi.GPIO as GPIO
import time 

 

def GPIOSetup(fileName):
    df = read_csv(fileName)
    Number_list = len(fileName)

    for i in range(Number_list):
        name = df.iloc[i][UsePlace]
        pwm =  df.iloc[i][PWMpin]
        dire = df.iloc[i][Directionpin]

        GPIO.setup(pwm,GPIO.OUT)
        GPIO.setup(dire,GPIO.OUT)
        GPIO.PWM(pwm,100)
        GPIO.output(dire,True)

        print( "Finish " + name + "/setup " + "PWM:" + str(pwm) + " Direction:" + str(dire))


        
