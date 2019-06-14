# %% Problem_591


from math import pi
from Tools import bezout, gcd


# bezout(u, n):  # return y, x where u*x + b*y = 1


def a_b_n(k, D):
    h1, k1 = 1, 0
    a_i = int(D ** 0.5)
    r = 1, 1, -a_i, 1
    h2, k2 = a_i, 1
    for i in range(k):
        a, b, c, d = r
        a, b, c, d = (a * b * d ** 2, a ** 2 * d ** 2 * D - c ** 2 * b ** 2, -c * b ** 2 * d,
                      a ** 2 * d ** 2 * D - c ** 2 * b ** 2)
        d1 = gcd(abs(a), abs(b))
        a //= d1
        b //= d1
        a_i = int(a * (D ** 0.5) / b + c / d)
        c -= a_i * d
        d2 = gcd(abs(c), abs(d))
        c //= d2
        d //= d2
        r = a, b, c, d
        h1, h2 = h2, a_i * h2 + h1
        k1, k2 = k2, a_i * k2 + k1
    return h2, k2


def h_k_(i):
    h1, k1 = 1, 0
    a_i = int(pi)
    r = pi - a_i
    h2, k2 = a_i, 1
    for times in range(i):
        a_i = int(r**-1)
        r = r**-1-a_i
        h1, h2 = h2, a_i * h2 + h1
        k1, k2 = k2, a_i * k2 + k1
    return h2, k2


pi2 = h_k_(19)
k = 40
sqrt2int = a_b_n(40, 2)
a, b = sqrt2int
c, d = pi2
while (c*b) % d > 10:
    k += 1
    a, b = a_b_n(k, 2)
    if k > 10**4:
        break



