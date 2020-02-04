year_diff_dict = {
    'Jorden'    : 1,
    'Merkur'    : 0.2408467,
    'Venus'     : 0.61519726,
    'Mars'      : 1.8808158,
    'Jupiter'   : 11.862615,
    'Saturn'    : 29.447498,
    'Uranus'    : 84.016846,
    'Neptun'    : 164.79132
}


def sec_to_earth_years(sec):
    """sec/year = 60*60*24*365.25-ish)."""
    return sec/31557600


def from_earth_years(planet, earth_years):
    return earth_years * year_diff_dict[planet]


def print_all(sec):
    result_dict = {}
    for key in year_diff_dict:
        result = from_earth_years(key, sec_to_earth_years(sec))
        result_dict.update({key : result})
        print(key, '\t', end='')
        print(result)
    return result_dict
