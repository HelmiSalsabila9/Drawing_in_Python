

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(5)
t.pensize(2)
t.goto(0, -180)

h = 0

for mi in range(300):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.008
    t.pencolor(warna)
    t.left(120)
    t.circle(mi-90, 180)
    t.left(120)


t.done()