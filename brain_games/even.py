from random import randint
import prompt


def even_game(user_name):
    '''EVEN GAME: Answer "yes" if the number is even, otherwise answer "no".'''

    print('Answer "yes" if the number is even, otherwise answer "no".')

    attempts = 3
    while attempts > 0:
        the_number = randint(1, 99)
        print(f'Question: {the_number}')
        user_answer = prompt.string('Your answer: ')
        if the_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if (user_answer == correct_answer):
            print('Correct!')
            attempts -= 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            return None

    print(f'Congratulations, {user_name}!')
