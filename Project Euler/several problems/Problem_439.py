# %% Problem 439


from Tools import sum_divisor, phi, numpy_sieve

d = {}
N = 10**5
for i in range(1, N**2+1):
    d[i] = "i dont know what used to be here"
s = 0
for k in d:
    s += sum_divisor(k)*d[k]
    s %= 10**9
print(s)

l = numpy_sieve(10**6)

L = [(1, []) for i in range(10**11+1)]
for p in l:
    for k in range(p, 10**11+1, p):
        nb, l_k = L[k]
        L[k] = nb + 1, l_k + [p]
