# %% Problem 80


def approx(n):
    a = int(sqrt(n))
    if a ** 2 == n:
        return 0

    c = n
    for nb in range(1, 100):
        a *= 10
        c *= 100
        while (a + 1) ** 2 < c:
            a += 1

    s = 0
    while a > 0:
        s += a % 10
        a //= 10

    return s


s = 0
for n in range(2, 100):
    s += approx(n)
print(s)

# %% Problem 81

import os

os.chdir('/Users/maximin/Desktop/Euler/linked_files')
with open('p081_matrix.txt', 'r') as f:
    mat = []
    for i in f:
        l = []
        i = i[:-1]
        i = i.split(",")
        for n in i:
            l.append(int(n))
        mat.append(l)

tab = [[0] * 80 for i in range(0, 80)]
tab[0][0] = mat[0][0]

for i in range(1, 80):
    tab[0][i] = tab[0][i - 1] + mat[0][i]
    tab[i][0] = tab[i - 1][0] + mat[i][0]

for i in range(1, 80):
    for j in range(1, 80):
        tab[i][j] = mat[i][j] + min(tab[i][j - 1], tab[i - 1][j])

print(tab[79][79])

# %% Problem 82


from os import chdir

chdir("/Users/maximin/Desktop/Euler")

with open("p082_matrix.txt", 'r') as f:
    mat = []
    for i in f:
        mat.append([int(s) for s in i[:-1].split(",")])

tab = [[i for i in j] for j in mat]

for j in range(1, 79):
    for i in range(80):
        mini = tab[i][j - 1]
        if i > 0:
            if tab[i - 1][j] < mini:
                mini = tab[i - 1][j]

        k = i + 1
        s = 0
        while k < 80 and s < mini:
            s += tab[k][j]
            if s + tab[k][j - 1] < mini:
                mini = s + tab[k][j - 1]
            k += 1

        tab[i][j] += mini

for i in range(80):
    tab[i][-1] += tab[i][-2]

mini = tab[0][-1]
for i in range(80):
    if tab[i][-1] < mini:
        mini = tab[i][-1]

print(mini)

# %% Problem 83
from time import time
from os import chdir
timer = time()


chdir("/Users/maximin/Desktop/Euler")

with open("p083_matrix.txt", 'r') as f:
    mat = []
    for i in f:
        mat.append([int(s) for s in i[:-1].split(",")])


def d(s1, s2):
    i, j = s1
    k, l = s2
    return mat[i][j] + mat[k][l]


def near(s):
    i, j = s
    l = []
    for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= a < 80 and 0 <= b < 80:
            l.append((a, b))
    return l


P = {}
for i in range(80):
    for j in range(80):
        P[i, j] = False

D = [[1000000000000000000] * 80 for i in range(80)]  # c'était mon infini ....

D[0][0] = mat[0][0]

l_near = {(0, 0): 0}

s_work = (0, 0)


def update(s):
    l_near.pop(s)
    P[s] = True
    aa, bb = s
    DD = D[aa][bb]
    for i in near(s):
        if not P[i]:
            a, b = i
            D[a][b] = min(DD + d(s, i), D[a][b])
            l_near[i] = D[a][b]


def mini(d):
    i_m = min(d)
    m = d[i_m]
    for i in d:
        if d[i] < m:
            m = d[i]
            i_m = i
    return i_m

while (79, 79) not in l_near:
    update(s_work)
    s_work = mini(l_near)
