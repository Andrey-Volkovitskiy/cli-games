#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import game_engine
from brain_games.games.prime import prime_generator


def main():
    user_name = greet_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    questions_and_answers = prime_generator()
    game_engine(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
