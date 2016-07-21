"""
Continuous Lines. 

Click and drag the mouse to draw a line. 
"""
green = [0,225,0]
yellow =[255,255,0]
white =[255,255,255]
red =[255, 0, 0]
blue =[0, 0, 225]
purple =[128,0,128]



def setup():
    size(640, 360)
    background(0, 0, 0)
    fill(0,225,0)#green
    rect(0, 0, 100, 100)  # Draw right rectangle
    fill(255,255,0) #yellow
    rect(100,0,100,100)
    fill(255,255,255)#white
    rect(200,0,100,100)
    fill(255, 0, 0)#red
    rect(300,0,100,100)
    fill(0, 0, 225)#blue
    rect(400,0,100,100)
    fill(128,0,128)#purple
    rect(500,0,100,100)
Charles= 1

def draw():
    global Charles
    noStroke()
    if mouseY < 100:
        if mouseX< 100 and mousePressed:
            Charles=1
        if mouseX < 200 and mouseX>100 and mousePressed:
            Charles=2
        if mouseX < 300 and mouseX>200 and mousePressed:
            Charles=3
    elif mouseY > 100:
        if mousePressed and Charles == 1:
            fill(0,225,0)
            ellipse(mouseX,mouseY,20,20)
        if mousePressed and Charles == 2:
            fill(255,255,0)
            ellipse(mouseX,mouseY,20,20)
        if mousePressed and Charles == 3:
            fill(255,255,255)
            ellipse(mouseX,mouseY,20,20)
        
            
   