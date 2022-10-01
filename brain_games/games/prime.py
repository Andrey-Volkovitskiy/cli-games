from random import randint


def is_prime(the_number):
    result = 'yes'
    for i in range(2, the_number // 2):
        if the_number % i == 0:
            result = 'no'
            break
    return result


def prime_generator():
    q_a_list = list()
    num_of_game_rounds = 3
    while num_of_game_rounds > 0:
        the_number = randint(2, 99)
        correct_answer = is_prime(the_number)
        question = str(the_number)
        q_a_list.append((question, correct_answer))
        num_of_game_rounds -= 1

    return q_a_list
