

# SKUYMI [helmisalsabila.com]

import turtle as t 
import colorsys as c 
import random as r 

hels = t.Screen()
hels.tracer(1000)
hels.setup(1000,1000)

t.bgcolor('black')
t.hideturtle()

n = 250

main = []
for mi in range(n):
    main.append(t.Turtle())


h = 0.04
for mi in range(n):
    warna = c.hsv_to_rgb(h,1,1)
    h += 1/n
    main[mi].color(warna)
    main[mi].up()
    main[mi].goto(r.uniform(-500,500), r.uniform(-500,500))
    main[n-1].goto(0,0)
    main[n-1].shape('circle')
    main[n-1].shapesize(1)

def sat():
    for mi in range(n-1):
        akhir = main[mi].towards(main[mi+1])
        main[mi].seth(akhir)
    main[n-1].left(5)
    main[n-1].fd(20)
    for mi in range(n-1):
        main[mi].fd(10)
    hels.update()
    hels.ontimer(sat, 1000//20)

sat()
t.done()






















































