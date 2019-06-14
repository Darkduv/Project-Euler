# %% Problem 501

# if n has 8 divisors n is equal to p^7 or p^3*q^1 or p*q*r  where p, q, r are primes
from Tools import numpy_sieve, binary_search_inf

l_p = numpy_sieve(3*10**4)


def nb1(lim):  # n = p^7 with n <= lim
    a = int(lim ** (1 / 7))
    if (a + 1) ** 7 < lim:
        a += 1
    if a < 2:
        return 0
    return binary_search_inf(l_p, a) + 1


def nb2(lim):  # n = p^3*q with n <= lim
    s = 0
    for i in range(len(l_p)):  # q < p
        p = l_p[i]
        if p**3 > lim//2:
            break
        s += min(binary_search_inf(l_p[:i+1], lim / (p ** 3)) + 1, i)
    for i in range(len(l_p)):  # q > p
        q = l_p[i]
        b = lim/q
        if b < 8:
            break
        s += min(binary_search_inf(l_p[:i+1], b ** (1 / 3)) + 1, i)
    return s


def nb3(lim):
    s = 0
    for p in l_p:  # p > q > r
        for i in range(len(l_p)):
            q = l_p[i]
            if q >= p:
                break
            if q*p * 2 > lim:
                break
            s += min(binary_search_inf(l_p[:i+1], lim / (p * q)) + 1, i)
    return s


def nb(lim):
    return nb1(lim)+nb2(lim)+nb3(lim)

print(nb(10**12))  # not 308795374
