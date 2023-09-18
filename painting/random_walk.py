from turtle import Turtle,Screen
import random
t=Turtle()

c=['dark slate gray','yellow','tomato','purple','red','black']

t.width(5)
t.speed(15)
l=[0,90,180,270,360]



for i in range(500):
    t.color(random.choice(c))
    t.forward(10)
    t.setheading(random.choice(l))
s=Screen()
s.exitonclick()