# %% Problem 381

from Tools import numpy_sieve
l_8 = numpy_sieve(10**8)


def s(p):
    q, r = p.__divmod__(3)
    if r == 1:
        inv3 = 2*q + 1
    else:
        inv3 = q + 1
    q, r = p.__divmod__(4)
    if r == 1:
        inv4 = 3*q + 1
    else:
        inv4 = q + 1
    inv2 = (p-1) // 2
    return (inv3*inv4*inv2*9) % p

S = 0
for prime in l_8[2:]:
    S += s(prime)

print(S)
