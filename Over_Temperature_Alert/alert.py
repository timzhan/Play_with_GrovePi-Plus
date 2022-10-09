# Project 2: Over-Temperature Alert
# When the temperature is over than a threshold, the buzzer will beep
# by Tim Zhan

import grovepi
import time
import math

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
pin_dht11 = 4  # The Sensor goes on digital port D4.

# temp_humidity_sensor_type
# DH11 is the blue sensor
blue = 0    # DHT11
white = 1   # DHT Pro

# Set threshold for alert
threshold = 29 	# change to your own

# Connect the Grove Buzzer to digital port D8
# SIG,NC,VCC,GND
pin_buzzer = 8
grovepi.pinMode(pin_buzzer,"OUTPUT")

while True:
    try:
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(pin_dht11,blue)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f *C, humidity = %.02f%%"%(temp, humidity))
	
	if temp >= threshold:	
            # Buzz for 1 second
            grovepi.digitalWrite(pin_buzzer,1)
            print ('start')
            time.sleep(1)

            # Stop buzzing for 1 second and repeat
            grovepi.digitalWrite(pin_buzzer,0)
            print ('stop')
            time.sleep(1)	

	time.sleep(5)

    except KeyboardInterrupt:
        grovepi.digitalWrite(pin_buzzer,0)
	break

    except IOError:
        print ("Error")
