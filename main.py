import turtle
import pandas

csv_name = "50_states.csv"
data = pandas.read_csv(csv_name)

screen = turtle.Screen()
screen.setup(height=491,width=725)
image = "blank_states_img.gif"

# Step 1: You're adding a shape to the existing screen shapes (turtle,square,circle) & then you're using this shape
screen.addshape(image)

# Step 2: You're using the previous gif that you added as a shape in this turtle method.
turtle.shape(image)

# Step 3: How to get coordinates of each states on screen? Use the code below:
# Code:
# "def get_on_screen_coor(x, y):
#     print(x, y)
# screen.onscreenclick(get_on_screen_coor)
# turtle.mainloop()"

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = turtle.textinput(f"{len(guessed_states)}/50 Guess another state",
                              "What's another state name?").title()

    state_data = data[data.state == answer]
    if answer == "Exit":
        states_left = []
        for state in all_states:
            if state not in guessed_states:
                states_left.append(state)
        states_dict = pandas.DataFrame(states_left)
        states_dict.to_csv("states_not_guessed.csv")
        break
    if answer in all_states:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        x_cor = state_data.x.iloc[0]
        y_cor = state_data.y.iloc[0]
        pen.goto(x_cor, y_cor)
        pen.write(answer, font=("Calibre", 8, "normal"))
        guessed_states.append(answer)
