

# SKUYMI [helmisalsabila.com]

from turtle import *

bgcolor('black')
width(20)
warna = ['#db0f3c', '#50ebe7', '#ffffff']
posisi = [(0,0), (-5,13), (-5,5)]

for (x,y), col in zip(posisi, warna):
    up()
    goto(x,y)
    down()
    color(col)
    left(180)
    circle(50, 270)
    forward(160)
    left(180)
    circle(50, 90)