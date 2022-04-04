#충격 감지 센서 SW-420
from email import header
import RPi.GPIO as GPIO
import time
import requests, json
import posturl

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)

def shock(): #센서의 값을 반환하는 모듈
	result = GPIO.input(23)
	return result

def shock_result(): #센서의 값을 post통신으로 서버에 전송하는 모듈
	result = GPIO.input(23)
	data = json.dumps({ #보내는 데이터 : HelmetID와 센서 값(result)
			'helmetId' : 'H0001', 
			'result' : result
			})
	header = {'Content-type' : 'application/json'}

	res = requests.post(posturl.shock(), data=data, headers=header ) #posturl의 shock 모듈이 나타내는 서버로 데이터 전송
	return result


if __name__ == '__main__': #shock_detection.py가 단독으로 실행될때 실행
	while True:
		result = GPIO.input(23)
		if  result == 1:
			print("진동이 감지 되었습니다.")
			time.sleep(0.05)
		
		else:
			print("진동이 없습니다.")
			time.sleep(0.05)	
		