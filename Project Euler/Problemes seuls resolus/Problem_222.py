# %% Problem 222
def next_l(l, n):
    i = l.index(n+1)
    j = l.index(n+2)
    k = max(i, j)
    l.insert(k, n)

l = [50, 49]
for k in range(48, 29, -1):
    next_l(l, k)


def f(a, b):
    return ((a+b)**2 - (100 - a - b)**2)**0.5


def aux(l):
    a = l[0]
    s = a
    for b in l[1:]:
        s += f(a, b)
        a = b
    s += a
    return s

print(int(aux(l)*10**3))
