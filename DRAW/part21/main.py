

# SKUYMI [helmisalsabila.com]

import turtle as t
import colorsys as c 

t.bgcolor('black')
t.tracer(3)
t.width(3)

h = 25

for mi in range(250):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(warna)
    t.up()
    t.goto(0,0)
    t.fd(mi-1)
    t.down()
    t.circle(mi, 100)
    t.lt(45)

t.done()