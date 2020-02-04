"""Indicated what the different letters are worth."""
value_dict = {
    # 1p
    'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1,
    'U' : 1, 'L' : 1, 'N' : 1, 'R' : 1,
    'S' : 1, 'T' : 1,

    # 2p
    'D' : 2, 'G' : 2,

    # 3p
    'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3,

    # 4p
    'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4,
    'Y' : 4,

    # 5p
    'K' : 5,

    # 8p
    'J' : 8, 'X' : 8,

    # 10p
    'Q' : 10, 'Z' : 10
}


def get_letter_value(letter):
    """Returns the score value of a letter.
    Letters not in the value_dict
    will cause and error."""
    return value_dict[letter.upper()]


def get_score(word):
    """Returns the Scrabble score of a word."""
    score = 0
    for letter in word:
        score += get_letter_value(letter)
    return score
