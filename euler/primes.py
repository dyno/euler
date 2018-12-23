#!/usr/bin/env python3

from itertools import compress, count, cycle, islice


# ------------------------------------------------------------------------------
def naive():
    """
    >>> list(islice(naive(), 20))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """
    prime = 2  # first prime
    yield prime
    primes = [prime]
    for x in count(3, 2):  # odd numbers start from 3
        if not any(x % prime == 0 for prime in primes):
            yield x
            primes.append(x)


def erat2():
    """
    >>> list(islice(erat2(), 20))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """
    D = {}
    yield 2
    for q in count(3, 2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x & 1):
                x += p
            D[x] = p


def erat2a():
    """
    >>> list(islice(erat2a(), 20))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """

    witness = {}
    yield 2
    for q in count(3, 2):
        p = witness.pop(q, None)
        if p is None:
            witness[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in witness:
                x += 2 * p
            witness[x] = p


MASK = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))


def erat3():
    """
    >>> list(islice(erat3(), 20))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """
    yield from (2, 3, 5)

    witness = {
        9: 3,
        25: 5,
    }  # map composite integers to primes witnessing their compositeness
    for q in compress(count(7, 2), cycle(MASK)):
        p = witness.pop(q, None)
        if p is None:
            witness[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in witness or (x % 30) not in MODULOS:
                x += 2 * p
            witness[x] = p


def psieve():
    """
    >>> list(islice(psieve(), 20))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    """
    yield from (2, 3, 5, 7)
    ps = erat2()
    p = next(ps) and next(ps)
    assert p == 3
    psq = p * p
    witness = {}  # composite and its witness
    for i in count(9, 2):  # odd numbers from psd=3*3 which is 9.
        if i in witness:  # composite
            step = witness.pop(i)
        elif i < psq:  # prime
            yield i
            continue
        else:  # composite, = p*p
            assert i == psq
            step = 2 * p
            p = next(ps)
            psq = p * p

        i += step
        while i in witness:
            i += step
        witness[i] = step


# module exports
primes = erat3

# ------------------------------------------------------------------------------


def factors(n):
    """Return factors of number n.
    >>> list(factors(5))
    [5]
    >>> list(factors(12))
    [2, 2, 3]
    >>> list(factors(140))
    [2, 2, 5, 7]
    """
    for p in primes():
        while n % p == 0:
            yield p
            n //= p
        if n == 1:
            break


def divisors(n):
    """Return the devisors divisors of number.
    >>> list(divisors(12))
    [1, 2, 3, 4, 6, 12]
    >>> list(divisors(1024))
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    """
    r = {1}
    for i in factors(n):
        r |= {e * i for e in r}

    return list(sorted(r))


# Reference:
# https://rosettacode.org/wiki/Extensible_primeserator#Python
# https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/10733621#10733621
# http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
