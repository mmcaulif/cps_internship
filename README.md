# cps_internship

## Week 1:
There was little to no documentation on the flight controller being used which posed a lot of initial frustration as I hadn't any idea about where to start. From looking into betaflight and the protocol's used to communicate with drones I found several that seemed promising; MultiWiiSerial protocol (MSP), I2C, SBUS and dronekit.

The first week involved mainly just experimentation with little to no tangible results. The main issue causing this was the fact that these protocols were mostly handled by the mainstream flight configuration software and were traditionally never really tweaked or implemented by the average drone flyer and as such implementations in languages like python to be used to communicate to a flight controller without the aid of a flight configurator software was simply not common enough.

I found a couple python libraries implementing a couple of the protocols but all were quite old and poorly documented, there was a lot of trial and error involved in experimenting with these libraries, most of which just didn't work for no apparent reason, and quite often gave no indication that there was even communication taking place making it quite difficult to debug. 

Finally, one of the libraries (PyMultiWii) finally worked and successfully returned telemetry data (accelerometer and gyroscope) from the drone. This worked incredibly well and was the first tangible step towards creating the testbench for the drone by showing that we can in fact send commands to the drone without going through a flight configurator.

---

## Week 2:
Once the communication protocol was established and data could be read from the drone, the next step was to allow for a two way conversation between the drone and pc and to be able to send msp commands to the drone while tracking its location etc.

The end goal for the testbench would involve something like this:
* Send RC messages to the drone
* Drone responds with telemetry data
* Computer logs data and calculates relationship between rc commands and corresponding change in location/telemetry data
* Calibrate controller and any other variable acting in the drone

Unfortunately it became clear that I could not send RC commands to the drone (Serial RX cannot be swtitched on the usb port and is needef for these commands https://github.com/alduxvm/pyMultiWii/issues/36) thus we looked to alternative means to send commands to the drone through the UART ports (which we've confirmed are on the board).

---

## Week 5:
From parsing the code given to us by Henning we have found that the arming message sent to the microbit is as follows '\x00\x01\x02\x00\x06\x00\x08\x00\x0e\x00\x13\xff\x14\x00\x18\x00' 
