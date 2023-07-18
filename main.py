from turtle import Turtle, Screen, shape
import pandas as pd

screen = Screen()
screen.title("US State Game")
screen.addshape("blank_states_img.gif")
shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
correct_ans = []
game_is_on = True
count = 0
def ask_input(n):
    answer_state = screen.textinput(title=f"{n}/50 Guess the state", prompt="What's another state-name")
    ans = answer_state.title()
    correct_ans.append(ans)
    return ans

states = data.state.to_list()
def check():
    if ans in states:
        cor = data[data["state"] == ans]
        return int(cor['x']), int(cor['y'])
    else:
        game_is_on = False

def mark(ans):
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(new_x, new_y)
    tim.write(ans)

while game_is_on:
    ans = ask_input(count)
    new_x, new_y = check()
    mark(ans)
    count += 1

screen.exitonclick()
