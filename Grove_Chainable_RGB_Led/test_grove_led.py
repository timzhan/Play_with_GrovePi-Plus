
# test Grove Chainable LED
# by Tim Zhan

import time
import grovepi

# I have only one LED so just connect it to the D7 port of GrovePi
pin = 7
numleds = 1    #If you have x LEDs, change 1 to x.

grovepi.pinMode(pin,"OUTPUT")
time.sleep(1)


# test colors used in grovepi.chainableRgbLed_test()
testColorBlack = 0   # 0b000 #000000
testColorBlue = 1    # 0b001 #0000FF
testColorGreen = 2   # 0b010 #00FF00
testColorRed = 4     # 0b100 #FF0000


# patterns used in grovepi.chainableRgbLed_pattern()
thisLedOnly = 0


try:

    print("Initialize the chinable RGB led ...")

    # init chain of leds
    grovepi.chainableRgbLed_init(pin, numleds)
    time.sleep(.5)

    # change color to RED
    print("Change color to red ...")
    grovepi.chainableRgbLed_test(pin, numleds, testColorRed)
    time.sleep(1)

    # change color to GREEN
    print("Change color to green ...")
    grovepi.chainableRgbLed_test(pin, numleds, testColorGreen)
    time.sleep(1)

    # change color to BLUE
    print("Change color to blue ...")
    grovepi.chainableRgbLed_test(pin, numleds, testColorBlue)
    time.sleep(1)

    # reset (all off)
    grovepi.chainableRgbLed_test(pin, numleds, testColorBlack)
    time.sleep(.5)


except KeyboardInterrupt:
    # reset (all off)
    grovepi.chainableRgbLed_test(pin, numleds, testColorBlack)
except IOError:
    print ("Error")
