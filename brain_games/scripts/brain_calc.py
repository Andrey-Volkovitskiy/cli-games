#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import game_engine
from brain_games.games.calc import calc_generator


def main():
    user_name = greet_user()
    print("What is the result of the expression?")
    questions_and_answers = calc_generator()
    game_engine(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
