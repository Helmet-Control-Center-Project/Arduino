import shock_detection
import distance
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
time.sleep(1)


while True:
    wearing = distance.distance()
    shock = shock_detection.shock()

    distance.distance_result()
    if wearing == 0:
        if shock == 1:
            shock_detection.shock_result()
            print("충격이 감지")
        else:
            shock_detection.shock_result()
            print("충격이 감지되지 않았음")
    else:
        print("착용상태 아님")

    time.sleep(1)