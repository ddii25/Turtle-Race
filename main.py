import random
from turtle import Turtle, Screen


# turtle race

# create  turtles and each one has a different color  (function)

# once the turtles are on the screen and placed on their starting line ask the user which one they think it will win

# each turtle has different speed

# start the race

# once the winner turtle reaches the screen stop the game
# display a message to the user 'Your turtle won' or 'Your turtle lost'

screen = Screen()
screen.title("Turtle Race")
colors = ["blue", "red", "yellow", "pink", "green", "purple"]

def get_turtles(colors:list):
    """Returns as many turtls as colors in the list"""
    turtles = []
    for i in range(len(colors)):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        turtles.append(new_turtle)
    return turtles


racing_turtles = get_turtles(colors=colors)
x = -400
y = -100

text = Turtle()
text.hideturtle()
text.penup()

for turtle in racing_turtles:
    turtle.setx(x)
    turtle.sety(y)
    y += 50

try:
    user_bet = screen.textinput(title="Bet", prompt="Which turtle will win?").lower()
except AttributeError:
    user_bet = ""

is_true = True

while is_true:
    for turtle in racing_turtles:
        if turtle.xcor() > screen.canvwidth:
            is_true = False
            if turtle.color()[0] == user_bet:
                text.write("YOU WON :)")
            else:
                text.write("YOU LOST :(\n"
                           f"{turtle.color()[0]} won")
            break
        turtle.forward(random.randint(5, 20))



screen.exitonclick()