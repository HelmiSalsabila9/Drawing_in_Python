# SKUYMI (helmisalsabila.com)

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(1000)
t.pensize(2)

h = 0

t.penup()
t.goto(-150,-300)
t.down()
t.left(100)
t.forward(250)

for i in range(500):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.1
    t.pencolor(warna)
    t.left(i)
    t.fd(3)
    t.fd(5)
    t.write('SKUYMI', font=('Quicksand', 100, 'bold'))

t.done()