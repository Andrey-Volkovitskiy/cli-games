from random import randint
from brain_games import NUM_OF_GAME_ROUNDS


def is_prime(the_number):
    result = 'yes'
    for i in range(2, the_number // 2):
        if the_number % i == 0:
            result = 'no'
            break
    return result


def generate_prime():
    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        the_number = randint(2, 99)
        correct_answer = is_prime(the_number)
        question = str(the_number)
        q_a_list.append((question, correct_answer))
        rounds_left -= 1

    return q_a_list
