from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib as plt
import csv

array, plot_t, plot_other = [], [], []
with open('pmw_log.csv', mode='r') as log:
    logreader = csv.reader(log, delimiter=',')
    for row in logreader:
        #print(row)
        array.append(row)

for i in range(len(array)):
    plot_t.append(array[i][1])
    plot_other.append(array[i][2])

print(plot_t, "\n", plot_other)