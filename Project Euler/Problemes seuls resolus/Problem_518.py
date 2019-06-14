# %% Problem 518


from Tools import numpy_sieve, decompose_tout, binary_search_inf

l_8 = numpy_sieve(10**8)


s = 0
n = len(l_8)
ll_8 = set(l_8)

for i in range(n-2):
    a = l_8[i]
    la = decompose_tout(a+1, l_8)
    q = 1
    for p, j in la:
        q *= p**(j//2)
    m = int((l_8[-1]/a)**0.5*q)
    j2 = binary_search_inf(l_8, (a+1)*m/q)
    if m - q < j2-i:
        for k in range(q+1, m+1):
            b = (((a+1)//q)*k) - 1
            c = (((b+1)//q)*k) - 1
            if b in ll_8 and c in ll_8:
                s += a+b+c
    else:
        for j in range(i + 1, j2+1):
            b = l_8[j]
            c, r = ((b + 1) ** 2).__divmod__(a + 1)
            if c - 1 > 10 ** 8:
                break
            if r == 0 and c - 1 in ll_8:
                s += a + b + c - 1
print(s)


# or ?

def divisor(l, pos=0):
    if len(l) == pos:
        yield 1
    else:
        aa, jj = l[pos]
        for kk in range(jj//2+1):
            for pp in divisor(l, pos+1):
                yield pp*aa**kk


def ok(aa):
    ll = decompose_tout(aa + 1)
    ss = set()
    for pp in divisor(ll):
        for qq in range(1, pp):
            bb = (aa + 1) // pp * qq - 1
            if bb in ll_8:
                cc = (bb + 1) // pp * qq - 1
                if cc in ll_8:
                    ss.add((aa, bb, cc))
    return ss


def sum_set(ss):
    return sum(sum(aa) for aa in ss)


s_tot = 0
for a in l_8:
    s_tot += sum_set(ok(a))
