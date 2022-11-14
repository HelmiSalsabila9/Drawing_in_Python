

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(5)

h = 25

for mi in range(360):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.008
    t.goto(0,0)
    t.pensize(3)
    t.color(warna)
    t.begin_fill()
    t.circle(100-mi, 90)
    t.bk(180)
    t.lt(90)
    t.circle(100-mi, 90)
    t.begin_fill()

t.done()