

# SKUYMI ['helmisalsabila.com']

import turtle as t 
import colorsys as c 

t.bgcolor('black')
t.tracer(5)
t.pensize(7)
t.goto(0, -250)

warna = ['red', 'yellow', 'green', 'blue']
t.rt(2)

for mi in range(300):
    t.color(warna[mi%4])
    t.up()
    t.circle(300-mi, 30)
    t.up()
    t.circle(300-mi, 60)
    t.down()
    t.circle(300-mi, 180)

t.done()