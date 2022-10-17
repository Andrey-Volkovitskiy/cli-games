#!/usr/bin/env python3
from brain_games.scripts import start
from brain_games.games.gcd import generate_gcd

GAME_NAME = "Find the greatest common divisor of given numbers."


def main():
    start(GAME_NAME, generate_gcd)


if __name__ == '__main__':
    main()
