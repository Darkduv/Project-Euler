# %% Problem 717

from Tools import numpy_sieve


target = 10 ** 7

primes = numpy_sieve(target)


def g(p):
    x = pow(2, (pow(2, p, p - 1) - p) % (p - 1), p)
    return ((pow(2, p, p ** 2) * x) % p ** 2) // p


def sum_g():
    s = 0
    for p in primes:
        s += g(p)
    return s


print("Answer: ", sum_g())  # sol = 1603036763131
