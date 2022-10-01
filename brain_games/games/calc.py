from random import randint, choice


def calc_generator():
    result = list()
    num_of_game_rounds = 3
    while num_of_game_rounds > 0:
        first_number = randint(1, 10)
        second_number = randint(1, 10)
        math_operation = choice(['+', '-', '*'])
        
        if math_operation == '+':
            question = f'{first_number} + {second_number}'
            correct_answer = first_number + second_number
        
        if math_operation == '-':
            question = f'{first_number} - {second_number}'
            correct_answer = first_number - second_number

        if math_operation == '*':
            question = f'{first_number} * {second_number}'
            correct_answer = first_number * second_number

        result.append((question, str(correct_answer)))
        num_of_game_rounds -= 1

    return result