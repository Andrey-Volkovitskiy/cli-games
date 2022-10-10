import prompt


def play_game(user_name, questions_and_answers):
    num_of_game_rounds = len(questions_and_answers)
    for i in range(num_of_game_rounds):
        (question, correct_answer) = questions_and_answers[i]
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}")
            return None

    print(f'Congratulations, {user_name}!')
