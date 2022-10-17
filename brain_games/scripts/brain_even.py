#!/usr/bin/env python3
from brain_games.scripts import start
from brain_games.games.even import generate_even

GAME_NAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    start(GAME_NAME, generate_even)


if __name__ == '__main__':
    main()
