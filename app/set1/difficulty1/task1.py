"""Rain drop sounds, with keys corresponding
to the factors."""
rain_results = {
    3 : 'Pling',
    5 : 'Plang',
    7 : 'Plong'
}


def has_factor(a, b):
    """Returns True if a is divisible by b,
    meaning b is a factor of a."""
    return a%b == 0


def get_str_output(num):
    """Returns a string based on the factors of num."""
    return_string = ''
    for key in rain_results:
        if has_factor(num, key):
            return_string += rain_results[key]
    return return_string
