

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(20)

h = 25

for mi in range(260):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.008
    t.color(warna)
    t.pensize(3)
    t.goto(0,0)
    t.circle(mi)
    t.lt(160)
    t.circle(mi)
    t.lt(160)
    
t.done()