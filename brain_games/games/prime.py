from random import randint
from brain_games import NUM_OF_GAME_ROUNDS

MIN_NUMBER = 2
MAX_NUMBER = 99


def is_prime(number):
    '''Returns "yes" if the number is prime
    and "no" if the number is't prime.'''

    result = 'yes'
    for i in range(2, number // 2):
        if number % i == 0:
            result = 'no'
            break
    return result


def generate_prime():
    '''Generates list of tuples with questions and correct answers
    for Brain Prime game.'''

    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        number = randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = is_prime(number)
        question = str(number)
        q_a_list.append((question, correct_answer))
        rounds_left -= 1

    return q_a_list
