import os
import turtle
import pandas


data = pandas.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/50_states.csv")
all_states = data["state"].to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 500)
image = os.path.dirname(os.path.abspath(__file__)) + "/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States correct",
        prompt="What's another state's name?",
    )

    if answer_state != None:
        answer_state = answer_state.title()

        if answer_state == "Exit":
            for state in all_states:
                if state in guessed_states:
                    all_states.remove(state)

            data_dict = {"states": all_states}
            data_frame = pandas.DataFrame(data_dict)
            data_frame.to_csv(
                os.path.dirname(os.path.abspath(__file__)) + "/need_to_learn.csv"
            )
            break

        if answer_state in all_states:
            guessed_states.append(answer_state)
            state = data[data["state"] == answer_state]
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(int(state.x), int(state.y))
            t.write(answer_state)
