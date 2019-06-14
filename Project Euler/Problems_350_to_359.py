# %% Problem 357

from time import time
from queue import deque
from Tools import numpy_sieve

l_primes = numpy_sieve(10**8)

timer = time()


def ok_mieux(p, l_p):
    for i in l_p:
        if p//i + i not in d:
            return False
    return True

i, p, l, n_lim = 1, 2, l_primes, 10**8
s = 1  # 1 works !!!!!!

f = deque()
f.append((i, p, [1, 2]))
while f.__len__() != 0:
    i, p, l_p = f.popleft()
    if i == len(l):
        s += p if ok_mieux(p, l_p) else 0
    else:
        a = l[i]*p
        if a <= n_lim:
            f.append((i+1, p, l_p))
            l_p2 = l_p[:]
            for b in l_p:
                l_p2.append(b*l[i])
            f.append((i+1, a, l_p2))
        else:
            s += p if ok_mieux(p, l_p) else 0

print(s)
print(time()-timer)


# %%% Problem 358

from Tools import is_prime

# we search for p prime such that (10**(p-1)-1)/p = 00000000137...56789
b = int(1/0.00000000137)
a = int(1/0.00000000138)
# a < p < b
k = 1
while (56789*k) % 10**5 != 99999:
    k += 1
# p ends up with k
l = []
for p in range(a, b):
    if p % 10**5 == k and is_prime(p):
        l.append(p)


for a in l:
    print(9*(a-1)//2)
# s is one of the values
# sol = 3284144505
