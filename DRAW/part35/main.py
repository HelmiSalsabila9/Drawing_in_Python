

# SKUYMI [helmisalsabila.com]

from turtle import *
import colorsys as c 

bgcolor('black')
tracer(5)

def gambar():
    h = 0.08
    n = 145
    for mi in range(290):
        warna = c.hsv_to_rgb(h,1,1)
        h += 1/n
        up()
        goto(0,0)
        down()
        color(warna)
        pensize(2)
        fd(mi)
        circle(mi/1.5, 100)
        begin_fill()
        circle(mi/3, 100)
        end_fill()

gambar()
done()