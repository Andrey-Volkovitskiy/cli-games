import prompt


def greet_user(game_name):
    '''Greet a user and print current game invitation

    Arguments:
        game_name - current game invitation

    Returns:
        user_name, requested from the user

    '''
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_name)
    return user_name
