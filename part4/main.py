
# SKUYMI [helmisalsabila.com]

from itertools import count
# from tkinter import E
# from tkinter.tix import TList
import turtle
import random
import math

turtle.bgcolor('black')
turtle.tracer(0)

turtle.setup(1000, 1000)
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()
h = turtle.Turtle()
i = turtle.Turtle()
j = turtle.Turtle()
k = turtle.Turtle()
l = turtle.Turtle()
m = turtle.Turtle()
n = turtle.Turtle()
o = turtle.Turtle()
p = turtle.Turtle()
q = turtle.Turtle()
r = turtle.Turtle()
s = turtle.Turtle()
t = turtle.Turtle()

a.color('brown')
b.color('grey')
c.color('orange')
d.color('green')
e.color('blue')
f.color('salmon')
g.color('red')
h.color('purple')
i.color('yellow')
j.color('white')
k.color('gold')
l.color('dark green')
m.color('maroon')
n.color('lavender')
o.color('beige')
p.color('magenta')
q.color('lime')
r.color('olive')
s.color('spring green')
t.color('light blue')

tlist = []
tlist.append(a)
tlist.append(b)
tlist.append(c)
tlist.append(d)
tlist.append(e)
tlist.append(f)
tlist.append(g)
tlist.append(h)
tlist.append(i)
tlist.append(j)
tlist.append(k)
tlist.append(l)
tlist.append(m)
tlist.append(n)
tlist.append(o)
tlist.append(p)
tlist.append(q)
tlist.append(r)
tlist.append(s)
tlist.append(t)

turtle.speed(50)
turtle.hideturtle()
sum = 0
count = 0
for mi in range(1000):
    for me in range(10000):
        for l in tlist:
            l.seth(random.randrange(0, 350, 90))
            l.fd(10)
        turtle.update()
    for l in tlist:
        sum = math.sqrt(l.xcor()*l.xcor()*l.ycor()*l.ycor())/10*2*math.sqrt(l.xcor()*l.xcor() * l.ycor()*l.ycor())
        count += 1
    for l in tlist:
        l.clear()
        l.up()
        l.goto(0, 0)
        l.down()
    print(sum/count)
