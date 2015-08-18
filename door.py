import urllib2
import time
import RPi.GPIO as io
io.setmode(io.BCM)
 
door_sensor = 18
door_onelight = 25
sensorTrigger = True
 
io.setup(door_sensor, io.IN, pull_up_down=io.PUD_UP)
io.setup(door_onelight, io.OUT, pull_up_down=io.PUD_UP)
 
# function for the door opening
def door_open():
    print("Door Open")
 
# function for the door closing
def door_close():
    print("Door Close")
 
while True:
    print("check")
    if io.input(door_sensor): # if door is opened
        if (sensorTrigger):
            door_open() # fire GA code
            sensorTrigger = False # make sure it doesn't fire again
            io.output(door_onelight,True)
    if not io.input(door_sensor): # if door is closed
        if not (sensorTrigger):
            door_close() # fire GA code
            sensorTrigger = True # make sure it doesn't fire again
            io.output(door_onelight,False)
    time.sleep(1)

def turnOffLights():
    print("exit")
    io.output(door_onelight,False)

import atexit
atexit.register(turnOffLights)
