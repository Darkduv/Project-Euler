# %% Problem 90


from itertools import product

l_square = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (6, 4), (8, 1)]

l_i = list(product([0, 1], repeat=9))


def a_b(li):
    a = set()
    b = set()
    for k in range(9):
        a.add(l_square[k][li[k]])
        b.add(l_square[k][1 - li[k]])
    a = list(a)
    b = list(b)

    def aux(n, l):
        if n == 6:
            return [l[:]]
        else:
            ll = []
            for a in range(10):
                if a not in l:
                    for l2 in aux(n + 1, l + [a]):
                        ll.append(l2)
            return ll

    la = aux(len(a), a)
    if 6 in a:
        a.remove(6)
        a.append(9)
        la.extend(aux(len(a), a))
    lb = aux(len(b), b)
    if 6 in b:
        b.remove(6)
        b.append(9)
        lb.extend(aux(len(b), b))

    return product(la, lb)


L = []
for li in l_i:
    for a, b in a_b(li):
        a.sort()
        b.sort()
        if (a, b) not in L and (b, a) not in L:
            L.append((a, b))
print(len(L))  # sol = 1217

# %% Problem 91


from math import sqrt

lim = 50
n = 0
for x1 in range(1, lim + 1):
    for y1 in range(lim + 1):
        #  right angle at (0, 0) :
        if y1 == 0:
            n += lim

        # right angle at (x1, y1) :
        if y1 == 0:
            n += lim
        else:
            for x2 in range(x1):
                if ((x1 - x2) * x1) % y1 == 0:
                    if y1 + ((x1 - x2) * x1) // y1 <= lim:
                        n += 1

        # right angle at (x2, y2) :
        for x2 in range(x1):
            d = y1 ** 2 + 4 * x2 * (x1 - x2)
            if int(sqrt(d)) ** 2 == d:
                if (y1 + int(sqrt(d))) % 2 == 0:
                    if 0 < (y1 + int(sqrt(d))) // 2 <= lim:
                        n += 1
print(n)


# %% Problem 92

def aux92(n):
    s = 0
    while n != 0:
        s += (n % 10) ** 2
        n //= 10
    return s


nb = 0
for i in range(2, 10000000):
    while i != 1 and i != 89:
        i = aux92(i)
    if i == 89:
        nb += 1
print(nb)

# %% Problem 93:


lll = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            for kk in range(4):
                ok = True
                for test in range(4):
                    if test not in [i, j, k, kk]:
                        ok = False
                        break
                if ok:
                    lll.append([i, j, k, kk])

from fractions import Fraction

div = lambda a, b: a / b
div2 = lambda a, b: b / a
sub2 = lambda a, b: b - a

l_op = [div, Fraction.__add__, Fraction.__sub__, Fraction.__mul__, div2, sub2]
truc = []


def maxi(a, b, c, d):
    l = []
    ll = [Fraction(a, 1), Fraction(b, 1), Fraction(c, 1), Fraction(d, 1)]
    for i, j, k, kk in lll:
        aa, bb, cc, dd = ll[i], ll[j], ll[k], ll[kk]
        for f1 in l_op:
            try:
                for f2 in l_op:
                    s2 = f1(aa, bb)
                    try:
                        for f3 in l_op:
                            s3 = f2(s2, cc)
                            try:
                                s = f3(s3, dd)
                                if s._denominator == 1 and int(s) not in l:
                                    l.append(int(s))
                                    truc.append((int(s), int(aa), int(bb), int(cc), int(dd), f1, f2))
                            except:
                                pass
                    except:
                        pass
            except:
                pass

    test = 1
    while test in l:
        test += 1
    return test - 1


mmm = 0
set_max = [0, 0, 0, 0]

