from pymultiwii import MultiWii
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

inittime = time.time()
plot_x, plot_y1, plot_y2 = [], [], []
serialPort = "com3"
board = MultiWii(serialPort)
assert board != 1, "There's something wrong with the serial connection... check the logfile!"

fig, (p1, p2) = plt.subplots(2)

for i in range(100):
    try:
        telemetry = board.getData(MultiWii.RAW_IMU)  #a = accelerometer, g = gyroscope
        #attitude = board.getData(MultiWii.ATTITUDE)
        gyro = [telemetry['ax'], telemetry['ay'], telemetry['az']]
        acc = [telemetry['gx'], telemetry['gy'], telemetry['gz']]
    except:
        print("Packet error; defaulting to prev value")


    print("Gyro:",gyro,"Accelerometer:",acc)
    t = time.time() - inittime
    plot_x.append(t)
    plot_y1.append(gyro)
    plot_y2.append(acc)
    p1.plot(plot_x, plot_y1)
    p1.set(title='Gyroscope data')
    p2.plot(plot_x, plot_y2)
    p2.set(title='Accelerometer data')
    plt.pause(0.25)
    time.sleep(0.05)

    """print("Gyro:",gyro,"Accelerometer:",acc)
    t = time.time() - inittime
    plot_x.append(t)
    plot_y2.append(acc)
    plt.plot(plot_x, plot_y2)
    plt.cla()
    plt.pause(0.25)"""

plt.show()

with open('pmw_log.csv', mode='w') as log:
    logwriter = csv.writer(log)
    for i in range(len(plot_x)):
        logwriter.writerow([i, plot_x[i], plot_y1[i]])