from Tools import numpy_sieve
N = 10**10
l10 = numpy_sieve(N)


def q(p, n):
    return min(n//p, p)


s = 0
for prime in l10:
    s += q(prime, N)
print(N-s)  # sol = 2811077773
