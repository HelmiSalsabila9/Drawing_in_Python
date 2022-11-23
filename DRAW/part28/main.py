

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(50)
t.pensize(3)

def gambar():
    h = 255
    n = 250
    t.up()
    t.goto(159, -10)
    t.down()
    for mi in range(590):
        warna = c.hsv_to_rgb(h,1,1)
        h += 1/n
        t.color('black')
        t.fillcolor(warna)
        t.begin_fill()
        t.rt(46.51)
        t.fd(mi)
        t.circle(-25, 180)
        t.end_fill()
        t.circle(mi, 21, steps=5)
        t.fd(269)

gambar()
t.done()