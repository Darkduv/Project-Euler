# %% Problem 237
import numpy as np


L = np.matrix([1, 1, 4, 8]).transpose()

A = np.matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, -2, 2, 2]])


def quick_expo(x, n, mod=None):
    z = np.identity(4, int)
    y = x.copy()
    if mod:
        while n != 0:
            if n % 2 == 1:
                z = z * y
                z %= mod
            n //= 2
            y = y * y
            y %= mod
        return z % mod
    else:
        while n != 0:
            if n % 2 == 1:
                z = z * y
            n //= 2
            y = y * y
        return z

AZ = quick_expo(A, 10**12-4, 10**8)

print((AZ[3]*L)[0, 0] % 10**8)  # sol = 15836928
