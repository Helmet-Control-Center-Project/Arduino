# 메인 소스
import shock_detection
import HC_SR04
import time

while True:
    distance = HC_SR04.distance() #착용센서의 값을 저장
    shock = shock_detection.shock() #충격센서의 값을 저장

    HC_SR04.distance_result() #착용센서의 값을 서버로 전송
    if distance < 6: #착용중인 상태
        if shock == 1: #착용중이며 충격이 발생한 상태
            shock_detection.shock_result() #충격센서의 값을 서버로 전송
            print("--------------------------")
            print("착용 중")
            print("Distance => ", distance, "cm")
            print("충격 감지")
        else: #충격중이며 충격이 발생하지 않은 상태
            shock_detection.shock_result() #충격센서의 값을 서버로 전송
            print("--------------------------")
            print("착용 중")
            print("Distance => ", distance, "cm")
            print("충격이 감지되지 않았음")
    else: #착용중이 아닌 상태
        print("--------------------------")
        print("착용 아님")
        print("착용상태 아님")

    time.sleep(1)