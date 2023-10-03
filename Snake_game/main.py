import time
from turtle import Screen
from Snake import Snake
from Foood import  Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game 🐍")

# m=0
# for i in range(3):
#     t=Turtle()
#     t.shape('square')


#     t.color('white')
#     t.penup()
#     t.goto(m,0)
#     m+=20
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detection of food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()

        score.increase_score()
#    detection of wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_on = False
        score.game_over()
#     detects collision with body
    for seg in snake.segments[1:]:
        # if seg == snake.head:
        #     pass
        # else:
        if snake.head.distance(seg) < 10:
            is_on = False
            score.game_over()

screen.exitonclick()
