#!/usr/bin/python
from datetime import datetime, timedelta
from itertools import cycle
from phue import Bridge
from phue import Group
from phue import AllLights
from huelightClass import huelights
from TestMusic import doorbell

import time
import json
import threading
import RPi.GPIO as GPIO
import logging

LOG_FILENAME = datetime.now().strftime('Newlogfile_%H_%M_%S_%d_%m_%Y.log')
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

#Init Variables
activeBulb = 0

global up # = datetime.now()
global down # = datetime.now()
global debug
debug = 8  #zero no print statements,  10: All Print statements  

# Setup input Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)


print("Start lightsystem")
global b1
b1 = Bridge('192.168.86.94')
# If the app is not registered and the button is not pressed, press the button $
b1.connect()

H3 = huelights()
hueLights = json.dumps(b1.get_light(), indent=4 )
if debug > 8: print(hueLights)

g1 = Group(b1, 1 )
allLights = AllLights(g1)

b2 = doorbell()
if debug > 7: print("Bell: " + str(b2))

def doorbell(no):
    b2.play(no)

print ("Star Up Time: " + str(datetime.now()))
doorbell(1)

if debug > 8: print(b1.config_file_path)

def getLightInfo(activeBulb):    
    if debug > 9:
        allinfo = b1.get_light(activeBulb)
#     print("getLightInfo: " , allinfo)
        name = b1.get_light(activeBulb, "name")
        print("name %s", name )
    
        state = b1.get_light(activeBulb, "type")
        if state == "On/Off plug-in unit":
            print("Type: " , state )
        if state == "Dimmable light":
            brigthness = b1.get_light(activeBulb, "bri")
            print("Type %s - and Brightness %d " , state , brigthness)
        if state == "Color temperature light":
            brigthness = b1.get_light(activeBulb, "bri")
#        colorgamut = b1.get_light(activeBulb, "colorgamut")
#        color =  b1.get_light(activeBulb, "xy")
            colormode = b1.get_light(activeBulb, "colormode")
            print("Type: %s,  Brightness: %d, Colormode: %s" %( state , brigthness, colormode))
        if state == "Extended color light":
            brigthness = b1.get_light(activeBulb, "bri")
#        colorgamut = b1.get_light(activeBulb, "colorgamut")
            color =  b1.get_light(activeBulb, "xy")
            colormode = b1.get_light(activeBulb, "colormode")
            print("Type: %s, Brightness: %d, Color: %s, Colormode: %s " %( state , brigthness, color, colormode))
        
  
def onOff(activeBulb):
    print("onOff " + str(activeBulb))
    toggleState = b1.get_light(activeBulb, "on")

    print("toggleState: " + str(toggleState))
    if toggleState:     
        b1.set_light(activeBulb, 'on', False)
    else:
        b1.set_light(activeBulb, 'on', True)


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


def play():
    print("play")
    
    #Setup 
    Lightgroup = 3

    lightsingroup = H3.getgrouplights(Lightgroup)    
    lights = b1.get_light_objects('id')
    
    print("    lightsingroup : " + lightsingroup)
    k = 1
    i = 0
    n = 0
    
    noLight = len(lightsingroup.split())
    print("    No of lights: " + str(noLight))    
    
    offset = int(noLight -1 )    
    
    while i < 10:       
        i += 1
        for obj in lightsingroup.split():    
            
            if n == 0:
                time.sleep(0.2)
                a = int(obj)
                b1.set_light(a+offset, 'on', False, 1)
                b1.set_light(a, 'on', True, 1)
            if n == 1:
                time.sleep(0.2)
                b = int(obj)            
                b1.set_light(a, 'on', False, 1)
                b1.set_light(b, 'on', True, 1)
            if n == 2:
                time.sleep(0.2)
                c = int(obj)
                b1.set_light(b, 'on', False, 1)            
                b1.set_light(c, 'on', True, 1)
            if n == 3:
                time.sleep(0.2)
                d = int(obj)
                b1.set_light(c, 'on', False, 1)
                b1.set_light(d, 'on', True, 1)
            n += 1
        if n > offset: n = 0
        
    print("play End")



def group():
    print("Start group")
    Lightgroup = 6

    lightsingroup = H3.getgrouplights(Lightgroup)    
    print("    lightsingroup : " + str( lightsingroup))
    
    b1.set_light(lightsingroup, 'on', True)
    print("End group")


