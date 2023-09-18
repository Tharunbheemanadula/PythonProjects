# import colorgram
# colors=colorgram.extract('download.jpeg',15)
# colors_list=[]
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     n=(r,g,b)
#     colors_list.append(n)
# print(colors_list)
import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
t=Turtle()
colors=[(235, 220, 200), (208, 160, 108), (210, 232, 218), (129, 165, 190), (236, 213, 223), (47, 110, 147),
        (199, 139, 159), (130, 181, 157), (206, 220, 231), (223, 202, 128), (149, 67, 94), (186, 160, 34),
        (158, 84, 50), (42, 129, 95), (192, 89, 113)]
t.penup()
t.hideturtle()
t.speed('fast')
t.setheading(225)
t.forward(250)
t.setheading(0)
number_of_dots=100
for dots in range(1,number_of_dots+1):
    t.dot(20,random.choice(colors))
    t.forward(50)

    if dots %10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


s=Screen()
s.exitonclick()