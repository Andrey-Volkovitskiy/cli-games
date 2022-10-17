#!/usr/bin/env python3
from brain_games.scripts import start
from brain_games.games.progression import generate_progression

GAME_NAME = "What number is missing in the progression?"


def main():
    start(GAME_NAME, generate_progression)


if __name__ == '__main__':
    main()
