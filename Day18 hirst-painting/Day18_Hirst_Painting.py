# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('Day18_image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r, g, b)
#     rgb_colors.append(new_tuple)
#
# print(rgb_colors)

import random
import turtle as turtle_module

tim = turtle_module.Turtle()
tim.speed("fastest")
# Extracted by printing the colours in picture
# color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

colours = ["Gainsboro", "DarkGray", "DimGray", "Black", "SlateGray", "CornflowerBlue", "Blue", "MidnightBlue", "Cyan",  "LightSeaGreen", "DarkSlateGray", "MediumSeaGreen", "SpringGreen", "DarkGreen", "Chartreuse", "OliveDrab", "Olive", "Yellow", "DarkRed", "Orange", "DarkSlateBlue", "Magenta", "Purple", "Red", "IndianRed", "MediumVioletRed", "Salmon", "DarkRed", "Indigo", "Plum"]

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for j in range(10):
    for i in range(10):

        tim.dot(20, random.choice(colours))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

