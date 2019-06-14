# %% Problem 268

from Tools import numpy_sieve
l = numpy_sieve(100)


def f(N=10**16, p=1, k=-1, n=1, a=-1, s=0):
    tetra = [(i*(i+1)*(i+2))//6 for i in range(1, 25)]  # see inclusion-exclusion principle & tetrahedral numbers
    if p > N or n > 25:
        return s
    for k2 in range(k+1, 25):
        p2 = p*l[k2]
        if p2 > N:
            break
        if n >= 4:
            s += (N//p2) * a * tetra[n-4]
        s = f(N, p2, k2, n+1, a*-1, s)
    return s


print(f(10**3))
print(f(10**16))  # sol = 785478606870985
