# %% Problem 100

# see https://www.alpertron.com.ar/QUAD.HTM

b = 85
n = 120

while n < 10 ** 12:
    b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3
print(b)  # sol = 756872327473

# %% Problem 102

from math import atan, pi

from os import chdir

chdir("/Users/maximin/Desktop/Euler/linked_files")

with open('p102_triangles.txt', 'r') as f:
    l = []
    for i in f:
        l.append(list(eval(i)))


def arg(a, b):
    if a == 0:
        if b >= 0:
            return pi / 2
        else:
            return 3 * pi / 2
    elif a > 0:
        theta = atan(b / a)
        if theta < 0:
            theta += 2 * pi
        return theta
    else:
        theta = pi + atan(b / a)
        if theta < 0:
            theta += 2 * pi
        return theta


def origin_is_in(l_arg):
    l_arg.sort()
    return l_arg[1] - l_arg[0] <= pi and l_arg[2] - l_arg[1] <= pi and l_arg[0] - l_arg[2] + 2 * pi <= pi

n_in = 0
for el in l:
    ll = [arg(*el[2 * i:2 * i + 2]) for i in range(3)]
    n_in += origin_is_in(ll)

print(n_in)  # sol = 228


# %% Problem 103


def sub(L, k, n):
    if k == n:
        return L
    LL = []
    for i in L:
        LL.append(i + [k])
    L += LL
    LL = []
    for i in L:
        for j in sub([i], k + 1, n):
            if j not in L:
                LL.append(j)
    L += LL
    if [] in L:
        L.remove([])
    return L


L = sub([[]], 0, 7)


def ok(A):
    for i in L:
        for j in L:
            if i != j:
                B = []
                C = []
                for el in i:
                    B.append(A[el])
                for el in j:
                    C.append(A[el])
                if sum(B) == sum(C):
                    return False
                elif len(B) > len(C):
                    if sum(B) < sum(C):
                        return False
    return True


# bis

mini = 255
l_test = []
for a1 in range(1, 70):
    for a2 in range(a1 + 1, 120):
        for a3 in range(a2 + 1, min(121, a1 + a2 + 1)):
            for a4 in range(a3 + 1, min(122, a1 + a2 + 1)):
                if a1 + a4 == a2 + a3 or a1 + a3 == a4 + a2:
                    continue
                for a5 in range(a4 + 1, min(123, a1 + a2 + 1)):
                    if a1 + a5 == a2 + a3 or a1 + a5 == a2 + a4:
                        continue
                    for a6 in range(a5 + 1, min(124, a1 + a2 + 1)):
                        for a7 in range(a6 + 1, min(125, a1 + a2 + 1)):
                            if a1 + a7 + a4 == a2 + a3 + a6:
                                continue
                            if a1 + a2 + a3 + a4 <= a5 + a6 + a7:
                                break
                            if a1 + a2 + a3 + a4 + a5 + a6 + a7 > mini:
                                break
                            else:
                                l_test.append([a1, a2, a3, a4, a5, a6, a7])

                        if a1 + a2 + a3 + a4 + a5 + 2 * a6 + 1 > mini:
                            break
                    if a1 + a2 + a3 + a4 + 3 * a5 + 3 > mini:
                        break
                if a1 + a2 + a3 + 4 * a4 + 6 > mini:
                    break
            if a1 + a2 + 5 * a3 + 10 > mini:
                break
        if a1 + 6 * a2 + 15 > mini:
            break
    if 7 * a1 + 21 > mini:
        break


def tri5(l):
    return sum(l[:4]) > sum(l[4:])


l_test5 = [i for i in l_test if tri5(i)]


