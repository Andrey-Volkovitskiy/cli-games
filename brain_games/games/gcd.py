from random import randint
from math import gcd

TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 50


def generate(num_of_game_rounds):
    '''Generates list of tuples with questions and correct answers
    for Brain GCD game.'''

    q_a_list = list()
    rounds_left = num_of_game_rounds
    while rounds_left > 0:
        first_number = randint(MIN_NUMBER, MAX_NUMBER)
        second_number = randint(MIN_NUMBER, MAX_NUMBER)

        question = f'{first_number} {second_number}'
        correct_answer = gcd(first_number, second_number)

        q_a_list.append((question, str(correct_answer)))
        rounds_left -= 1

    return q_a_list
