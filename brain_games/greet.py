import prompt


def greet_user(the_game_name):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have you name? ')
    print(f'Hello, {user_name}!')
    print(the_game_name)
    return user_name
