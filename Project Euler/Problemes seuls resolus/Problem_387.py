# %% Problem 387
from Tools import is_prime


def s_digit(n):
    return sum(int(a) for a in str(n))


def ok(n):
    return n % s_digit(n) == 0


L = [i for i in range(1, 10)]
L_bis = [i for i in range(1, 10)]
for count in range(12):
    L_ter = []
    for a in L_bis:
        for i in range(10):
            b = a*10 + i
            if ok(b):
                L_ter.append(b)
                L.append(b)
    L_bis = L_ter


def ok2(n):
    return is_prime(n // s_digit(n)) and (n != 1) and (n // s_digit(n) != 1)

L = [a for a in L if ok2(a)]

S = 0
for a in L:
    for i in [1, 3, 7, 9]:
        if is_prime(a*10+i):
            S += a*10+i

print("\n", S)
