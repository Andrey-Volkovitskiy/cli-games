from random import randint, choice


def get_progression(progression_start, progression_step, progression_len):
    progression = [progression_start]
    for i in range(progression_len - 1):
        progression.append(progression[i] + progression_step)
    return progression


def get_question(progression, correct_answer):
    progression_str = map(str, progression)
    question = " ".join(progression_str)
    return question.replace(str(correct_answer), "..", 1)


def progression_generator():
    q_a_list = list()
    num_of_game_rounds = 3
    progression_len = 10
    while num_of_game_rounds > 0:
        progression_start = randint(0, 20)
        progression_step = randint(1, 5)
        progression = get_progression(progression_start, progression_step,
                                      progression_len)

        correct_answer = choice(progression[2:-2])
        question = (get_question(progression, correct_answer))
        q_a_list.append((question, str(correct_answer)))
        num_of_game_rounds -= 1

    return q_a_list
