# %% Problem_172
from math import factorial

L18 = []

for a in range(11):
    for b in range(11-a):
        for c in range(11-a-b):
            d = 10-a-b-c
            if b+2*c+3*d == 18:
                L18.append((a, b, c, d))


def binomial(k, n):
    return factorial(n)//(factorial(k)*factorial(n-k))

s = 0
for l in L18:
    p = factorial(18)
    for j in range(4):
        p //= factorial(j)**l[j]
    m = 10
    for j in range(1, 4):
        p *= binomial(l[j], m)
        m -= l[j]
    p *= 9
    p //= 10
    s += p
print(s)  # sol = 227485267000992000
