from Tools import decompose_tout, numpy_sieve, bezout

n_fin = 20000
modulo = 1000000007
lp = numpy_sieve(n_fin)


def inv(a, p):
    return bezout(a, p)[1] % p


l_inv = {p:inv(int(p)-1, modulo) for p in lp if p > 2 }


def sigma(d):
    a = 1
    for p in d:
        if p == 2:
            a *= pow(2, d[2]+1, modulo)-1
        else:
            a *= (pow(int(p), d[p]+1, modulo)-1)*l_inv[p]
        a %= modulo
    return a


def decompose_B(n, d, df):
    ln = decompose_tout(n, lp)
    for p, a in ln:
        if p in d:
            d[p] += a*n
        else:
            d[p] = a*n

        if p in df:
            df[p] += a
        else:
            df[p] = a
    for p in df:
        d[p] -= df[p]

    return sigma(d)


d, df = dict(), dict()
s = 1
for n in range(2, n_fin+1):
    s += decompose_B(n, d, df)
    s %= modulo
    if n in [5, 10, 100]:
        print(s)
print(s)  # sol = 538319652
