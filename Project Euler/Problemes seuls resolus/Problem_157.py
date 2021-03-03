# %% Problem 157
from Tools import decompose_tout


def f(l, i=0):
    if len(l)-i == 0:
        yield []
    else:
        p, a = l[i]
        for c in range(a+1):
            for ll in f(l, i+1):
                yield [(p, c)]+ll


def compute(l):
    prod = 1
    for p, a in l:
        prod *= p**a
    return prod


def div(n):
    ll = decompose_tout(n)
    for p_a in f(ll):
        yield compute(p_a)


def number(nb):
    s_tot = set()
    for p1 in range(nb+1):
        for p2 in range(nb+1):
            for q1 in range(nb+1):
                for q2 in range(nb+1):
                    if 2**p1*5**q1 > 2**p2*5**q2:
                        continue
                    pi = min(p1, p2)
                    qi = min(q1, q2)
                    pa = p1-pi
                    pb = p2-pi
                    qa = q1 - qi
                    qb = q2 - qi
                    for d in div(2**pa*5**qa+2**pb*5**qb):
                        a = 2**p1*5**q1 * d
                        b = d * 2**p2*5**q2
                        n = 1
                        q = 10
                        while (q*(a+b)) % (a*b) != 0 and n < nb:
                            q *= 10
                            n += 1
                        if n < 10:
                            for m in range(n, 10):
                                s_tot.add((a, b, (10**m*(a+b)) // (a*b), m))
    return len(s_tot)


print(number(9))  # sol = 53490
