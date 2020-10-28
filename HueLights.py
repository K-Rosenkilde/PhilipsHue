#!/usr/bin/python
from datetime import datetime, timedelta
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

firstrun = True

startdate = datetime.now().strftime('%d-%m-%Y')
print("startdate: " + str(startdate))

def setlogfile():
    global startdate, firstrun

    if startdate < datetime.now().strftime('%d-%m-%Y') or firstrun == True:
        print('startdate')
        firstrun = False
        startdatestr = datetime.now().strftime('%d_%m_%Y')
        LOG_FILENAME = '//home/pi/CodingProject/PhilipsHueControl/logs/Hue logfile ' + startdatestr + ' ' + datetime.now().strftime('%H_%M_%S.log')
        logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)
        logging.info('Start of file')


setlogfile();


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

b1 = Bridge('192.168.86.94')
# If the app is not registered and the button is not pressed, press the button $
b1.connect()

H3 = huelights()
#g1 = Group(b1, 1 )
#allLights = AllLights(g1)

if debug > 9: print(b1.config_file_path)

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
        

#i = 1
#loop = True
#_running = True
  
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

def Up21():
    print("Up21")
    activeBulb = 3
    upDown(activeBulb, True)

def Down21():
    print("Down21")
    activeBulb = 3
    upDown(activeBulb, False)

def getValue(activeBulb):
#    print("getValue")
    lights = b1.get_light_objects('id')
#    actualBrightness = lights[activeBulb].brightness
#    print("actualBrightness: " + str(actualBrightness))
    
def changeBrightness(activeBulb, value):
#    print("changeBrightness")
    
    if activeBulb > 0 :
        if debug > 8: print("Testtt: " + str(activeBulb))
        lights = b1.get_light_objects('id')
        actualBrightness = b1.get_light(activeBulb, "bri")
        
        if debug > 8:  print("actualBrightness: " + str(actualBrightness))
        if b1.get_light(activeBulb, "on"): 
            lights[activeBulb].brightness = int(value)

def UpdateValue(event):
    if debug > 8: print("Value: " + event)
    activeBulb = 3
    changeBrightness(activeBulb, event)


def printinfo():
    print("activeBulb: " + str(activeBulb))


def changeBrightnessNew(activeBulb):
    print("changeBrightness")
    
    if activeBulb > 0 :
        print("activeBulb: " + str(activeBulb))
        lights = b1.get_light_objects('id')
        actualBrightness = b1.get_light(activeBulb, "bri")
        print("actualBrightness: " + str(actualBrightness))
        
        if b1.get_light(activeBulb, "on"):
            print("Set Brightness")
            if H3.getdirection(channel) == "up":  
                print("IF Set Brightness up")
                if actualBrightness > 246:
                    lights[activeBulb].brightness = 255
                    H3.setdirection(18, "down")
                else:     
                    lights[activeBulb].brightness = int(actualBrightness+10)
            else:
                print("ELSE Set Brightness down")
                if actualBrightness < 11:
                    lights[activeBulb].brightness = 1
                    H3.setdirection(18, "up")
                    print()
                else:     
                   lights[activeBulb].brightness = int(actualBrightness-10)
               
#         else:
#             H3.dimdirection = "up"
#             toggleLight3()
#             lights[activeBulb].brightness = 10

def changeBrightnessChannel(channel):
    print("changeBrightnessChannel")
    activeBulb = H3.getlight(channel)    
    print("activeBulb: " + str(activeBulb))
                
    group = H3.getgroup(channel)
    print("group: " + str(group))
    lightsingroup = H3.getgrouplights(group)
    print("lightsingroup :" + str(lightsingroup))
    
    actualBrightness = b1.get_light(activeBulb, "bri")
    print("actualBrightness: " + str(actualBrightness))
    
    if debug > 8: print("lights: " + str(lights))
    
    if b1.get_light(activeBulb, "on"):
        lights = b1.get_light_objects('id')
    
        print("Set Brightness")
        if H3.getdirection(channel) == "up":  
            print("IF Set Brightness up")
            if actualBrightness > 246:
                for obj in lightsingroup.split():
                    lights[int(obj)].brightness = 255
                H3.setdirection(channel, "down")
            else:
                for obj in lightsingroup.split():
                    print("Obj: " + str(obj) )
                    print("Light: " + str(lightsingroup[int(obj)])  )
                    print("lights[int(obj)].brightness: " + str(lights[int(obj)].brightness ))
                    
                    lights[int(obj)].brightness = int(actualBrightness+10)
        else:
            print("ELSE Set Brightness down")
            if actualBrightness < 11:
                for obj in lightsingroup.split():
                    lightsingroup[int(obj)].brightness = 1
                H3.setdirection(channel, "up")
            else:
                for obj in lightsingroup.split():
                    lights[int(obj)].brightness = int(actualBrightness-10)
    
    
    
 
def onOffgroup(channel):
    print("changeBrightnessChannel")
    activeBulb = H3.getlight(channel)
    
    
    group = H3.getgroup(channel)
    print("group: " + str(group))
    lights = H3.getgrouplights(group)
    
    if debug > 8: print("lights: " + str(lights))
    
    toggleState = b1.get_light(activeBulb, "on")
    if toggleState:
        for obj in lights.split():
            print("lights: " + str( obj ))
            b1.set_light(int(obj), 'on', False)
    else:
        for obj in lights.split():
            print("lights: " + str( obj ))
            b1.set_light(int(obj), 'on', True)
            

def my_callback(channel):
    logging.debug('')
#     print("Time Fall: " + str(now))
    print("---------------------- Start -----------------------------")
    print('This is a edge event callback function!: ' + str(channel ))
#    print("lightnumber: " + str(myLights.index(channel) ))    


    lamptype = b1.get_light(H3.getlight(channel), "type")
    if lamptype == "On/Off plug-in unit":
       Dimmable = False 
    if lamptype == "Dimmable light" or lamptype == "Color temperature light" or lamptype == "Extended color light":
        Dimmable = True
    print("lamptype: " + str(lamptype) + ", Dimmable: " + str(Dimmable))
    
    if Dimmable:
        if not GPIO.input(channel):
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
    #         print("down: " + str(down))
    #         print("down60 : " + str(timedelta60))

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

    print("----------------------  End  -----------------------------")

    
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

var = True

while var:
    setlogfile()
    

print("Hue Light End")
