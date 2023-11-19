from turtle import Turtle, Screen
import random
screen = Screen()
y_axis = -100
is_race_on = False


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "green", "black", "blue", "purple"]
positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=positions[turtle_index])
    all_turtles.append(new_turtle)
print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtlee in all_turtles:
        if turtlee.xcor() > 220:
            winning_color = turtlee.pencolor()
            if winning_color == user_bet:
                print("You've won the bet!")
            else:
                print(f"You lost, {winning_color} turtle is the winner of the race!")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtlee.forward(rand_distance)

screen.exitonclick()
