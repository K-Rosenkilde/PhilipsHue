#!/usr/bin/python
#import time
from datetime import datetime, timedelta
from tkinter import *
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

LOG_FILENAME = datetime.now().strftime('logfile_%H_%M_%S_%d_%m_%Y.log')
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

#Init Variables
activeBulb = 0

global up # = datetime.now()
global down # = datetime.now()
global debug
debug = 8  #zero no print statements,  10: All Print statements  

# down = datetime.now()
# if debug > 0: print("Starting: " + str(down))

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
# hueLights = json.dumps(b1.get_light(), indent=4 )
# print(hueLights)

#lights = b1.get_light()
#print(lights)

#print("Hue Light: " + str(b1.get_light() ))

#b2 = doorbell()
#print("Bell: " + str(b2))

g1 = Group(b1, 1 )

allLights = AllLights(g1)


#print(b1.ip)
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


# def upDown(activeBulb, up):
#     print("upDown")
#     lights = b1.get_light_objects('id')    
#     actualBrightness = b1.get_light(activeBulb, "bri")
#     print("actualBrightness XXX: " + str(actualBrightness))
# #    actualBrightness = lights[activeBulb].brightness
# #    lights = b1.set_light(activeBulb, 'id')
#     print("lights: " + str(lights))
#     
#     if(up):
#         if (actualBrightness < 250):
#             lights[activeBulb].brightness = actualBrightness + 10
# #            lights[slaveBulb].brightness = actualBrightness + 5
#     else:
#         if (actualBrightness > 5):
#             lights[activeBulb].brightness = actualBrightness - 10
# #            lights[slaveBulb].brightness = actualBrightness - 5

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


window = Tk() 
window.title("Welcome to Hue Lights Control Panel")
window.geometry('600x600')

# def clicker(event):
#     _running = True
#  #   threading.Thread(my_loop()).start()
#     myLabel = Label(window, text = "You Clicked Me")
#     myLabel.grid(column=9, row=2)
#     
# def clickerStop(event):
#     print("clickerStop")
#     loop = False
#     _running = False # this will stop the loop in the other thread... 
#     myLabel = Label(window, text = "-")
#     myLabel.grid(column=9, row=2)
# 
# def myUpDown():
#     i = 0
#     while loop:
#       i += 1
#       print("i: " + str(i))
#       
#       #if i > 1024 then i = 1


# eButton = Button(window, text = "Click Me")
# eButton.bind("<ButtonRelease-1>", on_release)
# eButton.bind("<Button-1>", on_press)
# eButton.grid(column=9, row=1)


def toggleLight1():
    print("Toggle Light Stairs1") 
    activeBulb = 1
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight2():
    print("Toggle Light Stairs2") 
    activeBulb = 2
    getLightInfo(activeBulb)
    onOff(activeBulb)
    
def toggleLight3():
    print("Toggle Light Stairs3")
    activeBulb = 3
    getLightInfo(activeBulb)
    onOff(activeBulb)
    
def toggleLight4():
    print("Toggle Light Stairs3")
    activeBulb = 4
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight5():
    print("Toggle Light Stairs1") 
    activeBulb = 5
    getLightInfo(activeBulb)
    onOff(activeBulb)   

def toggleLight6():
    print("Toggle Light Stairs2") 
    activeBulb = 6
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight7():
    print("Toggle Light Stairs3")
    activeBulb = 7
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight8():
    print("Toggle Light Stairs3")
    activeBulb = 8
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight9():
    print("Toggle Light Stairs1") 
    activeBulb = 9
    getLightInfo(activeBulb)
    onOff(activeBulb)
    
def toggleLight10():
    print("Toggle Light Stairs2") 
    activeBulb = 10
    getLightInfo(activeBulb)
    onOff(activeBulb)
    
def toggleLight11():
    print("Toggle Light Stairs3")
    activeBulb = 11
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight12():
    print("Toggle Light Stairs3")
    activeBulb = 12
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight13():
    print("Toggle Light 13") 
    activeBulb = 13
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight14():
    print("Toggle Light 14") 
    activeBulb = 14
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight15():
    print("Toggle Light 15")
    activeBulb = 15
    getLightInfo(activeBulb)
    onOff(activeBulb)
 
def toggleLight16():
    print("Toggle Light 16")
    activeBulb = 16
    getLightInfo(activeBulb)
    onOff(activeBulb)
        
def toggleLight17():
    print("Toggle Light 17")
    activeBulb = 17
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight18():
    print("Toggle Light 18")
    activeBulb = 18
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight19():
    print("Toggle Light 19")
    activeBulb = 19
    getLightInfo(activeBulb)
    onOff(activeBulb)

def toggleLight20():
    print("Toggle Light 20")
    activeBulb = 20
    getLightInfo(activeBulb)
    onOff(activeBulb)

def Up21():
    print("Up21")
    activeBulb = 3
    upDown(activeBulb, True)

def Down21():
    print("Down21")
    activeBulb = 3
    upDown(activeBulb, False)

