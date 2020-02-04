from app.set1.difficulty2.API import API


def test_init():
    api = API()
    assert api.url == 'https://api.kodesonen.no/?task=hangman'


def test_get_word():
    api = API()
    result = api.get_word()
    assert result is not None
    assert type(result) is str
    assert len(result) > 0
    #assert result == 'PYTHON'   # Remove when connection is up.
