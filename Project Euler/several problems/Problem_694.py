from Tools import decompose_tout, numpy_sieve

l6 = numpy_sieve(10**6)

lp = [True for i in range(10**6+1)]
for p in l6:
    k = p**2
    while k <= 10**6:
        lp[k] = False
        k += p**2
lp = [p for p in range(1, 10**6+1) if lp[p]]

def s_prime(a, n):
    return n//(a**3)


N = 10**18
M = 10**6


def sol(M, N):
    s = 0
    for a in range(1, M+1):
        if a in lp:
            s += s_prime(a, N)
    return s


print(sol(M, N))


def aux(n):
    l = []
    for a in range(1, n+1):
        if n%a == 0:
            for o, i in decompose_tout(a):
                if i < 3:
                    break
            else:
                l.append(a)
    return l
