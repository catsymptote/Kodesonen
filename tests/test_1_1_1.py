from app.set1.difficulty1.task1 import *

def test_has_factor():
    result1 = has_factor(6, 3)
    result2 = has_factor(128, 2)
    result3 = has_factor(127, 3)

    assert type(result1) is type(result2) is type(result3) is bool
    
    assert result1
    assert result2
    assert not result3


def test_get_str_output():
    result = get_str_output(3)
    assert result is not None
    assert type(result) is str
    
    assert get_str_output(1) == ''
    assert get_str_output(2) == ''
    assert get_str_output(3) == 'Pling'
    assert get_str_output(4) == ''
    assert get_str_output(5) == 'Plang'
    assert get_str_output(6) == 'Pling'
    assert get_str_output(7) == 'Plong'
    assert get_str_output(8) == ''
    assert get_str_output(9) == 'Pling'
    assert get_str_output(15) == 'PlingPlang'
    assert get_str_output(21) == 'PlingPlong'
    assert get_str_output(35) == 'PlangPlong'
    assert get_str_output(105) == 'PlingPlangPlong'
