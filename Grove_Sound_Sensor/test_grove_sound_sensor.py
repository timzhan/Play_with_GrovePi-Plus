# test Grove Sound Sensor
# by Tim Zhan

import time
import grovepi

# Connect the Grove Sound Sensor to analog port A0
# SIG,NC,VCC,GND
sound_sensor = 0

grovepi.pinMode(sound_sensor,"INPUT")


while True:
    try:
        # Read the sound level
        sensor_value = grovepi.analogRead(sound_sensor)

        print("sensor_value = %d" %sensor_value)
        time.sleep(1)

    except IOError:
        print ("Error")
