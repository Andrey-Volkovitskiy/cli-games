from random import randint
from math import gcd


def gcd_generator():
    result = list()
    num_of_game_rounds = 3
    while num_of_game_rounds > 0:
        first_number = randint(1, 50)
        second_number = randint(1, 50)

        question = f'{first_number} {second_number}'
        correct_answer = gcd(first_number, second_number)

        result.append((question, str(correct_answer)))
        num_of_game_rounds -= 1

    return result
