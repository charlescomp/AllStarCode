from random import *
from time import sleep

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
x = 0
y = 150

i = choice(letters)

def setup():
    size(500,250)
    background(225)

def draw():
    global x
    global y
    global letters
    background(225)
    fill(0)
    textSize(26)
    text(y, x, 150)
    x = x+10
    sleep(.1)
    if keyPressed:
        if key == i:
            background(0)
            x = 0
            i = choice(letters)
    
    
# if x > 250:
    #    x = 0
    #   y = randint(0, 250)

        
    