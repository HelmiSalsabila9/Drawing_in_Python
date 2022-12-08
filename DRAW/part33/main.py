

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(10)
t = t.Turtle()
t.pensize(3)

h = 0

def me(set_me,r):
    t.seth(set_me)
    t.circle(200-r, 120)
    t.seth(set_me + 180)
    t.circle(200-r, 120)

for mi in range(20):
    warna = c.hsv_to_rgb(h,1,1)
    t.pencolor(warna)
    for mo in range(30):
        me(mi*30, 30+mo)
    
    h += 0.1

t.done()