def tri6(L):
    for i in range(7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                for kk in range(k + 1, 7):
                    if L[i] + L[kk] == L[j] + L[k] or L[j] + L[kk] == L[i] + L[k]:
                        return False
    return True


l_test6 = [i for i in l_test5 if tri6(i)]


def tri7(L):
    for i in range(7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                for ii in range(k + 1, 7):
                    for jj in range(ii + 1, 7):
                        for kk in range(jj + 1, 7):
                            if L[i] + L[kk] + L[j] == L[k] + L[ii] + L[jj]:
                                return False
                            elif L[i] + L[kk] + L[k] == L[j] + L[ii] + L[jj]:
                                return False
                            elif L[i] + L[kk] + L[ii] == L[j] + L[k] + L[jj]:
                                return False
                            elif L[i] + L[kk] + L[jj] == L[j] + L[k] + L[ii]:
                                return False
                            elif L[i] + L[jj] + L[j] == L[k] + L[ii] + L[kk]:
                                return False
                            elif L[i] + L[jj] + L[k] == L[j] + L[ii] + L[kk]:
                                return False
                            elif L[i] + L[jj] + L[ii] == L[j] + L[k] + L[kk]:
                                return False
                            elif L[i] + L[ii] + L[j] == L[k] + L[jj] + L[kk]:
                                return False
                            elif L[i] + L[ii] + L[k] == L[j] + L[jj] + L[kk]:
                                return False
    return True


l_test7 = [i for i in l_test6 if tri7(i)]
print(len(l_test7))

mini = sum(l_test7[0])
l_min = l_test7[0]
for i in l_test7:
    if sum(i) < mini:
        mini = sum(i)
        l_min = i
print(l_min)

ss = [str(i) for i in l_min]
s = "".join(ss)
print(s)

# s = 20313839404245

# %% Problem 104


from math import log10


def ok2(n):
    l = []
    nn = int(log10(n))
    if nn < 9:
        return False
    while len(l) != 9:
        r, n = int.__divmod__(n, 10 ** nn)
        l.append(r)
        nn -= 1
    for i in range(9):
        if i not in l:
            return False
    return True


def ok1(n):
    l = []
    while n != 0:
        l.append(n % 10)
        n //= 10
    for i in range(1, 10):
        if i not in l[-9:]:
            return False
    return True


L = []
a, b, k = 1, 1, 1
while k < 10 ** 7:
    a, b, k = b % (10 ** 9), (b + a) % (10 ** 9), k + 1
    if ok1(a):
        L.append(k)

a, b, k = 1, 1, 1
while k <= L[-1]:
    a, b, k = b, b + a, k + 1
    if k in L:
        if ok2(a):
            print(k)
            break

# sol = 329468

# %% Problem 105

from os import chdir

chdir("/Users/maximin/Desktop/Euler")

l_sets = []
with open('p105_sets.txt', 'r') as f:
    for i in f:
        l = list(eval(i))
        l.sort()
        l_sets.append(l)


def tri1(l):
    if len(l) % 2 == 1:
        d = len(l) // 2
        return sum(l[:d + 1]) > sum(l[d + 1:])
    else:
        d = len(l) // 2
        return sum(l[:d + 1]) > sum(l[d:])


def tri2(L):
    d = len(L)
    for i in range(d):
        for j in range(i + 1, d):
            for k in range(j + 1, d):
                for kk in range(k + 1, d):
                    if L[i] + L[kk] == L[j] + L[k] or L[j] + L[kk] == L[i] + L[k]:
                        return False
    return True


def tri3(L):
    d = len(L)
    for i in range(d):
        for j in range(i + 1, d):
            for k in range(j + 1, d):
                for ii in range(k + 1, d):
                    for jj in range(ii + 1, d):
                        for kk in range(jj + 1, d):
                            if L[i] + L[kk] + L[j] == L[k] + L[ii] + L[jj]:
                                return False
                            elif L[i] + L[kk] + L[k] == L[j] + L[ii] + L[jj]:
                                return False
                            elif L[i] + L[kk] + L[ii] == L[j] + L[k] + L[jj]:
                                return False
                            elif L[i] + L[kk] + L[jj] == L[j] + L[k] + L[ii]:
                                return False
                            elif L[i] + L[jj] + L[j] == L[k] + L[ii] + L[kk]:
                                return False
                            elif L[i] + L[jj] + L[k] == L[j] + L[ii] + L[kk]:
                                return False
                            elif L[i] + L[jj] + L[ii] == L[j] + L[k] + L[kk]:
                                return False
                            elif L[i] + L[ii] + L[j] == L[k] + L[jj] + L[kk]:
                                return False
                            elif L[i] + L[ii] + L[k] == L[j] + L[jj] + L[kk]:
                                return False
    return True


from random import shuffle


def tri_plus(l):
    if len(l) < 8:
        return True
    for j in range(4, len(l) // 2 + 1):
        for k in range(100000):
            ll = l.copy()
            shuffle(ll)
            if sum(ll[:j]) == sum(ll[j:2 * j]):
                return False
    return True


l_sets2 = [i for i in l_sets if tri1(i)]
l_sets3 = [i for i in l_sets2 if tri2(i)]
l_sets4 = [i for i in l_sets3 if tri3(i)]
l_sets5 = [i for i in l_sets4 if tri_plus(i)]
print(len(l_sets5))
l_sets6 = [i for i in l_sets5 if tri_plus(i)]
print(len(l_sets6))

s = 0
for i in l_sets6:
    s += sum(i)
print(s)


# %% Problem 106


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def cPn(p, n):
    return fact(n) // (fact(p) * fact(n - p))


def ok33(n):
    return sum([cPn(2 * i, n) * cPn(i, 2 * i) for i in range(1, n // 2 + 1)])


def nb_tot(n):
    return ok33(n) // 2


def ok(k, i_min, j_min, n, l):
    if i_min >= j_min:
        return 0
    if n - i_min < 2 * k:
        return 0
    if n - j_min < k:
        return 0
    if k == 0:
        return 1
    s = 0
    for i in range(i_min + 1, n - 2 * k + 2):
        if i not in l:
            for j in range(max(j_min + 1, i + 1), n - k + 2):
                s += ok(k - 1, i, j, n, l + [j])
    return s


def nb_ok(k, n):
    return ok(k, 0, 1, n, [])


def nb_tot_ok(n):
    s = 0
    for k in range(1, n // 2 + 1):
        s += nb_ok(k, n)
    return s


print("Problem 106: ", nb_tot(12) - nb_tot_ok(12))

# %% Problem 107


from time import time

timer = time()
from os import chdir

chdir("/Users/maximin/Desktop/Euler/linked_files")

f = open('p107_network.txt')
m = []
infini = float('inf')

for line in f.readlines():
    l = line.split(",")
    m.append([])
    for c in l[:-1]:
        if c == "-":
            m[-1].append(infini)
        else:
            m[-1].append(int(c))
f.close()

n = len(m)

u = 0

for i in range(n):
    for j in range(i):
        if m[i][j] < infini:
            u += m[i][j]

aretes = []

for i in range(n):
    for j in range(i):
        if m[i][j] < infini:
            aretes.append((m[i][j], i, j))

aretes = sorted(aretes)


def fusionner_composantes(c, i, j):
    x = c[j]
    y = c[i]
    if x != y:
        for k in range(len(c)):
            if c[k] == x:
                c[k] = y


poids = 0
compo = [i for i in range(n)]

for a in aretes:
    p, i, j = a
    if compo[i] != compo[j]:
        poids += p
        fusionner_composantes(compo, i, j)

print(u - poids)
print(time() - timer)

with open('matrice.ml', 'w') as f:
    s = ""
    s += "[|"
    for l in m:
        s += "[|"
        for i in l:
            if i is not None:
                s += str(i)
            else:
                s += "-1"
            s += ";"
        s = s[:-1]
        s += "|];\n"
    s = s[:-2]
    s += "|]"
    f.write(s)


# %% Problem 108


def sol(n):
    nb = 0
    x = n + 1
    while x <= 2 * n:
        if (n * x) % (x - n) == 0:
            nb += 1
        x += 1
    return nb


n = 1000
while sol(n) < 1000:
    n += 1
print(n)


# %% Problem 109


def dart():
    for i in range(1, 21):
        for k in range(1, 4):
            yield "SDT"[k - 1] + str(i), i * k, k == 2
    for k in range(1, 3):
        yield "SD"[k - 1] + "25", 25 * k, k == 2


def p109(maxi, mini=0):
    L = []
    n = 0
    for d1, s1, ok1 in dart():
        if mini <= s1 <= maxi and ok1:
            n += 1
            # print(d1)
        if s1 > maxi:
            continue
        for d2, s2, ok2 in dart():
            if mini <= s1 + s2 <= maxi and ok2:
                n += 1
                # print(d1, d2)
            if s1 + s2 > maxi:
                continue
            for d3, s3, ok3 in dart():
                s = s1 + s2 + s3
                if mini <= s <= maxi and ok3 and (d1, d2, s) not in L and (d2, d1, s) not in L:
                    L.append((d1, d2, s))
                    n += 1
                    # print(d1, d2, d3)
    return n


print(p109(100))

# %% Problem 110

# all the following code is useless:
# the number of solution for x (so we have to divise by 2 the total) is the number of divisor of n ** 2 ...
# And the number of divisor of n ** 2 is : prod(2*a_i+1, i, 1, m)
# where n = prod(p_i ** a_i, i, 1, m) with p_1, p_2 ...p_m primes
# here we want prod(2*a_i+1, i, 1, m) > 4 000 000 * 2


from time import time


def factor110(n):
    if n % 2 == 0:
        return 2, n // 2
    i = 3
    while i ** 2 <= n and n % i != 0:
        i += 2
    if n % i == 0:
        return i, n // i
    else:
        return n, 1


def nb_d(n):
    nb = 0
    for i in range(1, n + 1):
        if n % i == 0:
            nb += 1
    return nb


timer = time()
L_true = []
for i in range(10 ** 4):
    L_true.append(nb_d(i))
print(time() - timer)

timer = time()
L_test = [0, 1, 2]
for j in range(3, 10 ** 7):
    p, a = factor110(j)
    s = L_test[a] * 2
    if a % p == 0:
        a //= p
        s -= L_test[a]
    L_test.append(s)
print(time() - timer)


def nb_d_proof1(n):
    p, a = factor110(n)
    if a < 10 ** 7:
        s = L_test[a] * 2
        if a % p == 0:
            s -= L_test[a // p]
    else:
        s = nb_d_proof1(a) * 2
        if a % p == 0:
            s -= nb_d_proof1(a // p)
    return s


def nb_d_proof2(n):
    p, a = factor110(n)
    if a * n < 10 ** 7:
        s = L_test[a * n] * 2 - L_test[a * a]
    else:
        ss = nb_d_proof2(a) * 2
        if a % p == 0:
            ss -= nb_d_proof1(a * (a // p))
        s = ss * 2 - nb_d_proof2(a)
    return s


n = 1250
while True:
    n += 1
    if nb_d_proof2(n) // 2 > 1000:
        print(n, nb_d_proof2(n))
        break

# %% Problem 111

# see single-solved problems


# %% Problem 112


def aux(n):
    l = []
    while n != 0:
        l.append(n % 10)
        n //= 10
    return l[::-1]


def ok(n):
    def ok_(l):
        i0 = l[0]
        for i in l:
            if i0 > i:
                return False
            i0 = i
        return True

    l = aux(n)
    if not ok_(l):
        return ok_(l[::-1])
    else:
        return True


n = 100
nb = 0
nb_tot = 100
while nb_tot * 99 != nb * 100:
    n += 1
    nb_tot += 1
    if not ok(n):
        nb += 1
print(n)


# %% Problem 113


def c_p_n(p, n):
    prod = 1
    b = 1
    for i in range(1, p + 1):
        prod *= n - i + 1
        b *= i
    return prod // b


def f1(n):
    s = 0
    for nk in range(1, 11):
        s += c_p_n(nk - 1, n - 1) * c_p_n(nk, 10)
    return s


def f2(n):
    s = 0
    for nk in range(1, 12):
        s += c_p_n(nk - 1, n - 1) * c_p_n(nk, 11)
    return s


def f(n):
    return f1(n) + f2(n) - 11 - 9 * (n - 1) - n


print(f(100))
# print(f(10))
# print(f(6))

# %% Problem 114

C = [1, 1, 1, 2]
for n in range(4, 51):
    C.append(C[-1] + sum(C[0:-3]) + 1)
print(C[-1])  # sol = 16475640049

# %% Problem 115

N = 50
C = [1 for _ in range(N)]
a = 2
n = N
while a < 10 ** 6:
    n += 1
    C.append(a)
    a += sum(C[0:-N]) + 1
print(n)


# %% Problem 118

from Tools import numpy_sieve, binary_search_inf
l_8 = numpy_sieve(10**8)


nb_tot = [[[] for _ in range(10)] for k in range(10)]

for n in range(1, 10):
    nb_tot[n][1] = [[1]*n]
    for maxi in range(2, n+1):
        for m2 in range(0, maxi+1):
            nb_tot[n][maxi].extend([a+[maxi] for a in nb_tot[n-maxi][m2]])
    nb_tot[n][n].append([n])

nb_tot9 = []
for maxi in range(1, 10):
    for a in nb_tot[9][maxi]:
        if a not in nb_tot9:
            nb_tot9.append(a)
nb_tot9.sort()
nb_tot9 = [a for a in nb_tot9 if a.count(1) <= 4]


def ok(p):
    pp = str(p)
    for c in pp:
        if c == '0':
            return False
        if pp.count(c) > 1:
            return False
    return True


l8bis = [prime for prime in l_8 if ok(prime)]
primes = [[]]
i = 0
k0 = 1
while k0 <= 8:
    j = binary_search_inf(l8bis, 10**k0)
    primes.append(l8bis[i:j+1])
    i = j+1
    k0 += 1


def _in(p):
    p = str(p)
    ll = list(p)
    ll.sort()
    return "".join(ll)


dict_in = [{} for _2 in range(10)]
for prime in l8bis:
    nb_d = len(str(prime))
    ss = _in(prime)
    if ss in dict_in[nb_d]:
        dict_in[nb_d][ss].append(int(prime))
    else:
        dict_in[nb_d][ss] = [int(prime)]


def apply_pattern_ok(not_used, li, la):
    if not li:
        la.sort()
        la = "X".join(la)
        if la not in l:
            l.append(la)
        return
    b = li[0]
    for key in dict_in[b]:
        not_this = False
        for char in key:
            if char not in not_used:
                not_this = True
                break
        if not_this:
            continue
        not_used2 = not_used[:]
        for d in key:
            not_used2.remove(d)
        for p in dict_in[b][key]:
            apply_pattern_ok(not_used2, li[1:], la + [str(p)])


l = []
not_use = list("123456789")
for l_i in nb_tot9:
    apply_pattern_ok(not_use, l_i, [])


print(len(l))


# %% Problem 119

i = 2
l = []
while len(l) < 100:
    n = 1
    while n <= 100:
        s = i ** n
        if log10(s) >= 1 and sum(int(a) for a in str(s)) == i:
            l.append(s)
        n += 1
        """
        if n >= 50:
            print(i)
            break
        """
    i += 1
l.sort()
print(l[29])
