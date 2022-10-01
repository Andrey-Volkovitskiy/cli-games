from random import randint


def even_generator():
    result = list()
    num_of_game_rounds = 3
    while num_of_game_rounds > 0:
        the_number = randint(1, 99)
        question = str(the_number)

        if the_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        result.append((question, correct_answer))
        num_of_game_rounds -= 1

    return result
