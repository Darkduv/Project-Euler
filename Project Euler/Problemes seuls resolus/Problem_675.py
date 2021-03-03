from Tools import decompose_tout, bezout, numpy_sieve

l7 = numpy_sieve(10**7)

a = 1
mod = 1000000087
ss = 0
d = {}
for n in range(2, 10**7+1):
    lp = decompose_tout(n, l7)
    for p, i in lp:
        if p in d:
            a *= bezout(mod, 1+2*d[p])[0]
            d[p] += i
            a *= 1 + 2 * d[p]
        else:
            d[p] = i
            a *= 1 + 2 * d[p]
        a %= mod
    ss += a
    ss %= mod
print(ss)
# sol = 416146418
