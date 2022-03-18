# -*- coding: utf-8 -*-
import shock_detection
from email import header
import requests, json
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
time.sleep(1)

def distance():
    wearing = GPIO.input(24)
    return wearing

def distance_result():
    wearing = GPIO.input(24)
    data = json.dumps({
            'helmetId' : 'H0001',
            'wearing' : wearing
            })
    header = {'Content-type' : 'application/json'}
    res = requests.post('http://125.177.137.35:8080/api/shocksensor', data=data, headers=header)
    return wearing

if __name__ == '__main__':
    while True :
        wearing = GPIO.input(24)
        if wearing == 0:
            print("--------------------------")
            print("착용 중")
            print("충격센서 값 : ", shock_detection.shock())
            time.sleep(1)
        else:
            print("--------------------------")
            print("착용 아님")
            time.sleep(1)