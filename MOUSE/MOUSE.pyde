from random import *

r = 13
g = 60
b = 110
value = 0
redRange= 1


def setup():
    size(500,500)
    background(255,255,255)

def draw():
    global r
    global g
    global b
    fill(r,g,b)
    stroke(r,g,b)
    ellipse(mouseX,mouseY,40,40)
    r=r+1
    if r == 60:
        r = 0
    g=g+1
    if g==140:
        g=0
    b=b+1
    if b==20:
        b=0