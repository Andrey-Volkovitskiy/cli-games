import prompt


def greet_user(game_name):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game_name)
    return user_name
