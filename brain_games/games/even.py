from random import randint


def even_generator():
    q_a_list = list()
    num_of_game_rounds = 3
    while num_of_game_rounds > 0:
        the_number = randint(1, 99)
        question = str(the_number)

        if the_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        q_a_list.append((question, correct_answer))
        num_of_game_rounds -= 1

    return q_a_list
