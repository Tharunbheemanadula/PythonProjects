
from turtle import Turtle, Screen

import pandas as pd
screen = Screen()
screen.title('USA States Game')
image= 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_state_list = data.state.to_list()
for state in all_state_list:
    state=state.lower()

guess_states=[]

while len(guess_states)<=50:
    answer = screen.textinput(prompt="Guess USA States...?", title=f"{len(guess_states)}/50USA States").title()

    if answer in all_state_list:
        guess_states.append(answer)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == answer]
        new_turtle.goto(int(state_data.x),int(state_data.y))
        new_turtle.write(arg=answer)

    elif answer == "Exit":
        learn_states = []
        for state in all_state_list:
            if state not in guess_states:
                learn_states.append(state)
        df=pd.DataFrame(learn_states)
        df.to_csv("to_be_learn_states.csv")


        break

    else:
        pass



screen.exitonclick()
