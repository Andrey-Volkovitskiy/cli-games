#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import play_game
from brain_games.games.gcd import generate_gcd


def main():
    GAME_NAME = "Find the greatest common divisor of given numbers."
    user_name = greet_user(GAME_NAME)
    questions_and_answers = generate_gcd()
    play_game(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
