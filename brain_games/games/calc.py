from random import randint, choice
from brain_games import NUM_OF_GAME_ROUNDS


def generate_calc():
    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        first_number = randint(1, 10)
        second_number = randint(1, 10)
        math_operation = choice(['+', '-', '*'])

        if math_operation == '+':
            question = f'{first_number} + {second_number}'
            correct_answer = first_number + second_number

        elif math_operation == '-':
            question = f'{first_number} - {second_number}'
            correct_answer = first_number - second_number

        elif math_operation == '*':
            question = f'{first_number} * {second_number}'
            correct_answer = first_number * second_number

        q_a_list.append((question, str(correct_answer)))
        rounds_left -= 1

    return q_a_list
