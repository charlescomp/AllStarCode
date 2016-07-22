from time import *
from random import *

aliens = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

x = 35
    
y = 35

xspaceship = 185

ySpaceship = 375

xbullet = 0

yBullet = 0

isBulletShot = False





def setup():
    global aliens
    size(400, 400)
    background(0)
  
    

def draw():
    global x
    global y
    global aliens 
    global fill
    global xspaceship, ySpaceship
    global isBulletShot
    global yBullet
    global xBullet
     
    for slist in range(len(aliens)):
        for index in range(len(aliens[slist])): 
            if aliens[slist][index] == 1:
                fill(255, 0, 0)
                ellipse(x, y, 30, 30)#circles
                fill(255, 255, 255)
                rect(xspaceship, 375, 30, 30)
                
                x = x + 100
            
            if x > 400:
                y = y + 100
                x = 35 
                
    if keyPressed and xspaceship > 5:
        if keyCode == 37:
            xspaceship = xspaceship - 1
    
    if keyPressed and xspaceship < 380:
        if keyCode == 39:
            xspaceship =  xspaceship + 1
    
    if keyPressed:
        if keyCode == 0 and isBulletShot == False:
            isBulletShot = True
            xBullet = xspaceship
            yBullet = ySpaceship
            
        
    print isBulletShot
    
    if isBulletShot == True: 
        fill(255, 255, 255)
        rect(xBullet, yBullet, 30, 30) 
        yBullet = yBullet - 1
        
        if yBullet < -30:
            isBulletShot = False