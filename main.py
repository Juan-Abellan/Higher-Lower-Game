# TODO: IMPORTS
from art import logo, vs
from game_data import data
from random import randint, choice
import os


# TODO: STARTING CONDITIONS

vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


# TODO: FUNCTIONS

def clear():
    """
    Function clearing the screen
    """
    return os.system('clear')

def pick_random():
    """
    Function choosing from data a random dictionary to compare.
    """
    return choice(data)


def compare(_a_choice, _b_choice):
    """
    Function receiving 2 dictionaries and returns the choice with higher number of followers
    """
    return _a_choice if _a_choice["follower_count"] > _b_choice["follower_count"] else _b_choice


def user_choice(_a_choice, _b_choice):
    """"
    Function returning the user´s choice
    """
    print(f"Compare A: {_a_choice['name']}, an {_a_choice['description']}, from {_a_choice['country']}" if
          _a_choice['description'][0]
          in vocals else f"Compare A: {_a_choice['name']}, a {_a_choice['description']}, from {_a_choice['country']}"
                         f"\n{vs}")

    print(f"Against B: {_b_choice['name']}, an {_b_choice['description']}, from {_b_choice['country']}" if
          _b_choice['description'][0]
          in vocals else f"Against B: {_b_choice['name']}, a {_b_choice['description']}, from {_b_choice['country']}")

    guess = (input("Who has more followers? Type 'A' or 'B': ")).lower()
    return _a_choice if guess == "a" else _b_choice


def play_game():
    still_playing = True
    user_points = 0
    print(logo)

    a_choice = pick_random()

    while still_playing:
        b_choice = pick_random()

        if a_choice == b_choice:
            b_choice = pick_random()

        if user_choice(_a_choice=a_choice, _b_choice=b_choice) == compare(_a_choice=a_choice, _b_choice=b_choice):
            user_points += 1
            print(f"Good job! Score: {user_points}")
            a_choice = b_choice
        else:
            still_playing = False
            print(f"Sorry that´s wrong your Final Score: {user_points}\n")


# TODO: TRYING

while input("Do you want to play? 'y' or 'n'? ") == 'y':
    clear()
    play_game()
