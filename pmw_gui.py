from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import csv

buffer, plot_t, plot_y, gyro, acc = [], [], [], [], []
with open('pmw_log.csv', mode='r') as log:
    logreader = csv.reader(log, delimiter=',')
    for row in logreader:
        #print(row)
        buffer.append(row)

for i in range(len(buffer)):
    plot_t.append(buffer[i][1]) #get time
    gyro.append(buffer[i][2:5]) #get gyro data
    acc.append(buffer[i][5:8])  #get accelerometer data

plot_random = np.random.normal(20, 5, len(plot_t))
gyro = np.array(gyro)
plot_t = np.array(plot_t)
gyro = gyro.astype(float)

plt.plot(plot_t, gyro)
plt.xlabel('Time')
plt.ylabel('Angle from origin')
plt.show()