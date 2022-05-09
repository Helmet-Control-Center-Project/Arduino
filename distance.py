#거리감지 센서 GP2Y0D805Z0F / 호환성 문제로 해당 센서 폐기
import shock_detection
from email import header
import requests, json
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
time.sleep(1)

def distance(): #센서의 값을 반환하는 모듈
    wearing = GPIO.input(17)
    return wearing

def distance_result(): #센서의 값을 post통신으로 서버에 전송하는 모듈
    wearing = GPIO.input(17) #보내는 데이터 : HelmetID와 센서 값(wearing)
    data = json.dumps({
            'helmetId' : 'H0001',
            'wearing' : wearing
            })
    header = {'Content-type' : 'application/json'}
    res = requests.post('http://125.177.137.35:8080/api/shocksensor', data=data, headers=header) #해당 API의 서버로 데이터를 전송
    return wearing

if __name__ == '__main__': #distance.py가 단독으로 실행될때 실행
    while True :
        if distance() == 0:
            print("--------------------------")
            print("착용 중")
            print(distance())
            print("충격센서 값 : ", shock_detection.shock()) #shock_detection의 shock 모듈
            time.sleep(1)
        else:
            print("--------------------------")
            print("착용 아님")
            time.sleep(1)