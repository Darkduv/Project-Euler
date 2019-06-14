# %% Problem 234

from math import ceil
from Tools import numpy_sieve

lim = 999966663333
lp = numpy_sieve(int(lim**0.5)+30)

s = 0
for i in range(len(lp)-1):
    p1 = lp[i]
    if p1 ** 2 + 1 > lim:
        break
    p2 = lp[i+1]
    n1max = (p2**2-1)//p1
    n1min = p1+1
    s += p1 * ((n1max*(n1max+1) - n1min*(n1min-1))//2)

    n2max = p2 - 1
    n2min = ceil((p1 ** 2 + 1) / p2)
    s += p2 * ((n2max*(n2max+1) - n2min*(n2min-1))//2)

    n3max = int((p2**2-1) / (p1*p2))
    n3min = ceil((p1**2+1) / (p1*p2))
    s -= 2 * p1 * p2 * ((n3max * (n3max + 1) - n3min * (n3min - 1)) // 2)

p1, p2 = lp[-2:]
s -= sum(k for k in range(lim, p2**2) if (k % p1 == 0) ^ (k % p2 == 0))  # surely a lot fof smarter ways

print(s)  # s = 1259187438574927161
