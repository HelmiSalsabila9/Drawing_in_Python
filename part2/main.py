

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(100)

h = 0

def gambar(asli, n):
    t.circle(50+n, 30)
    t.left(asli)
    t.circle(50+n, 60)

t.pensize(4)
t.goto(-20, 0)

for mi in range(500):
    warna = c.hsv_to_rgb(h,1,1)
    h += 0.1
    t.pencolor(warna)
    gambar(90, mi)
    gambar(160, mi)
    t.penup()
    gambar(180, mi)
    gambar(90, mi)
    t.down()

t.done()