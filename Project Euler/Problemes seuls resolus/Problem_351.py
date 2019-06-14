# %% Problem 351

from Tools import numpy_sieve

n_tot = 10**8
l8 = numpy_sieve(n_tot)

phi = [i for i in range(n_tot+1)]
for p in l8:
    for k in range(p, n_tot, p):
        phi[k] *= (p - 1)
        phi[k] //= p

s_tot = 0
for s in range(1, n_tot + 1):
    s_tot += s - phi[s]
print(s_tot)  # sol = 11762187201804552