def getValue(activeBulb):
    lights = b1.get_light_objects('id')

def UpdateValue(event):
    if debug > 8: print("Value: " + event)
    activeBulb = 3
    changeBrightness(activeBulb, event)

def printinfo():
    print("activeBulb: " + str(activeBulb))


def changeBrightnessChannel(channel):
    print("changeBrightnessChannel")
    activeBulb = H3.getlight(channel)    
    actualBrightness = b1.get_light(activeBulb, "bri")
    group = H3.getgroup(channel)
    lightsingroup = H3.getgrouplights(group)

    print("activeBulb: " + str(activeBulb))                
    print("group: " + str(group))    
    print("lightsingroup :" + str(lightsingroup))    
    print("actualBrightness: " + str(actualBrightness))

    if b1.get_light(activeBulb, "on"):
        lights = b1.get_light_objects('id')
    
        print("Set Brightness")
        if H3.getdirection(channel) == "up":  
            print("IF Set Brightness up")
            if actualBrightness > 246:
                b1.set_light(lightsingroup, 'bri', 255) 
                H3.setdirection(channel, "down")
            else:
                b1.set_light(lightsingroup, 'bri', int(actualBrightness+10))                
        else:
            print("ELSE Set Brightness down")
            if actualBrightness < 11:
                b1.set_light(lightsingroup, 'bri', 1)
                H3.setdirection(channel, "up")
            else:
                b1.set_light(lightsingroup, 'bri', int(actualBrightness-10))

def onOffgroup(channel):
    print("changeBrightnessChannel")
    activeBulb = H3.getlight(channel)    
    group = H3.getgroup(channel)
    lights = H3.getgrouplights(group)
    
    print("group: " + str(group))
    
    toggleState = b1.get_light(activeBulb, "on")
    if toggleState:
        b1.set_light(lights, 'on', False)
    else:
        b1.set_light(lights, 'on', True)
            

def my_callback(channel):
#     print("Time Fall: " + str(now))
    print("---------------------- Start -----------------------------")
    print('This is a edge event callback function!: ' + str(channel ))
#    print("lightnumber: " + str(myLights.index(channel) ))    
    
    if(channel == 17):
        if not GPIO.input(channel):
            doorbell(1)
    else: 
        print("else")
        lightControl(channel)
        
    print("----------------------  End  -----------------------------")
        
        
def lightControl(channel):
    print("lightControl: " + str(channel))
#    global down 
    print("GPIO: " + str(GPIO.input(channel)))

    lamptype = b1.get_light(H3.getlight(channel), "type")
    if lamptype == "On/Off plug-in unit":
        Dimmable = False 
    if lamptype == "Dimmable light" or lamptype == "Color temperature light" or lamptype == "Extended color light":
        Dimmable = True
    print("lamptype: " + str(lamptype) + ", Dimmable: " + str(Dimmable))
    
    if Dimmable:        
        if not GPIO.input(channel) :
            print("GPIO: " + str(GPIO.input(channel)))
            logging.info('Light: ' + str(H3.getlight(channel)))
            global down
            down = datetime.now()
            print("down: " + str(down))        
              
            while not GPIO.input(channel):
                time.sleep(0.1)
                changeBrightnessChannel(channel)
    #             changeBrightnessNew(H3.getlight(channel))            
        else:
            up = datetime.now()
                
            print("Rising edge detected on: " + str(channel) + " - " + str(up))
            elapsedTime = up - down
            timedelta60 = down + timedelta(seconds = 1)
            print("down: " + str(down))
            print("down60 : " + str(timedelta60))

            if up < timedelta60 :
    #             onOff( H3.getlight(channel))
                onOffgroup(channel)
                
            print("Time elapsed: " + str(elapsedTime))
            
            # Change dim Direction
            if H3.getdirection == "up":
                H3.setdirection(channel, "down")
            else:
                H3.setdirection(channel, "up")
    else:
        if not GPIO.input(channel):
            logging.info('Light: ' + str(H3.getlight(channel)))
            onOffgroup(channel)



    
GPIO.add_event_detect(1, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(2, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(5, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(7, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(8, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(9, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(10, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(12, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(13, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(14, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(15, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(16, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(17, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(18, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(19, GPIO.BOTH, callback=my_callback, bouncetime=200)
GPIO.add_event_detect(20, GPIO.BOTH, callback=my_callback, bouncetime=200)

