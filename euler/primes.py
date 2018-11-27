#!/usr/bin/env python3

from itertools import compress, count, cycle, islice


def naive():
    prime = 2  # first prime
    yield prime
    primes = [prime]
    for x in count(3, 2):  # odd numbers start from 3
        if not any(x % prime == 0 for prime in primes):
            yield x
            primes.append(x)


def erat2():
    D = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
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
    witness = {}
    yield 2
    for q in islice(count(3), 0, None, 2):
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
    yield from (2, 3, 5)

    witness = {9: 3, 25: 5}  # map composite integers to primes witnessing their compositeness
    for q in compress(islice(count(7), 0, None, 2), cycle(MASK)):
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
    yield from (2, 3, 5, 7)
    witness = {}  # composite and its witness
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p * p
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

# Reference:
# https://rosettacode.org/wiki/Extensible_primeserator#Python
# https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/10733621#10733621
# http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
