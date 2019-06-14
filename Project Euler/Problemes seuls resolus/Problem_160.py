# %% Problem 160

from Tools import v_p
from math import log2

D = 10 ** 5
N = 10 ** 12

g = {1: 1}
p = 1
for i in range(1, D, 2):
    if i % 5 != 0:
        p *= i
        p %= D
        g[i] = p


def f(n):
    q, r = n.__divmod__(D)
    return (g[r]*pow(g[D-1], q, D))%D


p_tot = 1

for a2 in range(int(log2(N))+1):
    for a5 in range(int(log2(N)/log2(5))+1):
        if 2**a2*5**a5 > N:
            break
        b = N//(2**a2*5**a5)
        while b%2 == 0 or b%5 == 0:
            b -= 1
        p_tot *= f(b)
        p_tot %= D
        if p_tot == 0:
            print(a2, a5, b)
            a2 /= 0


p_tot *= pow(2, v_p(N, 2)-v_p(N, 5), D)
p_tot %= D
print(p_tot)  # sol = 16576