print((D[-1][-1] + mat[-1][-1])//2)


print(time()-timer)


# %% Problem 84

from random import randint, shuffle


def des_2(sides):
    a = randint(1, sides)
    b = randint(1, sides)
    return a + b, a == b

L_CC = ["0", "10"] + [None]*14


def f_R(case):
    if case == 7:
        return 15
    elif case == 22:
        return 25
    else:
        return 5


def f_U(case):
    if case == 7:
        return 12
    elif case == 22:
        return 28
    else:
        return 12


def g(x):
    global a
    if x is not None:
        a = eval(x)

L_CH = [None, None, None, None, "0", "10", "11", "24", "39", "5",
        "f_R(a)", "f_R(a)", "f_U(a)", "int.__sub__(a, 3)"]

d = {}
for i in range(40):
    d[i] = 0

shuffle(L_CH)
shuffle(L_CC)


n = 4
a = 0
acc = 0
for k in range(10**7):
    b, double = des_2(n)
    if double:
        acc += 1
    else:
        acc = 0
    if acc == 3:
        acc = 0
        a = 10
    else:
        a += b
        a %= 40
        if a == 30:
            a = 10
        elif a in [7, 22, 36]:
            b = L_CH.pop()
            g(b)
            L_CH = [b] + L_CH
        elif a in [2, 17, 33]:
            b = L_CC.pop()
            g(b)
            L_CC = [b] + L_CC
        else:
            pass
    a %= 40
    d[a] += 1
L = [(i, d[i]) for i in d]
L.sort(key=lambda x: x[1])
print(L[-3:])


# %% Problem 85


def nb(m, n):
    """nb of rectangles contained in a n*m grid"""
    n *= n + 1
    m *= m + 1
    n //= 2
    m //= 2
    return n * m


nn = 2000000
limit = int((2*nn**0.5)**0.5)
mini = (limit, limit)
mm = abs(nb(*mini) - nn)
for m in range(1, limit):
    n = int((-1 + (1 + 16*nn / (m*(m+1)))**0.5) / 2)
    # we should verify both "sides" of the solution,
    # but it works this way ;p
    nb_ = nb(m, n)
    if abs(nb_-nn) < mm:
        mini = m, n
        mm = abs(nb_-nn)
print(mini[0]*mini[1])  # sol = 2772

# %% Problem 86


from math import sqrt
from Tools import is_square

c = 0
n = 0
while n < 10**6:
    c += 1
    for d in range(c+1, int(c*5**0.5+0.1)+1):
        if is_square(d**2-c**2):
                m = int((d**2-c**2)**0.5+0.1)
                if m <= c+1:
                    n += m//2
                else:
                    n += (2*c - m) // 2 + 1


# %% Problem 87

from Tools import numpy_sieve

l = [False for i in range(50000000)]

l_pp = list(numpy_sieve(7070))
for i in l_pp:
    for j in l_pp:
        for k in l_pp:
            n = i ** 2 + j ** 3 + k ** 4
            if n >= 50000000:
                break
            else:
                l[n] = True
        if i ** 2 + j ** 3 + 2**4 > 50000000:
            break

print(l.count(True))  # sol = 1097343


# %% Problem 88


def prod(l):
    p = 1
    for i in l:
        p *= i
    return p

LL = []
for k in range(2, 12001):
    mini = None
    L = [1]*k
    L[-1] = 2
    L[-2] = 2
    j = 1
    while j < k:
        while prod(L) < sum(L):
            L[-j] += 1
        if prod(L) == sum(L):
            if mini is None:
                mini = sum(L)
            elif sum(L) < mini:
                mini = sum(L)
        if j < k-1:
            L[-j - 1] += 1
            L[-j:] = [L[-j - 1]]*j
        j += 1
    if mini not in LL:
        LL.append(mini)
print(sum(LL))


# %% Problem 88

k_max = 12000

N = [2*k for k in range(2*k_max+1)]
D = [[] for k in range(2*k_max+1)]
for d in range(2, 2*k_max+1):
    for j in range(d, 2*k_max + 1, d):
        D[j].append(d)


def product(i, n, m):
    if len(D[m]) == 1:
        return [[n]]
    a = D[m][i]

    l = []
    for j in range(i, len(D[m])):
        b = D[m][j]
        if n % b == 0 and b ** 2 <= n:
            l.extend([[b] + a for a in product(j, n//b, m)])
        elif n == b:
            l.extend([[b]])

    if l == []:
        return [[n]]
    return l


def prod(l):
    p = 1
    for a in l:
        p *= a
    return p


def set_k(n):
    for l in product(0, n, n):
        k = prod(l) - sum(l) + len(l)
        if 2 <= k <= 12000:
            N[k] = min(N[k], n)

for n in range(4, 24000):
    set_k(n)

s = []
for k in range(2, k_max+1):
    if N[k] not in s:
        s.append(N[k])
print(sum(a for a in s))

# %% Problem 89

import os

os.chdir('/Users/maximin/Desktop/Euler/linked_files')
with open('p089_roman.txt', 'r') as f:
    s = 0
    for i in f:
        s += len(i[:-1])

        n = i.find("IIII")
        if n != -1:
            i = i[:n] + "IV" + i[n + 4:]

        n = i.find("VIV")
        if n != -1:
            i = i[:n] + "IX" + i[n + 3:]

        n = i.find("XXXX")
        if n != -1:
            i = i[:n] + "XL" + i[n + 4:]

        n = i.find("LXL")
        if n != -1:
            i = i[:n] + "XC" + i[n + 3:]

        n = i.find("CCCC")
        if n != -1:
            i = i[:n] + "CD" + i[n + 4:]

        n = i.find("DCD")
        if n != -1:
            i = i[:n] + "CM" + i[n + 3:]

        # ff.write(i)
        # print(i)
        s -= len(i[:-1])
    print(s)  # sol = 743

