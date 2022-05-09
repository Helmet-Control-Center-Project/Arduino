import spidev
import time
import requests, json
import posturl 

Vcc = 5.0
R1 = 1000
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Calculate fsr402 registor value
def fsr420_Registor(voltage):
    R = (R1 * Vcc)/voltage - R1
    return R
 
def ReadChannel(channel):
    adc = spi.xfer([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def cha0():
    # delay = 0.03
    # f = open('fsr402-2.dat', 'w') 
    index = 0
    analog_level = ReadChannel(0)
    Vout = analog_level * Vcc / 1024.0
    if(Vout < 2.2):
        Vout = 0.001
        Rfsr = 5000000
        analog_level = 0
    else:
        Rfsr = fsr420_Registor(Vout)
        # print("0_Digital:", analog_level, " Voltage:", Vout, " R(K Ohm):", Rfsr / 1000.0)
        # data = "{} {} {} {}\n".format(index, analog_level, Vout, Rfsr / 1000.0)
        # f.write(data)
        # time.sleep(delay)
        index += 1
    return analog_level

def cha1():
    # delay = 0.03
    # f = open('fsr402-2.dat', 'w') 
    index = 0
    analog_level = ReadChannel(1)
    Vout = analog_level * Vcc / 1024.0
    if(Vout < 2.2):
        Vout = 0.001
        Rfsr = 5000000
        analog_level = 0
    else:
        Rfsr = fsr420_Registor(Vout)
        # print("1_Digital:", analog_level, " Voltage:", Vout, " R(K Ohm):", Rfsr / 1000.0)
        # data = "{} {} {} {}\n".format(index, analog_level, Vout, Rfsr / 1000.0)
        # f.write(data)
        # time.sleep(delay)
        index += 1
    return analog_level

def cha_result(): #센서의 값을 post통신으로 서버에 전송하는 모듈
    Left_result = cha0() 
    Right_result = cha1()
    data = json.dumps({
            'helmetId' : 'H0001',
            'shockDataLeft' : Left_result,
            'shockDataRight' : Right_result
            })
    header = {'Content-type' : 'application/json'}
    res = requests.post(posturl.shock(), data=data, headers=header) #해당 API의 서버로 데이터를 전송

if __name__ == '__main__':
    while True :
        a = cha0()
        b = cha1()
        if a or b > 0:
            print("a : ",a, "b : ",b)
            print("total : ", a+b)
            cha_result()
        time.sleep(0.03)
   