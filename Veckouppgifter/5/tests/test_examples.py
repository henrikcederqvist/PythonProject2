from examples import add, hypo
from pytest import approx

def test_add_integers():
    expected = 3
    actual = add(1, 2)
    assert actual == expected

def test_add_floats():
    expected = 0.3
    actual = add(0.1, 0.2)
    assert approx(actual) == expected

def test_hypo():
    #testdata: a=5, b=12, c=13
    expected = 13
    actual = hypo(5, 12)
    # obs - hypo returnerar en float
    assert actual == expected