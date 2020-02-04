from app.set1.difficulty1.task2 import *


def test_get_letter_value():
    assert get_letter_value('A') == 1
    assert get_letter_value('Q') == 10
    assert get_letter_value('a') == 1

    #assert get_letter_value('Æ') == 0
    #assert get_letter_value('2') == 0
    #assert get_letter_value(2) == 0


def test_get_score():
    assert get_score('Python') == 14
    assert get_score('B') == 3
    assert get_score('ZZZ') == 30
