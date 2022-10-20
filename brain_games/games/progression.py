from random import randint, choice
from brain_games import NUM_OF_GAME_ROUNDS

PROGRESSION_LEN = 10
PROGRESSION_STARTS_FROM_MIN = 0
PROGRESSION_STARTS_FROM_MAX = 20
PROGRESSION_STEP_MIN = 1
PROGRESSION_STEP_MAX = 5


def get_progression(progression_start, progression_step, progression_len):
    '''Returns the linar math prorgession'''
    progression = [progression_start]
    for i in range(progression_len - 1):
        progression.append(progression[i] + progression_step)
    return progression


def get_question(progression, correct_answer):
    '''In progression list replaces correct answer with ".."
    and convert the progression to a string'''
    progression_str = map(str, progression)
    question = " ".join(progression_str)
    return question.replace(str(correct_answer), "..", 1)


def generate_progression():
    '''Generates list of tuples with questions and correct answers
    for Brain Progression game.'''

    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        progression_start = randint(PROGRESSION_STARTS_FROM_MIN,
                                    PROGRESSION_STARTS_FROM_MAX)
        progression_step = randint(PROGRESSION_STEP_MIN,
                                   PROGRESSION_STEP_MAX)
        progression = get_progression(progression_start,
                                      progression_step,
                                      PROGRESSION_LEN)

        correct_answer = choice(progression[2:-2])
        question = (get_question(progression, correct_answer))
        q_a_list.append((question, str(correct_answer)))
        rounds_left -= 1

    return q_a_list
