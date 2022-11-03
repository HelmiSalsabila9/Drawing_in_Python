
# SKUYMI [helmisalsabila.com]

import turtle

bintang = turtle.Turtle()
turtle.getscreen().bgcolor('black')

bintang.shape('turtle')
bintang.speed(100)
bintang.color('gold', 'light blue')

def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for mi in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()
star(bintang, 360)
turtle.mainloop