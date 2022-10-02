from random import randint
from brain_games import NUM_OF_GAME_ROUNDS


def even_generator():
    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        the_number = randint(1, 99)
        question = str(the_number)

        if the_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        q_a_list.append((question, correct_answer))
        rounds_left -= 1

    return q_a_list
