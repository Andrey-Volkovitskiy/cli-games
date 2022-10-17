from brain_games.greet import greet_user
from brain_games.engine import play_game


def start(GAME_NAME, game_generator):
    '''Stars all games

    Arguments:
        GAME_NAME - the name of the current game.
        game_generator - function for generating questions and
        correct answers for the current game.

    Returns:
        None'''
    user_name = greet_user(GAME_NAME)
    questions_and_answers = game_generator()
    play_game(user_name, questions_and_answers)
