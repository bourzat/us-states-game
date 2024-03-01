import turtle

import pandas as pd

from score import Score
from states import ShowState

# Initialize screen and score
screen = turtle.Screen()
screen.setup(width=730, height=490)
score = Score()
screen.title("U.S. States Game")

# Set up the background image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load states data
states_data = pd.read_csv("50_states.csv")
states_list = states_data["state"].to_list()

# Keep track of guessed states
states_guessed = []

# Game loop
while len(states_guessed) < 50:
    # Get user input
    answer_state = screen.textinput(title=f"{score.score}/50 Guess the state",
                                    prompt="Write the name of a state below").title()

    # Check if user wants to exit
    if answer_state.lower() == "exit":
        unnamed_states = list(set(states_list).symmetric_difference(states_guessed))
        with open("states_to_learn.csv", "w") as states_to_learn:
            for state in unnamed_states:
                states_to_learn.write(f"{state} \n")
        break

    # Check if the guessed state is correct
    if answer_state in states_list and answer_state not in states_guessed:
        states_guessed.append(answer_state)
        screen.tracer(0)
        ShowState(answer_state)  # Display the state
        score.increase_score()
        screen.tracer(1)

# Keep the window open
screen.mainloop()
