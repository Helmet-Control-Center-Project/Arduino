# 메인 소스
import FSR_402
import HC_SR04
import time

while True:
    distance = HC_SR04.distance() #착용센서의 값을 저장
    LEFT = FSR_402.cha0()
    RIGHT = FSR_402.cha1() #충격센서의 값을 저장

    HC_SR04.distance_result() #착용센서의 값을 서버로 전송
    if distance < 6: #착용중인 상태
        if LEFT or RIGHT > 0: 
            FSR_402.cha_result() #충격센서의 값을 서버로 전송
            print("--------------------------")
            print("착용 중")
            print("LEFT : ",LEFT, "RIGHT : ",RIGHT)
            print("total : ", LEFT+RIGHT)
        else: #착용중이며 충격이 발생하지 않은 상태
            print("--------------------------")
            print("착용 중")
            print("충격이 감지되지 않았음")
    else: #착용중이 아닌 상태
        print("--------------------------")
        print("착용 아님")