import serial, time, struct

start = time.time()
ser = serial.Serial("com7",115200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,0,False,False,False,2)
cmd = 102
checksum = 0

while True:

    total_data = ['$'.encode('utf-8'), 'M'.encode('utf-8'), '<'.encode('utf-8'), 0, cmd] + []
    for i in struct.pack('<2B' + '', *total_data[3:len(total_data)]):
        checksum = 0
        checksum = checksum ^ i
    total_data.append(checksum)
    try:
        b = None
        b = ser.write(struct.pack('<3c2B' + '' + 'B', *total_data))
    except Exception as error:
        print("\n\nError in sendCMD.")
        print("(" + str(error) + ")\n\n")
        pass

    while True:
        try:
            header = 0
            header = ser.read().decode('utf-8').strip()
        except:
            print("error")

        if header == '$':
            header = header + ser.read(2).decode('utf-8')
            break


    datalength = struct.unpack('<b', ser.read())[0]
    code = struct.unpack('<b', ser.read())
    data = ser.read(datalength)

    ser.flushInput()
    ser.flushOutput()
    elapsed = time.time() - start

    temp = struct.unpack('<' + 'h' * int(datalength / 2), data)

    ax = float(temp[0])
    ay = float(temp[1])
    az = float(temp[2])
    gx = float(temp[3])
    gy = float(temp[4])
    gz = float(temp[5])
    mx = float(temp[6])
    my = float(temp[7])
    mz = float(temp[8])

    telemetry = [ax,ay,az,gx,gy,gz,mx,my,mz]

    print("Acc:", telemetry[:3], "| Gyro:", telemetry[3:6])

    time.sleep(1)


