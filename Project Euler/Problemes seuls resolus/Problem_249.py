from Tools import numpy_sieve

L = numpy_sieve(5000)
L2 = numpy_sieve(sum(L))
LL = [0] * (L2[-1] + 1)
LL[0] = 1
s = 0
for b in L:
    for a in range(s, -1, -1):
        if a + b >= len(LL):
            continue
        LL[a + b] += LL[a]
        LL[a + b] %= 10 ** 16
    s += b
print(sum(LL[a] for a in L2) % 10 ** 16)  # sol = 9275262564250418
