# test Grove Button
# by Tim Zhan

import time
import grovepi

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3

grovepi.pinMode(button,"INPUT")

print("Try to press the button ...")

while True:
    try:
	result = grovepi.digitalRead(button)
	if result == 1:  
		print('Button is pressed!')
        time.sleep(0.2)

    except IOError:
        print ("Error")