btn1 = Button(window, text="1. Stairs 1", command=toggleLight1).grid(column=1, row=1)
btn2 = Button(window, text="2. Stairs 2", command=toggleLight2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text="3. Stairs 3", command=toggleLight3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text="4. Entre", command=toggleLight4)
btn4.grid(column=1, row=2)
btn6 = Button(window, text="6. Altan", command=toggleLight6)
btn6.grid(column=2, row=2)
btn7 = Button(window, text="7. Bedroom", command=toggleLight7)
btn7.grid(column=3, row=2)
btn5  = Button(window, text="5. Billed Spot", command=toggleLight5)
btn5.grid(column=1, row=3)
btn8  = Button(window, text="8. Kuppel", command=toggleLight8)
btn8.grid(column=2, row=3)
btn10 = Button(window, text="10. Kip Light", command=toggleLight10)
btn10.grid(column=3, row=3)
btn15 = Button(window, text="15. Desks", command=toggleLight15)
btn15.grid(column=5, row=3)
btn9  = Button(window, text="9.  Hall 1", command=toggleLight9)
btn9.grid(column=1, row=5)
btn11 = Button(window, text="11. Hall 2", command=toggleLight11)
btn11.grid(column=2, row=5)
btn17 = Button(window, text="17. Hall 3", command=toggleLight17)
btn17.grid(column=3, row=5)
btn12 = Button(window, text="12. Entre", command=toggleLight12)
btn12.grid(column=1, row=6)
btn13 = Button(window, text="13. Dinner UP", command=toggleLight13)
btn13.grid(column=1, row=6)
btn14 = Button(window, text="14. Dinner Down", command=toggleLight14)
btn14.grid(column=2, row=6)
btn19 = Button(window, text="19. Balcony 1", command=toggleLight19)
btn19.grid(column=1, row=7)
btn18 = Button(window, text="18. Balcony 2", command=toggleLight18)
btn18.grid(column=2, row=7)
btn20 = Button(window, text="20. Balcony 3", command=toggleLight20)
btn20.grid(column=3, row=7)
btn16 = Button(window, text="16. Hue Ambiance Spot test", command=toggleLight16)
btn16.grid(column=1, row=8)
lbl1 = Label(window, text="Test") 
lbl1.grid(column=1, row=11)
btn21 = Button(window, text="21. Up", command=Up21)
btn21.grid(column=1, row=10)
btn21 = Button(window, text="22. Down", command=Down21)
btn21.grid(column=2, row=10)

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


btntest = Button(window, text="print", command=printinfo)
btntest.grid(column=1, row=9)

dimValue = 40
#w = Scale(window, from_=0, to=42)
w = Scale(window, from_=1, to=255, orient=HORIZONTAL, command=UpdateValue)
w.set(dimValue) 
w.grid(column=2, row=9)

btnQuit = Button(window, text="Quit", command=quit) 
btnQuit.grid(column=5 , row=11)


# def toggleLight(activeBulb):
#     print("toggleLight: " + str(toggleLight))
#     getLightInfo(activeBulb)
#     onOff(activeBulb)


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

    
    
#     if channel == 17 :
#         if not GPIO.input(17):     # if port 25 == 1   
#             print("channel == 17")
# #             b2.play(1)
# #            scene_2(2)
#             for obj in lights.split():
#                 print("lights: " + str( obj ))
#                 changeBrightnessNew(int(obj))
#         else:
#             for obj in lights.split():
#                 print("lights: " + str( obj ))
#                 onOff( H3.getlight(channel))            
#                 
#     
#     if channel == 18 :    
#         if not GPIO.input(18):     # if port 25 == 1
#             global down 
#             down = datetime.now()
#             print("Falling edge detected on 25" + str(down))
#             i = 0
#             k = 0
#             n = 0
#             while not GPIO.input(18):
#                 time.sleep(0.1)  
# #                 now = datetime.now()
# #                 elapsedTime = now - down
# #                 timedelta60 = down + timedelta(seconds = 1)
# #                print("Falling elapsedTime: " +str(elapsedTime))
#                 i += 1
#                 k = round(i / 2) 
#                 if k > n :
#                     if debug > 9: print("**********************************************************************************i: " + str(k))
# #                     if down > timedelta60 :
#                     changeBrightnessNew(3)
#                     n = k
#         else:                  # if port 25 != 1
#  #           _running = False
#             if H3.getdirection == "up":
#                 H3.setdirection(channel, "down")
#             else:
#                 H3.setdirection(channel, "up")
#             up = datetime.now()
#             print("Rising edge detected on 18" + str(up))
#             elapsedTime = up - down
#             timedelta60 = down + timedelta(seconds = 1)
#             print("down: " + str(down))
#             print("down60 : " + str(timedelta60))
#             if up < timedelta60 :
#                 onOff( H3.getlight(channel))
#             print("Time elapsed: " + str(elapsedTime))

    
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

#Start GUI Main loop
window.mainloop()

print("Hue Light GUI End")