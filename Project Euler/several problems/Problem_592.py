from Tools import numpy_sieve


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)


def n_p(n, p=2):  # v_2(n!)
    s = 0
    m = 1
    while m < n:
        m *= p
        s += n // m
    return s

FACT = fact(20)
N2 = n_p(FACT)

# N2 = r * 4 ** k

r = N2 % 4
k = N2 // 4


l_7 = numpy_sieve(10**7)
d = dict()
for p in l_7:
    d[p] = n_p(FACT, p)


prod = 1
for p in d:
    if p == 2:
        continue
    prod *= pow(p, d[p], 16**12)
    prod %= 16**12
print(prod)

L = []
for i in range(10**5):
    a = (i*prod) % 16**12
    if a not in L:
        L.append(a)