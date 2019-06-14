# %% Problem 515

# it can be shown that d(p, p-1, k) = (k-1)^-1 in Z/pZ

from Tools import bezout, numpy_sieve


def inv(n, p):
    if n == 1:
        return 1
    a = bezout(n, p)[1]
    while a < 0:
        a += p
    return a


def is_prime(a):
    for p in l_p:
        if p**2 > a:
            return True
        if a % p == 0:
            return False
    return True


l_p = numpy_sieve(10**5)
l_9 = [p for p in range(10**9+1, 10**9+10**5, 2) if is_prime(p)]
s = 0
for p in l_9:
    s += inv(10**5-1, p)
print(s)
