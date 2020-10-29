#!/usr/bin/python
import sys
import time
import datetime

from itertools import cycle
from phue1 import Bridge
from TestMusic import doorbell


print("Start lightsystem")

b1 = Bridge('192.168.86.94')
b2 = doorbell()

print("Bell: " + str(b2))

# If the app is not registered and the button is not pressed, press the button $
b1.connect()

print(b1.ip)

print("File Path: " + b1.config_file_path)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##GPIO.setup(13, GPIO.OUT)
##GPIO.setup(16, GPIO.OUT)

releasedTime = False
tabedTime = False
timeDiff = False
quickTab = False

activeBulb = 1  #Spisebord 1
activeBulb = 2  #Spisebord 2
activeBulb = 3  #Lampe i stue
##activeBulb = 4  #Entre
##activeBulb = 5  #Plug
##activeBulb = 6  #Altan

slaveBulb = 1
up = False
a = 0
c = 0

alternatorUpDown = cycle(range(2))
alternatorScene = cycle(range(3))
alternatorOnOff = cycle(range(2))

prev_input_1 = 0
prev_input_2 = False

toggle = 0

LED_OnOff = 13
LED_Scene = 16

def onOff(activeBulb):
    print("onOff " + str(activeBulb))
    toggleState = b1.get_light(activeBulb, "on")
    print("toggleState: " + str(toggleState))
    if toggleState:
        b1.set_light(activeBulb, 'on', False)
##    b.set_light(slaveBulb, 'on', False)
    else:
        b1.set_light(activeBulb, 'on', True)
#       b.set_light(slaveBulb, 'on', True)

def upDown(activeBulb, up):
    lights = b.get_light_objects('id')
    actualBrightness = lights[activeBulb].brightness
    b.set_light(activeBulb, 'on', True)

    if(up):
        if (actualBrightness < 250):
            lights[activeBulb].brightness = actualBrightness + 5
            lights[slaveBulb].brightness = actualBrightness + 5
    else:
        if (actualBrightness > 5):
            lights[activeBulb].brightness = actualBrightness - 5
            lights[slaveBulb].brightness = actualBrightness - 5

def scene_1(activeBulb):
    command = {"on": True, "hue": 47103, "colormode": "xy", "xy": [0.3991, 0.4982]}
    b1.set_light(activeBulb, command)

def scene_2(activeBulb):
    command = {"on": True, "hue": 47103, "colormode": "xy", "xy": [0.3355, 0.3595]}
    b1.set_light(activeBulb, command)

def scene_3(activeBulb):
    command = {"on": True, "hue": 836, "colormode": "xy", "xy": [0.6475, 0.3316]}
    b1.set_light(activeBulb, command)

def scene_4(activeBulb):
    command = {"on": True, "hue": 836, "colormode": "xy", "xy": [0.6475, 0.3316]}
    b1.set_light(activeBulb, command)


##quickTab = True

def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')
    if channel == 11 : 
        activeBulb = 20
        onOff(activeBulb)
    if channel == 12 :
        b2.play(1)
    

GPIO.add_event_detect(11, GPIO.FALLING, callback=my_callback, bouncetime=200)  # add rising edge detection on a channel

GPIO.add_event_detect(12, GPIO.FALLING, callback=my_callback, bouncetime=200)


print("While 1")

var = True 
activeBulb = 0
a = 0



while var:
##    print("activeBulb: " + str(activeBulb))

##    if GPIO.event_detected(11):
##        print('Button pressed: 11')
##
##
##    if GPIO.event_detected(12):
##        print('Button pressed: 12')


##    if GPIO.input(11) == GPIO.LOW:
##        activeBulb = 3
##
##        toggle =  next(alternatorUpDown)
##        print("toggle: " + str(toggle))
##        onOff(activeBulb)
##        input_1 = 0
##        
##
##    # Toggle Scenes
####    input2 = GPIO.input(12)
##    if GPIO.input(12) == GPIO.LOW:
####    if input2 == 1:
##        print("input_2")
##        b2.play(1)
##        input2 = 0 
 
        
    activeBulp = 0
##    a = a + 1 
##    print("While loop: " + str(a))

print("lightsystem End")
    