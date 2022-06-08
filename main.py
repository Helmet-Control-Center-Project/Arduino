# 메인 소스
import RPi.GPIO as GPIO
from email import header
import requests, json
import FSR_402
import HC_SR04
import GPS
import posturl
import Emergency

button = 20
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

while True:
    distance = HC_SR04.distance()
    Left = FSR_402.cha0()
    Right = FSR_402.cha1()
    Center = FSR_402.cha2()
    Back = FSR_402.cha3()
    Front = FSR_402.cha4()
    inputIO = GPIO.input(button)
    
    GPS.GPS_result()
    HC_SR04.distance_result()
    
    if inputIO == False:
        Emergency.SOS()

    else :
        if Center or Left or Right or Front or Back > 0:
            FSR_402.cha_result()
            print("Distance => ", distance, "cm")
            print("Center : ",Center, ",Left : ",Left, ",Right : ",Right, ",Front : ",Front, ",Back : ",Back)
            print("total : ", Center+Left+Right+Front+Back)