l_test = []
for a in range(1, 10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            for d in range(c + 1, 10):
                m = maxi(a, b, c, d)
                if m > mmm:
                    mmm = m
                    set_max = [a, b, c, d]
                l_test.append([m, a, b, c, d])
l_test.sort()
for i in l_test[::-1]:
    print(i)

a, b, c, d = set_max
print(1000 * a + 100 * b + 10 * c + d)


# 1258


# %% Problem_94
maxi = 10**9

def probl_94_1():  # a, a, a+1,   a = 4c^2+1.  3c^2+1=y^2 and perimeter = 4y^2
    # c, y = 0, 1 -> 1, 2 -> 4, 7.... y_n+1 = 6x_n + y_n-1 and x_n+1=2y_n+x_n-1
    c0, y0 = 0, 1
    c1, y1 = 1, 2
    s = 0  # triangle 1,1,2 is not a triangle ;)
    while 4*y1**2 <= maxi:
        s += y1**2
        y1, c1, y0, c0 = 6*c1+y0, 2*y1+c0, y1, c1
    return 4*s


s_plus = probl_94_1()


# 109552588


def probl_94_2():  # a, a, a-1
    # a = 2c^2-1.  3c^2-2=y^2 and perimeter = 2y^2
    # c, y = 1, 1 -> 3, 5 -> 11, 19.... y_n+1 = 6x_n + y_n-1 and x_n+1=2y_n+x_n-1
    c0, y0 = 1, 1
    c1, y1 = 3, 5
    s = 0  # triangle 1,1,0 is not a triangle ;)
    while 4 * y1 ** 2 <= maxi:
        s += y1 ** 2
        y1, c1, y0, c0 = 6 * c1 + y0, 2 * y1 + c0, y1, c1
    return 2 * s

s_moins = probl_94_2()
# 408855758
print(s_plus + s_moins)
# sol = 518408346


# %% Problem 95

from Tools import sum_divisor


def sum_divisor_proper(m):
    return sum_divisor(m) - m


L_sum = [1] * 10 ** 6
L_sum[0] = -1
for p in range(2, 10 ** 6):
    for k in range(2 * p, 10 ** 6, p):
        L_sum[k] += p

L_by_class = []
L_already_seen = [False] * 10 ** 6

for i, n in enumerate(L_sum):
    if n == 1 or n == -1:
        continue
    if n < 10 ** 6 and not L_already_seen[n]:
        l_n = [i, n]
        L_already_seen[i] = True
        L_already_seen[n] = True
        j = L_sum[n]
        while j not in l_n and j < 10 ** 6 + 1:
            if j == -1:
                l_n = []
                break
            L_already_seen[j] = True
            l_n.append(j)
            j = L_sum[j]

        if j in l_n:
            l_n = l_n[l_n.index(j):]
            L_by_class.append(l_n)

i_max = 0
l_max = 0
for i, l in enumerate(L_by_class):
    ln = len(l)
    if ln > l_max:
        i_max = i
        l_max = ln
print(min(L_by_class[i_max]))
# k_max = 14316


# %% Problem 96

from os import chdir

chdir("/Users/tessie/Desktop/Euler")

with open("p096_sudoku.txt", 'r') as f:
    i = -1
    l_sudoku = []
    for s in f:
        i += 1
        i %= 10
        if i != 0:
            l = []
            for nb in s:
                try:
                    l.append(int(nb))
                except ValueError:
                    pass
            if i == 1:
                l_sudoku.append([l.copy()])
            else:
                l_sudoku[-1].append(l.copy())

# # # # # # SEE Solution in Caml Light

# %% Problem 97

n = pow(2, 7830457, 10**10)
n *= 28433
n += 1
n %= 10 ** 10
print(n)  # sol = 8739992577

# %% Problem 98

from Tools import is_square
from os import chdir

chdir("/Users/maximin/Desktop/Euler/linked_files")

s = ""
with open("p098_words.txt") as f:
    for i in f:
        s = i
L_words = list(eval(s))

d = {}
for s in L_words:
    a = list(s)
    a.sort()
    a = tuple(a)
    if a in d:
        d[a].append(s)
    else:
        d[a] = [s]

l_anagrams = []
for a in d:
    if len(d[a]) > 1:
        l_anagrams.append(d[a])

def find_well_distr(s):
    def find_distrib(s):
        if s == "":
            return [dict()]
        l = []
        for dictio in find_distrib(s[1:]):
            if s[0] in dictio:
                l.append(dictio)
            else:
                for i in range(10):
                    if i not in dictio.values():
                        d = dictio.copy()
                        d[s[0]] = i
                        l.append(d)
        return l

    ll = find_distrib(s)
    l_well = []
    for dictio in ll:
        if dictio[s[0]] == 0:
            continue
        l = [str(dictio[lettre]) for lettre in s]
        nb = int("".join(l))
        if is_square(nb):
            l_well.append(dictio)
    return l_well


def square_anagram(L):
    LL = [find_well_distr(s) for s in L]
    for i in LL[0]:
        if i in LL[1]:
            return True
    return False


L_square = []
for L in l_anagrams:
    if len(L) > 2:
        print(L)
    else:
        if square_anagram(L):
            L_square.append(L)


def find_square_max(L):
    try:
        LL = [find_well_distr(s) for s in L]
        L_ok = []
        for i in LL[0]:
            if i in LL[1]:
                L_ok.append(i)
        L_nb = []
        for dictio in L_ok:
            L_nb.append(int("".join([str(dictio[lettre]) for lettre in L[0]])))
            L_nb.append(int("".join([str(dictio[lettre]) for lettre in L[1]])))
        try:
            m = max(L_nb)
        except ValueError:
            print(L)
            raise ValueError
        return m
    except KeyError:
        print(L)
        raise KeyError


print(max([find_square_max(L) for L in L_square]))

# %% Problem 99

from math import log
from os import chdir

chdir("/Users/maximin/Desktop/Euler/linked_files")

aa, bb = 2, 2
i_max = -1

with open("p099_base_exp.txt", 'r') as f:
    i = 1
    for s in f:
        a, b = eval(s)
        if b * log(a) > bb * log(aa):
            bb, aa = b, a
            i_max = i
        i += 1

print(i_max) # sol = 709
