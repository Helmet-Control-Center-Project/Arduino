# import distance
import shock_detection
import HC_SR04
import time

while True:
    distance = HC_SR04.distance()
    shock = shock_detection.shock()

    HC_SR04.distance_result()
    if distance < 6:
        if shock == 1:
            shock_detection.shock_result()
            print("--------------------------")
            print("착용 중")
            print("Distance => ", distance, "cm")
            print("충격 감지")
        else:
            shock_detection.shock_result()
            print("--------------------------")
            print("착용 중")
            print("Distance => ", distance, "cm")
            print("충격이 감지되지 않았음")
    else:
        print("--------------------------")
        print("착용 아님")
        print("착용상태 아님")

    time.sleep(1)