import turtle
from turtle import  Turtle, Screen
import  random
is_raceon=False
s=Screen()
s.setup(width=500,height=400)
user_input = s.textinput(title="Make your  Bet",prompt="Which turtle going to win(choose color)?")
colors=["red","orange","yellow","green","blue","indigo","violet"]
k=-100
all_turtles=[]
t=Turtle()
t.penup()
t.goto(230,200)
t.pendown()
t.setheading(270)
t.forward(400)
c=0
for i in colors:
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()


    new_turtle.goto(x=-235, y=k)
    k += 40
    all_turtles.append(new_turtle)
if user_input:
    is_raceon = True
while is_raceon:
    for turtle in all_turtles:

        if turtle.xcor()>=230:
            c+=1
            if c==1:
                is_raceon=False
            win_color=turtle.pencolor()
            if win_color == user_input:
                print(f"You won the race,the turtle of color {win_color} won the race")
            else:
                print(f"You lost the race,the turtle of color {win_color} won the race")
        T_distance = random.randint(0, 10)
        turtle.forward(T_distance)



s.exitonclick()
