from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
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


def generate(num_of_game_rounds):
    '''Generates list of tuples with questions and correct answers
    for Brain Prime game.'''

    q_a_list = list()
    rounds_left = num_of_game_rounds
    while rounds_left > 0:
        number = randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = is_prime(number)
        question = str(number)
        q_a_list.append((question, correct_answer))
        rounds_left -= 1

    return q_a_list
