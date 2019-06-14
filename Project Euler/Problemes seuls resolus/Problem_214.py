# %% Problem 214 # TODO : far too long ...

from Tools import numpy_sieve, phi
lp = numpy_sieve(10**7*4)
dok = {}


def nb(n, k2=0):
    if k2 > 25:
        return 42
    if n == 1:
        return 1
    if n in dok:
        return dok[n]
    else:
        n2 = phi(n, lp)
        k = 1+nb(n2, k2+1)
        dok[n] = k
        return k

s = 0
ll = []
for p in lp:
    if nb(p-1) == 24:
        s += p
        ll.append(p)
print(s)  # sol = 1677366278943
