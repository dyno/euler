from euler.primes import naive, erat2, erat2a, psieve, erat3
from itertools import islice


PRIMES_TWENTY = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


def test_naive():
    primes = naive
    assert list(islice(primes(), 20)) == PRIMES_TWENTY


def test_erat2():
    primes = erat2
    assert list(islice(primes(), 20)) == PRIMES_TWENTY


def test_erat2a():
    primes = erat2a
    assert list(islice(primes(), 20)) == PRIMES_TWENTY


def test_psieve():
    primes = psieve
    assert list(islice(primes(), 20)) == PRIMES_TWENTY


def test_erat3():
    primes = erat3
    assert list(islice(primes(), 20)) == PRIMES_TWENTY
