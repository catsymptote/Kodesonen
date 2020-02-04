from app.set1.difficulty2.hangman import Hangman
from app.set1.difficulty2.API import API


def test_init():
    api = API()
    game = Hangman(api)


def test_get_word_from_API():
    game = Hangman(API())
    game.word = 'NOTPYTHON' # Fix when API is up.
    first_word = game.word
    game.get_word_from_API()
    
    assert first_word is not None
    assert game.word is not None
    assert first_word != game.word


def test_add_mistake():
    game = Hangman(API())
    assert game.mistakes == 0
    game.mistakes += 2
    assert game.mistakes == 2
    game.guess_word('WRONGWORD')
    assert game.mistakes == 5
    game.guess_letter('|')
    assert game.mistakes == 6


def test_guess():
    game = Hangman(API())
    pass


def test_guess_letter():
    game = Hangman(API())
    pass


def test_guess_word():
    game = Hangman(API())
    pass


def test_show():
    game = Hangman(API())
    game.word = ['P', 'Y', 'T', 'H', 'O', 'N']
    game.found_letters = ['_', '_', '_', '_', '_', '_']
    assert game.show() == ['_', '_', '_', '_', '_', '_']

    game.guess('Y')
    assert game.show() == ['_', 'Y', '_', '_', '_', '_']

    game.guess('T')
    assert game.show() == ['_', 'Y', 'T', '_', '_', '_']


def test_done():
    game = Hangman(API())
    pass
