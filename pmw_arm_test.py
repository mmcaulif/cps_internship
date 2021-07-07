from pymultiwii import MultiWii
import csv
import time
import numpy as np
import matplotlib.pyplot as plt

serialPort = "com7"
board = MultiWii(serialPort)
assert board != 1, "There's something wrong with the serial connection... check the logfile!"

"""data = [255,255,255,255,0,0,0,0]
att = board.sendCMDreceiveATT(15,MultiWii.SET_RAW_RC,data)
print(att)"""

board.arm()
print ("Board is armed now!")
print ("In 1/2 a second it will disarm...")
time.sleep(0.5)
board.disarm()
print ("Disarmed.")