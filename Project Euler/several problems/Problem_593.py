# %% Problem 593

from Tools import numpy_sieve
l_p = numpy_sieve(10**8)


def s(k):
    return pow(l_p[k-1], k, 10007)


def s2(k):
    return s(k) + s(k//10000+1)

L = [s(i) for i in range(1, 10**5)]
L2 = [s2(i) for i in range(1, 10**5)]


def m(i, j):
    LL = sorted(L2[i-1: j])
    n = len(LL)
    q, r = n.__divmod__(2)
    if r == 1:
        return LL[q]
    else:
        a = LL[q-1] + LL[q]
        r = a % 2
        a //= 2
        a += (0 if r == 0 else 0.5)
        return a


def f(n, k):
    s = 0
    for i in range(1, n-k+2):
        s += m(i, i+k-1)
    return s