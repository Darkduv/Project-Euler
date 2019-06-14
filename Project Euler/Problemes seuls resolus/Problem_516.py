# %% Problem 516

from math import log
from Tools import numpy_sieve, binary_search_inf
l6 = numpy_sieve(10**6)
l = 10**12


def is_prime(test):
    for pp in l6:
        if test < pp**2:
            return True
        if test % pp == 0:
            return False
    return True

lp = []
am = log(l+1)/log(2)
for a in range(int(am)+1):
    bm = (log(l+1) - a*log(2))/log(3)
    for b in range(int(bm)+1):
        cm = (log(l+1) - a*log(2) - b * log(3))/log(5)
        for c in range(int(cm)+1):
            n = 2**a*3**b*5**c
            if n+1 in [2, 3, 5]:
                continue
            if n > l+1:
                break
            if is_prime(n+1):
                lp.append(n+1)
lp.sort()

len_lp = len(lp)
lp2 = []
for i1 in range(len_lp):
    p1 = lp[i1]
    lp2.append(p1)
    for i2 in range(i1+1, len_lp):
        p2 = lp[i2]
        if p2*p1 > l:
            break
        lp2.append(p2*p1)
        for i3 in range(i2 + 1, len_lp):
            p3 = lp[i3]
            if p2 * p1*p3 > l:
                break
            lp2.append(p2 * p1*p3)
            for i4 in range(i3 + 1, len_lp):
                p4 = lp[i4]
                if p2 * p1 * p3 * p4 > l:
                    break
                lp2.append(p2 * p1 * p3 * p4)
                for i5 in range(i4 + 1, len_lp):
                    p5 = lp[i5]
                    if p2 * p1 * p3 * p4 * p5 > l:
                        break
                    lp2.append(p2 * p1 * p3 * p4 * p5)
                    for i6 in range(i5 + 1, len_lp):
                        p6 = lp[i6]
                        if p2 * p1 * p3 * p4 * p5 * p6 > l:
                            break
                        lp2.append(p2 * p1 * p3 * p4 * p5 * p6)
                        for i7 in range(i6 + 1, len_lp):
                            p7 = lp[i7]
                            if p2 * p1 * p3 * p4 * p5 * p6 * p7 > l:
                                break
                            lp2.append(p2 * p1 * p3 * p4 * p5 * p6 * p7)
                            for i8 in range(i7 + 1, len_lp):
                                p8 = lp[i8]
                                if p2 * p1 * p3 * p4 * p5 * p6 * p7 * p8 > l:
                                    break
                                lp2.append(p2 * p1 * p3 * p4 * p5 * p6 * p7 * p8)
                                for i9 in range(i8 + 1, len_lp):
                                    p9 = lp[i9]
                                    if p2 * p1 * p3 * p4 * p5 * p6 * p7 * p8 * p9 > l:
                                        break
                                    lp2.append(p2 * p1 * p3 * p4 * p5 * p6 * p7 * p8 * p9)

lp2.sort()

l2 = []
am = log(l)/log(2)
for a in range(int(am)+1):
    if a >= 32:
        break
    bm = (log(l) - a*log(2))/log(3)
    for b in range(int(bm)+1):
        cm = (log(l) - a*log(2) - b * log(3))/log(5)
        for c in range(int(cm)+1):
            n = 2**a*3**b*5**c
            if n > l:
                break
            l2.append(n)
l2.sort()

s = sum(l2) % 2**32
for p in lp2:
    k = binary_search_inf(l2, 10**12/p)
    s += p*sum(l2[:k+1])
    s %= 2**32
print(s)  # 939087315
