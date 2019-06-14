from math import log


def g(n, e):
    return n - (n - 1) ** (1 / e)


def f(k, e, lim):
    if k+k**e <= lim:
        l = [k+k**e]
    else:
        l = []
    a = k**(e**2)
    n = a+1
    while n <= lim and g(n, e) <= a:
        l.append(n)
        n += 1
    return l


def test(n, e, a0):
    l = []
    while a0 > 1:
        if a0 in l:
            return True, l
        else:
            l.append(a0)
        a0 = min(a0**e, n-a0**e)
    return False, []
# l_5_3 = [(a, test(a, 3, 5)[1]) for a in f(5, 3, 10**18)  if test(a, 3, 5)[0] ]
# len(l_5_3) == 2
# l_5_3 == [(1953130, [5, 125]), (1953250, [5, 125])]


N = 10**18
l_tot = []
for ee in range(2, int(log(N)/log(2))+1):
    for kk in range(2, int((N-1)**(1/ee**2))+1):
        l_tot.extend(f(kk, ee, N))
