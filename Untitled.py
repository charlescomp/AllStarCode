from Myro import *
init("sim")

speed=1
size=4
degrees=90

i = 0 # counter
penDown()
while i < 4:
    forward(speed,size)
    turnBy(degrees)
    i = i + 1
