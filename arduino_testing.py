import serial
import time
ser = serial.Serial(port='COM9', baudrate=115200, timeout=.1)
def write_read(x):
    ser.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = ser.readline()
    return data

while True:
    num = input("Enter a string: ") # Taking input from user
    value = write_read(num)
    print(value.decode('utf-8')) #decode removes the b'_'