# %% Problem 493

from Tools import fact


def comb(k, n):
    N = fact(n)
    N //= fact(k)
    N //= fact(n-k)
    return N


def f(left, k):
    if left <= 0:
        return 0
    if k == 1:
        if left > 10:
            return 0
        else:
            return comb(left, 10)
    S = 0
    for i in range(1, min(11, left+1)):
        S += comb(i, 10)*f(left - i, k - 1)
    return S

E = 0
for a in range(1, 8):
    E += comb(a, 7)*f(20, a)*a
E /= comb(20, 70)
print(int(E*10**9)/10**9)
