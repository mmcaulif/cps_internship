import serial, struct, time

#ser = serial.Serial("com7",115200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,0,False,False,False,2)
ser = serial.Serial(port='COM7', baudrate=115200, timeout=.1)
#print(ser)

"""x = input("Pinging arduino with a string: ")
print(type(x))"""

print("Pinging arduino with a string...")
time.sleep(2)
ser.write('$M<\x00ff'.encode('utf-8'))
time.sleep(0.05)
p = ser.readline()
print("Ping:", p)  # decode removes the b'_'
ser.flushInput()
ser.flushOutput()

while True:
    """str = '$M<\x00ff'
    print(bytes(str, 'utf-8'))
    ser.write(str.encode('utf-8'))
    #ser.write(bytes(str, 'utf-8'))
    time.sleep(0.05)"""

    data = ser.readline(18)
    #print(data)
    #print("Data:", data)  # decode removes the b'_'
    ser.flushInput()
    ser.flushOutput()

    if data.decode('utf-8') != '':
        processed_data = struct.unpack('<' + 'h' * int(18 / 2), data)[2:]
        print("Incoming: ", processed_data)

    else:
        print('Listening...')

    time.sleep(1)