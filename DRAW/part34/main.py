

# SKUYMI [helmisalsabila.com]

import turtle  as t 
t = t.Turtle()
t.screen.bgcolor('black')
t.speed(1)

def buled(lingkaran, warna):
    t.color(warna)
    t.begin_fill()
    t.circle(lingkaran)
    t.end_fill()

t.penup()
t.goto(0-30, -280)
t.pendown()

buled(250, 'red')
t.goto(-30, -240)
buled(210, 'white')
t.goto(-30, -200)
buled(170, 'red')
t.goto(-30, -160)
buled(130, 'blue')
t.goto(-153, 11)

t.begin_fill()
t.color('white')
for mi in range(5):
    t.forward(245)
    t.right(144)

t.end_fill()
t.hideturtle()
t.done()