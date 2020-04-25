from turtle import *

setup(450, 200, 0, 0)
screensize(300, 150)
title("Programa Hexágono")
hideturtle()

pensize(5)
fillcolor("red")
begin_fill()
for i in range(6):
    forward(100)
    right(60)
end_fill()
