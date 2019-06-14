# %% Problem 120


def rest(a, n):
    if n % 2 == 0:
        return 2
    else:
        return (2 * n * a) % (a**2)


def maxi(a):
    m = 0
    for n in range(1, 2*a):
        r = rest(a, n)
        if r > m:
            m = r
    return m

acc = 0
for a in range(3, 1001):
    acc += maxi(a)
print(acc)


# %% Problem 121

from itertools import product


l_possible = list(product([0, 1], repeat=15))


def ok(l):
    return sum(l) >= 8


def prob(l):
    a = 1
    b = 1
    for k, c in enumerate(l):
        a *= (k + 2)
        if c == 0:
            b *= (k+1)
    return b, a

a, b = 0, 1
for l in l_possible:
    if ok(l):
        c, d = prob(l)
        a *= d
        a += b*c
        b *= d
print(b//a)

# %% Problem 123


L = [2]
p = 3
n = 1
while True:
    end = False
    ok = True
    for j in L:
        if j ** 2 > p:
            break
        if p % j == 0:
            ok = False
            break
    if ok:
        n += 1
        L.append(p)
        if n % 2 == 1 and p > 10 ** 5:
            if (2 * n * p) % (p ** 2) >= 10 ** 10:
                print(n)
                end = True

    p += 2
    if end:
        break


# %% Problem 124


def rad(n):
    l = []
    while n % 2 == 0:
        if 2 not in l:
            l.append(2)
        n //= 2
    a = 3
    while n > 1:
        if n % a == 0:
            if a not in l:
                l.append(a)
            n //= a
        else:
            a += 2
    p = 1
    for i in l:
        p *= i
    return p


d = []
for n in range(1, 100001):
    d.append([rad(n), n])
d.sort()
print(d[10000-1][1])

# %% Problem 125

from Tools import palindromic


def ok(n):
    s = 1
    L = [1]
    i = 2
    while L:
        j = i**2
        if s + j < n:
            L.append(j)
            s += j
            i += 1
        elif s + j == n:
            return True
        else:
            s -= L.pop(0)
    return False

s = 0
for i in range(2, 10**8):
    if palindromic(i) and ok(i):
        s += i
print(s)

# %% Problem 129


def a(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    nb = 1
    k = 1
    nb %= n
    while nb != 0:
        k += 1
        nb *= 10
        nb += 1
        nb %= n
    return k

n = 10**6+1
while a(n) < 10 ** 6:
    n += 2
print(n)

# %% Problem 130


from Tools import numpy_sieve
l_p = numpy_sieve(10**6)

def a(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    nb = 1
    k = 1
    nb %= n
    while nb != 0:
        k += 1
        nb *= 10
        nb += 1
        nb %= n
    return k
nb = 0
n = 90
s = 0
while nb < 25:
    n += 1
    if n not in l_p:
        if pow(10, n-1, n) == 1:
            if (n-1) % a(n) == 0:
                nb += 1
                s += n
print(s)

# %% Problem 131

from Tools import numpy_sieve

l_p = numpy_sieve(10**6)

a = 1
n = 0
c = 3*a**2+3*a+1
while c < 10**6:
    if c in l_p:
        n += 1
    a += 1
    c = 3*a**2+3*a+1
print(n)

# %% Problem 132

from Tools import numpy_sieve


def ok(p):
    if p-1 < 10**9:
        # return 10**9 % (p-1) % p == 0
        return (10**(10**9 % (p-1)) - 1) % p == 0
    else:
        return False
        # return (10**((p-1) % 10**9) - 1) % p == 0

L = numpy_sieve(10**7)
s = 0
counter = 0
for p in L[3:]:
    if ok(p):
        s += p
        counter += 1
        print(p)
    if counter == 40:
        break
print(s)

# %% Problem 133

from Tools import numpy_sieve


def non_fac(p):
    nb = 1
    k = 1
    nb %= p
    while nb != 0:
        k += 1
        nb *= 10
        nb += 1
        nb %= p
    while k % 2 == 0:
        k //= 2
    while k % 5 == 0:
        k //= 5
    return k != 1

s = 2+3+5
for p in numpy_sieve(100000)[3:]:
    if non_fac(p):
        s += p
print(s)

# %% Problem 134

from Tools import bezout, numpy_sieve


def inv(u, p):
    return bezout(u, p)[1]


def mini(p1, p2):
    b = 10**int(log10(p1)+1) % p2
    return ((-p1*inv(b, p2)) % p2)*10**int(log10(p1)+1)+p1


l_p = numpy_sieve(10**6+10)

s = 0
for i in range(2, len(l_p)-1):
    if l_p[i] > 10**6:
        break
    s += mini(l_p[i], l_p[i+1])
print(s)

# %% Problem 137

# A_F(x) = -x/(x**2+x-1)
# A_f(x) = n avec x rationnel => 5n**2+2n+1=y**2

# f(x) = sqrt(5x**2+2x+1)
def f_prime(x, y):
    return 5*x+1, y

x1, y1 = 2, 5
x2, y2 = 15, 34


def next(x1, y1, x2, y2):
    a, b = f_prime(x2, y2)
    x3 = (2*b**2 - 2*a*(b*y1-a*x1))//(a**2 - 5*b**2)-x1
    y3 = (a*(x3-x1))//b + y1
    return x3, y3


count = 2
while count < 15:
    x3, y3 = next(x1, y1, x2, y2)
    x1, y1, x2, y2 = x2, y2, x3, y3
    count += 1
print(x2)


# %% Problem 138

# les next ne sont pas tous entier, utiliser type rationnel ??


def f_prime138(x, y):
    return 5*x+2, y

x1, y1 = 0, 1
x2, y2 = 136, 305


def next(x1, y1, x2, y2):
    a, b = f_prime138(x2, y2)
    x3 = (4*b**2 - 2*a*(b*y1-a*x1))//(a**2 - 5*b**2)-x1
    y3 = (a*(x3-x1))//b + y1
    return x3, y3

count = 1
L = [y2]
while count < 12:
    x3, y3 = next(x1, y1, x2, y2)
    x1, y1, x2, y2 = x2, y2, x3, y3
    L.append(y2)
    count += 1


def f_prime138(x, y):
    return 5*x-2, y

x1, y1 = 0, 1
x2, y2 = 8, 17


def next2(x1, y1, x2, y2):
    a, b = f_prime138(x2, y2)
    x3 = (-4*b**2 - 2*a*(b*y1-a*x1))//(a**2 - 5*b**2)-x1
    y3 = (a*(x3-x1))//b + y1
    return x3, y3

count = 1
L.append(17)
while count < 12:
    x3, y3 = next2(x1, y1, x2, y2)
    x1, y1, x2, y2 = x2, y2, x3, y3
    L.append(y2)
    count += 1

L.sort()
print(L[:12])
print(sum(L[:12]))


# %% Problem 139
"""
for a < b < c such that a**2 + b**2 == c**2 and (b-a) | c, we can show that b-a == 1
so we are looking for x, y such that x**2 + (x+1)**2 == y**2 with 2*x+1+y <= 10**8,
that is 2*x**2 + 2*x + 1 == y ** 2.
so with f(x) = sqrt(2*x**2 + 2*x + 1), f(x) = y
"""


def f_prime(x, y):
    return 2*x+1, y

x1, y1 = 0, 1
x2, y2 = 3, 5


def next(x1, y1, x2, y2):
    a, b = f_prime(x2, y2)
    x3 = (2*b**2 - 2*a*(b*y1-a*x1))//(a**2 - 2*b**2)-x1
    y3 = (a*(x3-x1))//b + y1
    return x3, y3

L = []

while 2*x2 + 1 + y2 < 10**8:
    L.append(2*x2+y2+1)
    x3, y3 = next(x1, y1, x2, y2)
    x1, y1, x2, y2 = x2, y2, x3, y3

n = 0
for s in L:
    q = (10**8)//s
    n += q
print(n)
