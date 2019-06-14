# %% Problem 345
string = """  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805"""

s = string.split('\n')
mat = []
for sa in s:
    mat.append([int(a) for a in sa.split(" ") if a != ""])


def next_permut(l):
    i = 0
    n = len(l)
    ok = False
    while i + 1 < n:
        if l[i] > l[i+1]:
            ok = True
            break
        i += 1
    if ok:
        a = l[i+1]
        m = min([el for el in l[:i+1] if el > a])
        j = l.index(m)
        l[j] = a
        return l[i::-1] + [m] + l[i+2::]

l = [4, 3, 9, 7, 0, 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 14]

mat_sum = 0
while True:
    s = sum([mat[i][l[i]] for i in range(15)])
    if s > mat_sum:
        mat_sum = s
    if l == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14][::-1]:
        break
    l = next_permut(l[::-1])[::-1]


def mat_sum(mat, Li, Lj):
    if len(Li) == 1:
        i1 = Li[0]
        i2 = Lj[0]
        return mat[i1][i2]
    else:
        maxi = 0
        for j in range(len(Li)):
            if len(Li) == 15:
                print(j)
            b = mat[Li[0]][Lj[j]]
            if b > 600:
                s = mat_sum(mat, Li[1:], Lj[:j]+Lj[j+1:])
                a = s + mat[Li[0]][Lj[j]]
                if a > maxi:
                    maxi = a
        return maxi

print(mat_sum(mat, list(range(15)), list(range(15))))

# %% Problem 346

from math import log2

N = 10**12
p_max = int(N**0.5)


def k_max(p):
    n = int(log2(N*(p-1)+1)/log2(p)+0.1)
    a = (p**(n+1)-1)//(p-1)
    while a > N:
        n -= 1
        a = (p**(n+1)-1)//(p-1)
    return n


def sum_p(p):
    k = k_max(p)
    return ((1-k)*(p-1) + p**(k+2) - p**3)//((p-1)**2)

s = 0
for p in range(2, p_max+1):
    s += sum_p(p)
s += 1
s -= 31 + 8191
# sol = 336108797689259276


# %% Problem 347

from math import log
from Tools import numpy_sieve
l = numpy_sieve(10**7)

S = 0
n = len(l)
for i in range(n):
    for j in range(i+1, n):
        p = l[i]
        q = l[j]
        a1, a2 = 1, int(log(10**7/p)/log(q))
        if a2 != 0:
            nb_max = p**a1 * q ** a2
            while a1 < int(log(10**7/q)/log(p)):
                a1 += 1
                while p**a1 * q ** a2 > 10**7 and a2 > 1:
                    a2 -= 1
                if p**a1 * q ** a2 > nb_max:
                    nb_max = p**a1 * q ** a2
            S += nb_max
# i < 1432
# S = 11109800204052


# %% Problem 348

from Tools import palindromic
d = {}
for a in range(700):
    for b in range(30000):
        dd = a ** 3 + b ** 2
        if palindromic(dd):
            d[dd] = 1 + d.get(dd, 0)
print(sum([i for i in d if d[i] == 4]))  # sol = 1004195061

# or

lim = 900000000
d = {}
for a in range(1, int(lim**(1/3))+1):
    for b in range(1, int((lim-a**3)**0.5)+1):
        dd = a ** 3 + b ** 2
        if palindromic(dd):
            d[dd] = 1 + d.get(dd, 0)
print(sum([i for i in d if d[i] == 4]))


# %% Problem 349
def clock(a):
    if a == (0, 1):
        return 1, 0
    elif a == (-1, 0):
        return 0, 1
    elif a == (0, -1):
        return -1, 0
    else:
        return 0, -1

def contrclock(a):
    if a == (1, 0):
        return 0, 1
    elif a == (0, 1):
        return -1, 0
    elif a == (-1, 0):
        return 0, -1
    else:
        return 1, 0

nb = 0
mat = [[1]*100001 for _ in range(100001)]
i = 50000
j = 50000
sens = (0, 1)

for t in range(10**18):
    if mat[i][j] == 0:
        mat[i][j] = 1
        nb -= 1
        sens = contrclock(sens)

    else:
        mat[i][j] = 0
        nb += 1
        sens = clock(sens)
    a, b = sens
    i += a
    j += b
    if i > 100000 or j > 100000 or i < 0 or j < 0:
        print("ouille", t)
        break

print(nb)