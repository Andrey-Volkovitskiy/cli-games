#!/usr/bin/env python3
from brain_games.scripts import start
from brain_games.games.calc import generate_calc

GAME_NAME = "What is the result of the expression?"


def main():
    start(GAME_NAME, generate_calc)


if __name__ == '__main__':
    main()
