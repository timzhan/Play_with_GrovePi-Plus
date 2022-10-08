# test Grove Light Sensor
# by Tim Zhan
#

import time
import grovepi

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

grovepi.pinMode(light_sensor,"INPUT")

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value

        print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
        time.sleep(5)

    except IOError:
        print ("Error")
