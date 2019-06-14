# %% Problem 396


def from_base(l, p):
    a = 0
    for d in l:
        a *= p
        a += d
    return a


def to_base(n, p):
    l = []
    while n != 0:
        n, r = int.__divmod__(n, p)
        l.append(r)
    return l[::-1]


def goodstein(n):
    l = [n]
    a = n
    k = 1
    while a != 0:
        k += 1
        a = from_base(to_base(a, k), k+1) - 1
        l.append(a)
    return l


def g(n):
    return len(goodstein(n))-1

s = 0
for i in range(1, 16):
    s += g(i)
print(s)