

# SKUYMI ['helmisalsabila.com']

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(5)
t.pensize(2)
t.up()
t.goto(-250, 150)
t.down()

h = 0

for mi in range(300):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.08
    t.color('gold')
    t.fillcolor(warna)
    t.up()
    t.circle(mi, 125)
    t.down()
    t.begin_fill()
    t.circle(mi-100, 125)
    t.lt(65)
    t.circle(mi-100, 125)
    t.end_fill()

t.done()