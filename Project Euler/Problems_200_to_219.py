# %% Problem 203


# def square_free(n):
#     if n % 2 == 0:
#         n //= 2
#         if n % 2 == 0:
#             return False
#     a = 3
#     while n != 1 and a ** 2 <= n:
#         if n % a == 0:
#             n //= a
#             if n % a == 0:
#                 return False
#         a += 2
#     return True


def is_square_free(n):
    for i in [4, 9, 25, 49]:
        if n % i == 0:
            return False
    return True

from time import time
timer = time()
l = [1, 1]
acc = 1
l_sf = [1]
for line in range(3, 52):
    ll = [1]
    for i in range(line-2):
        a = l[i] + l[i+1]
        if is_square_free(a):
            if a not in l_sf:
                l_sf.append(a)
                acc += a
        ll.append(a)
    ll.append(1)
    l = ll.copy()
print(acc)
print(time()-timer)  # 3.5 ms

# bis (cf thread project euler)
timer = time()
squaredprimes = [4, 9, 25, 49]


def squarefree(n):
    return not any([n % i == 0 and n >= i for i in squaredprimes])


def candidates(n):
    triangle = [1]
    s = set()
    for i in range(0, n - 1):
        triangle = [j + k for j, k in zip([0] + triangle, triangle + [0])]
        s = s | set(triangle[:len(triangle) // 2])
    return s


print(sum([i for i in candidates(51) if squarefree(i)]))
print(time() - timer)  # 1.358 ms

# %% Problem 204

from math import log10
from Tools import numpy_sieve
l_100 = numpy_sieve(100)


def f(s, i):
    if i == len(l_100):
        return 1
    nb = 0
    while s <= 9:
        nb += f(s, i + 1)
        s += log10(l_100[i])
    return nb

print(f(0, 0))

# %% Problem 205

colin = dict()
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        colin[a+b+c+d+e+f] = colin.get(a+b+c+d+e+f, 0) + 1
pete = dict()
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        for g in range(1, 5):
                            for h in range(1, 5):
                                for i in range(1, 5):
                                    pete[a + b + c + d + e + f + g + h + i] = \
                                        pete.get(a + b + c + d + e + f + g + h + i, 0) + 1
n_tot = 4**9*6**6

s = 0
s2 = 0
for n1 in colin:
    for n2 in pete:
        s2 += colin[n1]*pete[n2]
        if n2 > n1:
            s += colin[n1]*pete[n2]
print(s/n_tot)


# %% Problem 206
import re

s = "1_2_3_4_5_6_7_8_9_0"
"""i**2 % 1000 = 900 => i%100 = 70 """

for i in range(10**7, 15*10**6):
    if re.match('1[0-9]2[0-9]3[0-9]4[0-9]5[0-9]6[0-9]7[0-9]8[0-9]9[0-9]0$', str((i*100+70)**2)):
        print(i*100+70)
        break

# s = 1389019170**2


# %% Problem 207

from math import log2


def n_tot(m):
    a = int((1+(1+4*m)**0.5)/2+0.01) - 1
    while a*(a+1) <= m:
        a += 1
    return a - 1


def my_log2(a):
    b = log2(a)
    p = 2**b
    while p*2 < a:
        b += 1
        p *= a
    return b


def n_perfect(m):
    return int(my_log2(1+4*m)/2 - 1 + 0.01)


def n(m):
    return n_perfect(m), n_tot(m), n_perfect(m)/n_tot(m)


def f(x):
    a, b = n(x)[:-1]
    return 12345*a - b

a = 1000
b = 10**11

while b - a > 1:
    m = (b+a) / 2
    if f(m) >= 0:
        a = m
    else:
        b = m
print(int(b))

# %% Problem 210

from Tools import decompose_tout


def problem_210(R=10**9):  # ok only for R such that R%8 == 0

    nb_tot = 3*(2*R+1)*R//4  # number of lattice point B outside the circle passing by O, C.

    nb_tot2 = 1
    r0 = (R/4)*2**0.5/2
    for i in range(0, int(r0)+1):
        nb_tot2 += 4*int((R**2/32-i**2)**0.5)

    def circumference(n):  # give the number of x,  y such that x**2+y**2 = n
        l = decompose_tout(n)
        B = 1
        for p, a in l:
            if p == 2:
                continue
            if p % 4 == 1:
                B *= a+1
            elif a % 2 == 1:
                return 0
        return B*4

    nb_problem = nb_tot + nb_tot2 - (R-1) - circumference(R**2/32)
    # less the number of B ON the circle passing by O, C and less the number of triangle with a 180° angle.
    return nb_problem  # sol = ??? 1598174770174689526
