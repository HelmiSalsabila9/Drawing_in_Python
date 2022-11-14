

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(100)

def draw():
    h = 25
    s = 98
    for mi in range(300):
        warna = c.hsv_to_rgb(h,1,1)
        h += 1/s
        t.color(warna)
        t.pensize(3)
        t.fillcolor('black')
        t.begin_fill()
        t.circle(mi, 43)
        t.rt(20)
        t.bk(45)
        t.up()
        t.goto(7, 56)
        t.down()
        t.circle(mi, 23)
        t.end_fill()
        t.circle(mi, 90)

draw()
t.done()