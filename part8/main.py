
# SKUYMI [helmisalsabila.com]

import turtle

turtle.bgcolor('black')

a = turtle.Turtle()

def style():
    for mi in range(200):
        a.pensize(20)
        a.right(1)
        a.forward(1)

def love():
    a.pensize(20)
    a.fillcolor('red')
    a.pencolor('red')
    
    a.begin_fill()
    a.left(140)
    a.forward(113)
    
    style()
    a.left(120)
    
    style()
    a.forward(112)
    
    a.end_fill

love()