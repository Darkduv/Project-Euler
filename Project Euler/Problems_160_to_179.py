# %% Problem 162

L = [0, 1, 16+15]
for i in range(3, 17):
    L.append(16**(i-1)+L[-1]*15)
L2 = [0, 0, 2]
for i in range(3, 17):
    L2.append(2*L[i-1] + 14*L2[-1])
L3 = [0, 0, 0, 6]
for i in range(4, 17):
    L3.append(3*L2[i-1] + 13*L3[-1])
print(str(hex(sum(L3[i]-L2[i-1] for i in range(3, 17))))[2:].upper())  # sol = 3D58725572C62302


# %% Problem 164


from time import time
t = time()

N = 20
L = [[] for _ in range(10)]
for i in range(10):
    for j in range(10-i):
        L[i].append(1)

for n in range(3, N+1):
    LL = [[] for _ in range(10)]
    for i in range(10):
        for j in range(10-i):
            LL[i].append(sum(L[j][k] for k in range(10-i-j)))
    L = LL

s = 0
for i in range(1, 10):
    for j in range(10-i):
        s += L[i][j]
t2 = time()
print(s)
print(t2-t)


# %% Problem 169

d = {2: 2, 1: 1}


def f(k):
    if k not in d:
        q, r = int.__divmod__(k, 2)
        if r == 1:
            a = f(q)
        else:
            a = f(q) + f(q - 1)
        d[k] = a
    else:
        a = d[k]
    return a

print(f(10**25))


# %% Problem 172


def f(L):
    if len(L) == 18:
        return L
    LL = []
    for el in L:
        for i in range(10):
            if el.count(i) <= 2:
                LL += f([el + [i]])
    return LL

f([[i] for i in range(1, 10)])


# %% Problem 173  #  there is very much better than this solution -> see The thread


from Tools import decompose_tout, numpy_sieve
l_6 = numpy_sieve(10**6)


def d(n):
    l = decompose_tout(n, l_6)
    p = 1
    for a, i in l:
        p *= i+1
    return p

s = 0
for n in range(2, 25*10**4+1):
    s += d(n)//2
print(s)


# %% Problem 174  #  there is very much better than this solution -> see The thread


from Tools import decompose_tout, numpy_sieve
l6 = numpy_sieve(10**6)


def d(n):
    l = decompose_tout(n, l6)
    p = 1
    for a, i in l:
        p *= i+1
    return p

s = 0
for n in range(2, 25*10**4+1):
    if d(n)//2 <= 10:
        s += 1
print(s)


# %% Problem 179

from Tools import decompose_tout, numpy_sieve
l_erato = numpy_sieve(10**7)


def nb_div(n):
    l = decompose_tout(n, l_erato)
    p = 1
    for i, nb in l:
        p *= (nb+1)
    return p

p = 1
nb = 0
for i in range(2, 10**7+1):
    pp = nb_div(i)
    if pp == p:
        nb += 1
    p = pp
print(nb)
