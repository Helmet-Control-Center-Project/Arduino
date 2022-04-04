# from sys import stdin

def API(): #API.txt의 각 열을 lines배열에 입력하는 모듈 / lines[0] = IP, lines[1] = Port
    file_path = "/home/ubuntu/Arduino/API.txt" 
    with open(file_path) as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return lines
            
def shock(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 충격센서
    lines = API()
    shock_URL ='http://' + lines[0] + ':' + lines[1] + '/api/shocksensor'
    return shock_URL

def wearing(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 거리센서
    lines = API()
    wearing_URL ='http://' + lines[0] + ':' + lines[1] + '/api/wearing'
    return wearing_URL

def sos(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 버튼
    lines = API()
    sos_URL ='http://' + lines[0] + ':' + lines[1] + '/api/sos'
    return sos_URL

def sosC(): #API.txt 수정을 통해 서버 API를 변경하는 모듈 - 버튼
    lines = API()
    sosC_URL ='http://' + lines[0] + ':' + lines[1] + '/api/sos/cancel'
    return sosC_URL

# def IP_change():
#     print("변경할 IP주소 입력 :")
#     file_path = "/home/ubuntu/Arduino/API.txt"
#     with open(file_path,'r') as f:
#         lines=f.readlines()
#     with open(file_path, 'w') as f:
#         for i,line in enumerate(lines,1):
#             if i==1:
#                 f.write(input()+"\n")
#             else :
#                 f.write(line)

# def PORT_change():
    # print("변경할 PORT번호 입력 :")
    # file_path = "/home/ubuntu/Arduino/API.txt"
    # with open(file_path,'r') as f:
    #     lines=f.readlines()
    # with open(file_path, 'w') as f:
    #     for i,line in enumerate(lines,1):
    #         if i==2:
    #             f.write(input())
    #         else :
    #             f.write(line)

# # def start():
#     while True:
#         os.system('clear')
#         print("POST통신\n")
#         print("현재 서버 : ", API())
#         print("서버 변경 = 1, 시작 = 2 : ")
#         answer = int(stdin.readline())
#         os.system('clear')
#         if answer == 1:
#             while True:
#                 print("변경할 부분을 선택하여 주세요.\n")
#                 print("IP변경 = 1, PORT변경 = 2, 전체변경 = 3, 취소 = 4 : ")
#                 answer2 = int(stdin.readline())
#                 os.system('clear')
#                 if answer2 == 1:
#                     IP_change()
#                     break
#                 elif answer2 == 2:
#                     PORT_change()
#                     break
#                 elif answer2 == 3:
#                     IP_change()
#                     PORT_change()
#                     break
#                 elif answer2 == 4:
#                     break
#                 else :
#                     print("잘못된 입력\n")
#                     time.sleep(1)
#         elif answer == 2:
#             break
#         else :
#             print("잘못된 입력\n")
#             time.sleep(1)
#     print("통신을 시작합니다.\n")
