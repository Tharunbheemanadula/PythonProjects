from turtle import Turtle, Screen
t=Turtle()

import random


c=['dark slate gray','yellow','tomato','purple','red','black']
def shapes(num_sides):
    angle=360//num_sides
    for  i in range(num_sides):
        t.forward(100)
        t.right(angle)
for i in range(3,11):
    t.color(random.choice(c))
    shapes(i)
s=Screen()
s.exitonclick()