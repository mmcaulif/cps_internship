import serial, time, struct

start = time.time()
ser = serial.Serial("com5",115200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,0,False,False,False,2)

print("Waking up board on " + ser.port + "...")
time.sleep(2)

print("Arming...")
checksum = 0
total_data = ['$'.encode('utf-8'), 'M'.encode('utf-8'), '<'.encode('utf-8'), 16, 200] + [220, 5, 220, 5, 232, 3, 220, 5, 0, 0, 0, 0, 0, 0, 0, 0]
for i in struct.pack('<2B' + '16B', *total_data[3:len(total_data)]):
    checksum = checksum ^ i
total_data.append(checksum)
print(total_data)
b = ser.write(struct.pack('<3c2B' + '16B' + 'B', *total_data))

print("Waiting 3 secs")
time.sleep(3)

print("Disarming...")
checksum = 0
total_data = ['$'.encode('utf-8'), 'M'.encode('utf-8'), '<'.encode('utf-8'), 16, 200] + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in struct.pack('<2B' + '16B', *total_data[3:len(total_data)]):
    checksum = checksum ^ i
total_data.append(checksum)
print(total_data)
b = ser.write(struct.pack('<3c2B' + '16B' + 'B', *total_data))




