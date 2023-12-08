import turtle
import pandas

screen = turtle.Screen()
screen.title("U. S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)
#
# turtle.mainloop()
#

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What is another states name?")
    answer_state = answer_state.title()
    # if answer is in one of the state in 50_states_csv
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        tom = turtle.Turtle()
        tom.hideturtle()
        tom.penup()
        states_data = data[data["state"] == answer_state]
        tom.goto(int(states_data.x), int(states_data.y))
        tom.write(states_data.state.item())
