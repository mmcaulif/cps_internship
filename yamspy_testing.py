from yamspy import MSPy
import numpy as np
import matplotlib.pyplot as plt
import time

inittime = time.time()
plot_t, plot_g = [], []

with MSPy(device="com3", loglevel='DEBUG', baudrate=115200) as board:
    #print(board)
    assert board != 1, "There's something wrong with the serial connection... check the logfile!"

    for i in range(10):
        # Read info from the FC
        # Please, pay attention to the way it works:
        # 1. Message is sent: MSP_ALTITUDE without any payload (data=[])
        if board.send_RAW_msg(MSPy.MSPCodes['MSP_ALTITUDE'], data=[]):  # 2. Response msg from the flight controller is received
            dataHandler = board.receive_msg()   # 3. The msg is parsed
            board.process_recv_data(dataHandler)    # 4. After the parser, the instance is populated.
            acc = board.SENSOR_DATA['accelerometer']
            gyro = board.SENSOR_DATA['gyroscope']
            volt = board.VOLTAGE_METER_CONFIGS
            att = board.SENSOR_DATA['kinematics']
            #time.sleep(0.1)
            t = time.time() - inittime
            print(i+1,":",acc,gyro,volt,att,round(t,3))
            plot_t.append(t)
            plot_g.append(gyro)

    plt.plot(plot_t, plot_g)
    plt.show()