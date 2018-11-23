NUM_MAX = 1_000_000  # 1 million
FOUND_MAX = 10_001  # max primes to find


def sieve_primes():
    primes = [True] * 1_000_000
    primes[0] = False  # 0 is not a prime number
    primes[1] = False  # 1 is not a prime number

    p = 2  # current prime index
    count = 1
    last = time()
    while count < FOUND_MAX and p < NUM_MAX:
        for n in range(p * p - 1, NUM_MAX):
            if primes[n] and n % p == 0:
                primes[n] = False

        p += 1
        if count % 100 == 0:  # report some pro
        for i in range(p, NUM_MAX):
            if primes[i]:
                p = i
                break
        else:
            print("exhausted numbers - no more prime.")
            break  # break while
        count += 1gress
            print(p, count, "%.7f" % (time() - last))
            last = time()

    print(p, count)
    assert primes[p] or count < FOUND_MAX


if __name__ == "__main__":
    from time import time

    begin = time()
    sieve_primes()
    past = time() - begin
    print(f"used {past} secs")
