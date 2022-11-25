

# SKUYMI [helmsialsabila.com]

import math
from turtle import *
import colorsys as c 

def hati(n):
    return 14*math.sin(n)**3

def hatii(n):
    return 12*math.cos(n)-5*\
        math.cos(2*n)-2*\
        math.cos(3*n)-\
        math.cos(4*n)

tracer(5)
h = 0.4
bgcolor('black')

for mi in range(1000):
    goto(hati(mi)*20, hatii(mi)*20)
    for me in range(5):
        warna = c.hsv_to_rgb(h,1,1)
        h += 0.005
        color(warna)
        goto(0,0)

done()