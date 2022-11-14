
# SKUYMI [helmisalsabila.com]

from turtle import *

bgcolor('black')

colormode(255)
red = (234, 68, 53);
yellow = (255, 189, 0);
green = (0, 172, 71);
blue = (66, 133, 244);
h = 150
seth(-150)
up()

# RED
color(red)
begin_fill()
fd(h)
down()
right(90)
circle(-h, 120)
fd(h*3**.5)
left(120)
circle(2*h, 120)
left(60)
fd(h*3**.5)
end_fill()

# GREEN
left(180)
color(green)
begin_fill()
fd(h*3**.5)
left(120)
circle(2*h, 120)
left(60)
fd(h*3**.5)
left(180)
circle(-h, 120)
end_fill()

# YELLOW
left(180)
circle(h, 120)
color(yellow)
begin_fill()
circle(h, 120)
right(180)
fd(h*3**.5)
right(60)
circle(-2*h, 120)
right(120)
fd(h*3**.5)
end_fill()

# BLUE
up()
left(98)
fd(15)
seth(60)
color(blue)
down()
begin_fill()
circle(distance(1, 0))
end_fill()
ht()

done()

