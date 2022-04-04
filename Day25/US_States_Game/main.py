from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S States Games")

image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

# def get_mouse_on_click(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_on_click)
FONT = ("Courrier", 10, "normal")
correct_guesses = []
score = 0


def draw_state(state):
    state_drawer = Turtle()
    state_drawer.penup()
    state_drawer.hideturtle()
    state_location = state_data[state_data.state == state]
    state_pos_x = int(state_location.x)
    state_pos_y = int(state_location.y)
    # Could also do it this way
    # state_pos_x = state_data[state_data.state == state].x.item()
    # state_pos_y = state_data[state_data.state == state].y.item()
    state_drawer.setposition(state_pos_x, state_pos_y)
    state_drawer.write(state, align="center", font=FONT)


def add_score(correct_state):
    correct_guesses.append(correct_state)
    return score


state_data = pandas.read_csv("50_states.csv")

while True and (len(correct_guesses) != len(state_data.state)):
    user_guess = screen.textinput(title="Guess the state", prompt="What is the name of a U.S State? ").title()

    if user_guess == "Exit":
        break

    if user_guess in state_data.state.values:
        if user_guess in correct_guesses:
            print("You already guessed this one correctly!")
        else:
            draw_state(user_guess)
            score = add_score(user_guess)
            print(f"Score: {len(correct_guesses)} out of {len(state_data.state)}")
    else:
        print("Sorry, but no.")

    if len(correct_guesses) == len(state_data.state):
        print("You win!")

# On Exit, print the missed guesses to a csv
missed_guesses = [state for state in state_data.state.values if state not in correct_guesses]
# for state in state_data.state.values:
#     if state not in correct_guesses:
#         missed_guesses.append(state)

missed_guesses_df = pandas.DataFrame(missed_guesses, columns=["State"])
missed_guesses_df.to_csv("states_to_learn.csv")

screen.exitonclick()
