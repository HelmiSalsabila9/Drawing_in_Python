

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(30)
t.pensize(3)

h = 0
n = 90
for mi in range(510):
    warna = c.hsv_to_rgb(h,1,1)
    h += 1/n
    t.color(warna)
    t.up()
    t.goto(0,0)
    t.down()
    t.bk(mi)
    t.fillcolor(warna)
    t.begin_fill()
    t.circle(90, 100)
    t.end_fill()
    t.lt(189)

t.done()