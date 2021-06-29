#! /usr/bin/env python3
from os import system
from serial import Serial
import time
from WiiProxy import MultiWii, Commands, Priority

serial = Serial("com5", 115200)
time.sleep(6)
Commands.seed()
fc = MultiWii(serial)

def arm():
    command = Commands.SET_RAW_RC
    values = (0, 0, 2000, 1000, 0, 0, 0, 0)
    start = time.time()
    elapsed = 0
    while elapsed < 0.5:
        fc.execute(command, values)
        time.sleep(0.05)
        elapsed = time.time() - start

def disarm():
    command = Commands.SET_RAW_RC
    values = (0, 0, 0, 0, 0, 0, 0, 0)
    start = time.time()
    elapsed = 0
    while elapsed < 0.5:
        fc.execute(command, values)
        time.sleep(0.05)
        elapsed = time.time() - start

fc.start()
print("Arming...")
arm()
print("Armed.")
time.sleep(3)
print("Disarming...")
disarm()
print("Disarmed")