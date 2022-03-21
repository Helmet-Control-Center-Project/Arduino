import RPi.GPIO as GPIO
from email import header
import requests, json
import time
import posturl

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

def distance():
    GPIO.output(17, False)
    time.sleep(0.5)

    GPIO.output(17, True)
    time.sleep(0.00001)
    GPIO.output(17, False)
   
    while GPIO.input(18) == 0:
        start = time.time()
       
    while GPIO.input(18) == 1:
        stop = time.time()
       
    time_interval = stop - start
    distance = time_interval * 17000
    distance = round(distance, 2)
    return distance

def distance_result():
    distance_result = distance()
    data = json.dumps({
            'helmetId' : 'H0001',
            'distance' : distance_result
            })
    header = {'Content-type' : 'application/json'}
    res = requests.post(posturl.shock(), data=data, headers=header)
    return distance_result


if __name__ == '__main__':

    while True:
        print("Distance => ", distance(), "cm")