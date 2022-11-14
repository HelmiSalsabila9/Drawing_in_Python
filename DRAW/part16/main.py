

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(2)
t.pensize(2)

h = 2

for mi in range(200):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(warna)
    for me in range(2):
        t.fd(mi)
        t.lt(60)
        t.rt(120)
    t.rt(240)
    t.lt(51)
    t.circle(3)

t.done()