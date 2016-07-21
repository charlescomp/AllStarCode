from time import *
from random import *


#vars
moveX= 250
moveY= 250
SpdX=0
SpdY=0
SpdX2=0
SpdY2=0



def setup():
    global SpdX
    global SpdY
    background(255)
    size(500,500)
    sleep(.1)
    SpdX=randint(-10,10)
    SpdY=randint(-10,10)
    SpdX2=randint(-20,20)
    SpdY2=randint(-20,20)
    sleep(.1)
    
    
def draw():
    global moveX
    global moveY
    global SpdX
    global SpdY
    global SpdX2
    global SpdY2
    
    background(255)
    fill(181)
    stroke(180)
    ellipse(moveX,moveY,50,50)
    moveX=moveX+SpdX
    moveY=moveY+SpdY
    if moveX >= 490:
        sleep(.01)
        SpdX=SpdX*-1

    if moveX <= 10:
        sleep(.01)
        SpdX=SpdX*-1

    if moveY >= 490:
        sleep(.01)
        SpdY=SpdY*-1

    if moveY <= 10:
        sleep(.01)
        SpdY=SpdY*-1
        
    background(0)
    fill(255,0,0)
    stroke(0,0,0)
    ellipse(moveX,moveY,50,50)
    moveX=moveX+SpdX2
    moveY=moveY+SpdY2
    if moveX >= 490:
        sleep(.01)
        SpdX2=SpdX2*-1

    if moveX <= 10:

        SpdX2=SpdX2*-1

    if moveY >= 490:
        sleep(.01)
        SpdY2=SpdY2*-1

    if moveY <= 10:
        sleep(.01)
        SpdY2=SpdY2*-1
  
  