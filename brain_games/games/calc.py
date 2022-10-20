from random import randint, choice
import operator

TASK = "What is the result of the expression?"
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}
MIN_NUMBER = 1
MAX_NUMBER = 10


def generate(num_of_game_rounds):
    '''Generates list of tuples with questions and correct answers
    for Brain Calc game.'''

    q_a_list = list()
    rounds_left = num_of_game_rounds
    while rounds_left > 0:
        first_number = randint(MIN_NUMBER, MAX_NUMBER)
        second_number = randint(MIN_NUMBER, MAX_NUMBER)
        math_operation = choice(list(OPERATORS.keys()))

        question = f'{first_number} {math_operation} {second_number}'
        correct_answer = OPERATORS[math_operation](first_number, second_number)

        q_a_list.append((question, str(correct_answer)))
        rounds_left -= 1

    return q_a_list
