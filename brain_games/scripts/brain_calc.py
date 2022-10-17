#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import play_game
from brain_games.games.calc import generate_calc

GAME_NAME = "What is the result of the expression?"


def main():
    user_name = greet_user(GAME_NAME)
    questions_and_answers = generate_calc()
    play_game(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
