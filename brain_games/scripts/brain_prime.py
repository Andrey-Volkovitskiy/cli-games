#!/usr/bin/env python3
from brain_games.scripts import start
from brain_games.games.prime import generate_prime

GAME_NAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    start(GAME_NAME, generate_prime)


if __name__ == '__main__':
    main()
