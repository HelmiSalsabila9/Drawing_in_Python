

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.width(2)
t.speed(0)

for mi in range(700):
    t.color(c.hsv_to_rgb(mi/255,1,1))
    t.forward(mi)
    t.left(58)

t.hideturtle()
t.done()