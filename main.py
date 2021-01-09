# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(type(data))
# # print(type(data["temp"]))
# # data_dict = data.to_dict()
# # print(data_dict)
# data_list = data["temp"].to_list()
# # average_temp = sum(data_list) / len(data_list)
# # print(average_temp)
# #
# # print(data["temp"].mean())
#
# # get max value
# # print(data["temp"].max())
#
#
# # condition
# # print(data["condition"])
# # print(data.condition)
#
# # get data in rows
# # print(data[data.day == ["Monday"])]
# # getting row with maximum temperature
# # print(data[data.temp == data.temp.max()])
# # max_temp_day = data[data.temp == data.temp.max()]
# # print(max_temp_day.condition)
#
# # Creating dataframe fro scratch
#

# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
#
# print(grey_squirrel_count)
# print(red_squirrel_count)
# print(red_squirrel_count)
#
# data_dict = {
#     "For Color": ["Gray", "Red", "Black"],
#     "Count": [grey_squirrel_count, red_squirrel_count, red_squirrel_count]
# }
#
# # convert dict to data frame
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's "
                                                                                             "Name, Enter Exit if "
                                                                                             "give up").title()
    # We have to check if the answer is one of the state from 50 states csv
    if answer_state == "Exit" or answer_state == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()


