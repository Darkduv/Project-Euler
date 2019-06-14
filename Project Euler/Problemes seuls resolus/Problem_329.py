# %% Problem 329

from Tools import numpy_sieve, gcd

lp = numpy_sieve(500)
ok = "PPPPNNPPPNPPNPN"

L = [1]*501
for k in range(15):
    L2 = [0]*501
    L2[2] += L[1]*(2 if ok[k] == 'P' else 4)
    for p in range(2, 500):
        if p in lp:
            pp, pn = 2, 1
        else:
            pp, pn = 1, 2
        a = L[p] * (pp if ok[k] == 'P' else pn)
        L2[p - 1] += a
        L2[p + 1] += a
    L2[499] += L[500]*(2 if ok[k] == 'P' else 4)
    L = L2

s = 0
for a in L:
    s += a

d = gcd(s, 500*6**15)
print(str(s//d)+"/"+str((500*6**15)//d))  # sol = 199740353/29386561536000
