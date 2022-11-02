
# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(1000)
t.pensize(4)

h = 0 

t.hideturtle()
t.goto(100, 0)

for mi in range(1000):
    warna = c.hsv_to_rgb(h,1,1)
    t.color(warna)
    h += 0.1
    for me in range(8):
        t.left(120)
        t.forward(mi*2+3)
        t.left(120)
        t.circle(mi-30, 180)
        t.right(24)
        t.forward(mi)

t.done()