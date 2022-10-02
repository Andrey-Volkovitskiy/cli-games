from random import randint
from math import gcd
from brain_games import NUM_OF_GAME_ROUNDS


def gcd_generator():
    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        first_number = randint(1, 50)
        second_number = randint(1, 50)

        question = f'{first_number} {second_number}'
        correct_answer = gcd(first_number, second_number)

        q_a_list.append((question, str(correct_answer)))
        rounds_left -= 1

    return q_a_list
