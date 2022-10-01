#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import game_engine
from brain_games.games.even import even_generator


def main():
    user_name = greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions_and_answers = even_generator()
    game_engine(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
