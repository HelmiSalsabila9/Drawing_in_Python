

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(10)
t.pensize(2)

h = 15

t.up()
t.goto(0,0)
t.down()

for mi in range(340):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.005
    t.color(warna)
    t.up()
    t.fd(mi*2)
    t.down()
    t.circle(mi, -100)
    t.fd(mi)
    t.circle(mi, -100)

t.done()