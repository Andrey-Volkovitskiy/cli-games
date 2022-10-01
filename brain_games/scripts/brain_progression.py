#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import game_engine
from brain_games.games.progression import progression_generator


def main():
    user_name = greet_user()
    print("What number is missing in the progression?")
    questions_and_answers = progression_generator()
    game_engine(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
