

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(5)
t.pensize(2)

h = 255

for mi in range(300):
    t.goto(0, 0)
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.008
    t.pencolor(warna)
    t.circle(190-mi, 90)
    t.rt(120)
    t.rt(120)
    t.circle(190-mi, 90)
    t.circle(190-mi, 90)
    t.circle(190-mi, 60)

t.done()