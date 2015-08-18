import os
import RPi.GPIO as io

door_onelight = 25

io.setmode(io.BCM)

io.setup(door_onelight, io.OUT, pull_up_down=io.PUD_UP)
io.output(door_onelight,False)


print("exit")
