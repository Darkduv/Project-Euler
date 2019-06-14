# %% Problem 307


def binomial(n, k):
    L = [1]
    for _ in range(n):
        L2 = [1]
        a = 1
        for b in L[1:]:
            L2.append(a + b)
            a = b
        L2.append(1)
        L = L2[:k+1]
    return L


def f(k):
    L = binomial(k)
    s = 0
    for i in range(k//2+1):
        s += L[2*i]*2**(k-i)
    return s
