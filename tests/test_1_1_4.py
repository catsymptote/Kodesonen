from app.set1.difficulty1.task4 import *


def test_single_match():
    balance = [3, 4]
    weights = [1, 2, 7, 7]
    assert single_match(balance, weights) == 1

    weights.pop(0)
    assert single_match(balance, weights) == None


def test_double_balance():
    balance = [13, 4]
    assert not double_balance(balance, 2, 3)
    assert double_balance(balance, 3, 6)


def test_double_match():
    balance = [13, 4]
    weights = [1, 2, 3, 6, 14]
    assert double_match(balance, weights) == [3, 6]

    weights.pop(2)
    # [1, 2, 6, 14]
    assert double_match(balance, weights) == None

    weights.append(5)
    # [1, 2, 6, 14, 5]
    assert double_match(balance, weights) == [5, 14]

    weights.pop(-1)
    # [1, 2, 6, 14]
    weights.append(-5)
    # [1, 2, 6, 14, -5]
    assert double_match(balance, weights) == [-5, 14]


def test_balancing():
    # All empty.
    assert balancing([], []) == None

    # No weights.
    assert balancing([1, 2], []) == None

    # Wrong number of sides on the balance.
    assert balancing([1, 2, 3], [4, 5, 6]) == None
    assert balancing([1], [2, 3]) == None

    # No solution.
    assert balancing([1, 2], [3]) == 'Ikke mulig!'

    # Single solution.
    assert balancing([1, 3], [2]) == 2

    # Double solution.
    assert balancing([1, 2], [3, 4]) == [3, 4]

    # Sorting
    assert balancing([1, 2], [4, 3]) == [3, 4]
