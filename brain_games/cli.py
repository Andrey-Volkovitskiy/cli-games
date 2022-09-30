import prompt


def welcome_user():
    user_name = prompt.string('May I have you name? ')
    print(f'Hello, {user_name}!')
