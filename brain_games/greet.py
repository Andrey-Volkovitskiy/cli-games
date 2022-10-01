import prompt


def greet_user():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have you name? ')
    print(f'Hello, {user_name}!')
    return user_name
