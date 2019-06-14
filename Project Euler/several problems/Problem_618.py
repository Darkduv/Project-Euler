from Tools import numpy_sieve


fib = [0, 1]
for _ in range(23):
    fib.append(fib[-1]+fib[-2])

nn = fib[24]
lp = list(numpy_sieve(nn+1))


L = [[], [], [2], [0, 3], [4]]
for a in range(5, nn+1):
    ll = []
    for i in range(len(lp)):
        k = lp[i]
        if k > a//2:
            break
        elif k == a//2 and a % 2 == 0:
            ll.extend([0] * (i - len(ll)))
            ll.append(k*k % 10**9)
        else:
            if len(L[a-k]) > i:
                ll.extend([0]*(i-len(ll)))
                ll.append(sum(L[a-k][i:])*k % 10**9)
    if a in lp:
        i = lp.index(a)
        ll.extend([0] * (i - len(ll)))
        ll.append(a)
    L.append(ll)
