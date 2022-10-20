from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 99


def generate(num_of_game_rounds):
    '''Generates list of tuples with questions and correct answers
    for Brain Even game.'''

    q_a_list = list()
    rounds_left = num_of_game_rounds
    while rounds_left > 0:
        number = randint(MIN_NUMBER, MAX_NUMBER)
        question = str(number)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        q_a_list.append((question, correct_answer))
        rounds_left -= 1

    return q_a_list
