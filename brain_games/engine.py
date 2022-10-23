import prompt

NUM_OF_GAME_ROUNDS = 3


def greet_user(task):
    '''Greet a user and print current game task

    Arguments:
        task - current game invitation

    Returns:
        user_name, requested from the user

    '''
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    if task is not None:
        print(task)
    return user_name


def play_game(user_name, questions_and_answers):
    '''Implements universal game logic

    Arguments:
        user_name - name reqested from user,
        questions_and_answers - a list of pairs with questions and
        correct answers for current game

    Returns:
        None
    '''
    for i in range(NUM_OF_GAME_ROUNDS):
        (question, correct_answer) = questions_and_answers[i]
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return None
    print(f'Congratulations, {user_name}!')


def start(game):
    '''Stars all games

    Arguments:
        game_name - the name of the game to run

    Returns:
        None
    '''
    user_name = greet_user(game.TASK)
    questions_and_answers = game.generate(NUM_OF_GAME_ROUNDS)
    play_game(user_name, questions_and_answers)
