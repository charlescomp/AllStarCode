from Myro import *

DarkBlue = makeColor(0,51,76)

Red = makeColor(217, 26, 33)

Blue = makeColor(112,150,158)

Yellow = makeColor(252, 227, 166)



pic = makePicture(pickAFile())
pixels = getPixels (pic)
for pixel in pixels:
    if getGray(pixel)> 180:
        setColor(pixel,Yellow)
    elif getGray(pixel)> 120:
        setColor(pixel,Blue)
    elif getGray(pixel)> 60:
        setColor(pixel,Red)
show(pic)
savePicture(pic,"Tinko.jpg") 
    
    