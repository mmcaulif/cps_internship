import serial, time, struct

ser = serial.Serial("com7",115200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,0,False,False,False,2)

#print('\U0001F642')
#print(b'$M<\x00ff'.decode("utf-8"))

b = ser.write('$M<\x00ff'.encode('utf-8'))
#b = ser.write(b'$M<\x00ff')
print("Bytes written: ",b)

while True:
    try:
        header = 0
        header = ser.read().decode('utf-8')
    except:
        print("error")

    if header == '$':
        header = header + ser.read(2).decode('utf-8')
        break

datalength = struct.unpack('<b', ser.read())[0]
print("Datalength:", datalength)
code = struct.unpack('<b', ser.read())
data = ser.read(datalength)

ser.flushInput()
ser.flushOutput()

print(data, type(data))
temp = struct.unpack('<' + 'h' * int(datalength / 2), data)
print(temp)
print(list(temp)[:6])