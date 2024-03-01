from turtle import Turtle, Screen
import pandas as pd

states_data = pd.read_csv("50_states.csv")


class ShowState(Turtle):

    def __init__(self, state):
        super().__init__()
        self.hideturtle()
        self.state = state
        self.display_state()

    def state_cor(self):
        global states_data
        """Takes the state the user guessed and gives out co-ordinates of the state in a tuple"""
        x_series = states_data[states_data["state"] == self.state]["x"]
        y_series = states_data[states_data["state"] == self.state]["y"]
        x = float(x_series.iloc[0])
        y = float(y_series.iloc[0])
        co_ordinates = (x, y)
        return co_ordinates

    def display_state(self):
        """Takes the co-ordinates from state_cor and displays the state on the screen"""
        self.penup()
        self.goto(self.state_cor())
        self.write(f"{self.state}", align="center", font=('Arial', 12, "normal"))

    def player_wins(self):
        self.penup()
        self.goto(self.state_cor())
        self.write("YOU WON! :)", align="center", font=('Arial', 12, "normal"))
