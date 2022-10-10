#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import play_game
from brain_games.games.even import generate_even


def main():
    GAME_NAME = 'Answer "yes" if the number is even, otherwise answer "no".'
    user_name = greet_user(GAME_NAME)
    questions_and_answers = generate_even()
    play_game(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
