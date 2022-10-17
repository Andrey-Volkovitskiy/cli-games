import prompt


def welcome_user():
    '''Greet a user and ask for his name

    Arguments:
        None

    Returns:
        user_name

    '''
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name
