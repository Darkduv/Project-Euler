# %% Problem 531


from Tools import numpy_sieve, gcd, bezout
l_6 = numpy_sieve(1005000)


def v_p(n, p):
    nb = 0
    while n % p == 0:
        n //= p
        nb += 1
    return nb

L = [{} for _ in range(5000)]
for p in l_6:
    n1, r1 = int.__divmod__(10**6, p)
    if r1 != 0:
        n1 += 1
    n2 = (1005000-1) // p
    for k in range(n1*p, (n2+1)*p, p):
        L[k-10**6][p] = v_p(k, p)


def phi(n):
    d = L[n-10**6]
    prod1 = 1
    prod2 = 1
    for p in d:
        prod1 *= (p-1)
        prod2 *= p
    return prod1*(n//prod2)


L_phi = []
for n in range(10**6, 10**6+5000):
    L_phi.append(phi(n))


def phi2(n):
    return L_phi[n-10**6]


def fx(n, m):
    d1 = gcd(n, m)
    n0 = n
    phin0 = phi2(n)
    c = phi2(m) - phin0
    if c % d1 != 0:
        return 0
    c //= d1
    m //= d1
    n //= d1
    v, u = bezout(n, m)
    k = (u*c) % m
    return n0*k+phin0


s = 0
for n in range(10**6, 10**6+5000-1):
    for m in range(n+1, 10**6+5000):
        s += fx(n, m)


# s == 4515432351156203105
