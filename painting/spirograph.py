from turtle import Turtle,Screen
import random
t=Turtle()

c=['dark slate gray','yellow','tomato','purple','red','black']


t.speed(15)
def spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        t.color(random.choice(c))
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)
spirograph(5)

s=Screen()

s.exitonclick()