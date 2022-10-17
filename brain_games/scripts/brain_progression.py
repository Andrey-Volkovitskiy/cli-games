#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import play_game
from brain_games.games.progression import generate_progression

GAME_NAME = "What number is missing in the progression?"


def main():
    user_name = greet_user(GAME_NAME)
    questions_and_answers = generate_progression()
    play_game(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
