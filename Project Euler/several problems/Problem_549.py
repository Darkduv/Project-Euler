from math import log
from Tools import decompose_tout, numpy_sieve
l_8 = numpy_sieve(10**8)

d = dict()


def log_p(n, p):
    return int(log(n)/log(p) + 0.5)


def decompose_p(n, p):
    k = 0
    while n % p == 0:
        k += 1
        n //= p
    return k


def ok(p):
    L = []
    m = 0
    i = 0
    k0 = log_p(10**8, p)
    while i < k0:
        m += p
        i += decompose_p(m, p)
        L.append((i, m))
    return L


for p in l_8:
    d[p] = ok(p)


def f(p, k):
    for i, m in d[p]:
        if i >= k:
            return m
    return None


def s(n):
    l = decompose_tout(n, l_8)
    maxi = 0
    for p, k in l:
        m = f(p, k)
        if m > maxi:
            maxi = m
    return maxi

L = [n for n in range(10**8+1)]

k0 = 0
for p in l_8:
    for k, m in d[p]:
        pass
