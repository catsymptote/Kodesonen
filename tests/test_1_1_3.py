from app.set1.difficulty1.task3 import *


def test_sec_to_earth_years():
    assert sec_to_earth_years(31557600) == 1

    assert sec_to_earth_years(31557601) < 1.001
    assert sec_to_earth_years(31557601) > 0.999
    assert int(sec_to_earth_years(31557601)) == 1


def test_from_earth_years():
    assert from_earth_years('Venus', 1) == 0.61519726
    assert from_earth_years('Neptun', 1) == 164.79132
    assert from_earth_years('Neptun', 3.5) == 3.5 * 164.79132


def test_print_all():
    assert print_all(31557600) == {'Jorden': 1.0,'Merkur': 0.2408467, 'Venus': 0.61519726, 'Mars': 1.8808158, 'Jupiter': 11.862615, 'Saturn': 29.447498, 'Uranus': 84.016846, 'Neptun': 164.79132}
    assert print_all(31557600*2) == {
    'Jorden'    : 2 * 1.0,
    'Merkur'    : 2 * 0.2408467,
    'Venus'     : 2 * 0.61519726,
    'Mars'      : 2 * 1.8808158,
    'Jupiter'   : 2 * 11.862615,
    'Saturn'    : 2 * 29.447498,
    'Uranus'    : 2 * 84.016846,
    'Neptun'    : 2 * 164.79132
}
