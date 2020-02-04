from .hangman import Game
from .API import API

api = API()
word = API.get_word()

game = Hangman(api)

while not game.done():
    user_input = input('Input letter or word: ')
    game.guess(user_input)
