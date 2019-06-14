# %% Problem 153
from Tools import gcd


def g(n, a, b):
    return sum(b*d*(n//(a*d)) for d in range(1, n//a+1))


def f(n):
    n2 = int(n**0.5)
    s = g(n, 1, 1)
    for i in range(1, n2+1):
        for j in range(i, n2+1):
            if gcd(i, j) != 1:
                continue
            s += g(n, i**2+j**2, (i+j))*(2 if i != j else 1)
    return s


print(f(10**8))
# sol = 17971254122360635
