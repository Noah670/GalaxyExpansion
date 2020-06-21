# Galaxy Expansion
# Noah670
# turtle library

from turtle import *
import os


title("Galaxy Expansion")
speed(0)


def expandGalaxy():
    #Outer space color
    bgcolor("#343d46")

    r, g, b = 255, 0, 0

    for i in range(255*4):
        colormode(255)
        if i < 255//3:
            g += 3
        elif i < 255*2//3:
            r -= 3
        elif i < 255:
            b += 3
        elif i < 255*4//3:
            g -= 3
        elif i < 255*5//3:
            r += 3
        else:
            b -= 3

        fd(50+i)
        rt(91)

        pencolor(r, g, b)



expandGalaxy()
