import serial, time

ser = serial.Serial("com7",115200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,0,False,False,False,2)

BASIC = "\x24\x4d\x3c\x00"
MSP_IDT = BASIC + "\x64\x64"
MSP_STATUS = BASIC + "\x63\x63"
MSP_RAW_IMU = BASIC + "\x66\x66"
MSP_SERVO = BASIC + "\x67\x67"
MSP_MOTOR = BASIC + "\x68\x68"
MSP_RC = BASIC + "\x69\x69"
MSP_RAW_GPS = BASIC + "\x70\x70"
MSP_COMP_GPS = BASIC + "\x71\x71"
MSP_ATTITUDE = BASIC + "\x72\x72"
MSP_ALTITUDE = BASIC + "\x73\x73"
MSP_BAT = BASIC + "\x74\x74"

MSP_STATUS = '\x24\x4d\x3c\x00' + '\x63\x63'

#print(MSP_STATUS)

CURRENT = MSP_STATUS

print(ser.isOpen())

if ser.isOpen():
    time.sleep(3)
    print("Serial port is open at " + ser.portstr)

    ser.flushInput()
    ser.flushOutput()

    CURRENT = b'$M<'
    print(CURRENT)
    ser.write(CURRENT)

    #print("Writing to " + ser.portstr + " " + CURRENT)
    time.sleep(0.5)
    numOfLines = 0
    while True:
        response = ser.read()
        # print(type(response))

        print(ser.read().encode("hex"))
        numOfLines = numOfLines + 1

        if (numOfLines >= 1):
            break
    ser.close()

else:
    print("Cannot open serial port")