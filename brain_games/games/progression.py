from random import randint, choice
from brain_games import NUM_OF_GAME_ROUNDS

PROGRESSION_LEN = 10


def get_progression(progression_start, progression_step, progression_len):
    progression = [progression_start]
    for i in range(progression_len - 1):
        progression.append(progression[i] + progression_step)
    return progression


def get_question(progression, correct_answer):
    progression_str = map(str, progression)
    question = " ".join(progression_str)
    return question.replace(str(correct_answer), "..", 1)


def generate_progression():
    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        progression_start = randint(0, 20)
        progression_step = randint(1, 5)
        progression = get_progression(progression_start, progression_step,
                                      PROGRESSION_LEN)

        correct_answer = choice(progression[2:-2])
        question = (get_question(progression, correct_answer))
        q_a_list.append((question, str(correct_answer)))
        rounds_left -= 1

    return q_a_list
