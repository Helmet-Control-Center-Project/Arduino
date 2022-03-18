# -*- coding: utf-8 -*-

from email import header
import RPi.GPIO as GPIO
import time
import requests, json

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
time.sleep(1)

def shock():
	result = GPIO.input(23)
	return result

def shock_result():
	result = GPIO.input(23)
	data = json.dumps({
			'helmetId' : 'H0001',
			'result' : result
			})
	header = {'Content-type' : 'application/json'}

	res = requests.post('http://125.177.137.35:8080/api/shocksensor', data=data, headers=header )
	return result


if __name__ == '__main__':
	while True:
		result = GPIO.input(23)
		if  result == 1:
			print("진동이 감지 되었습니다.")
			time.sleep(0.05)
		
		else:
			print("진동이 없습니다.")
			time.sleep(0.05)	
		