# %% Problem 425

from Tools import numpy_sieve

l7 = set(numpy_sieve(10**7))
s = dict()
seen = {p:False for p in l7}
greatest_prec = {p:-1 for p in l7}


p = [2]
while p.__len__() > 0:
    a = p.pop(0)
    if a < 10**6:
        for d in range(1, 10):
            b = int(str(d)+str(a))
            if b in l7:
                if not seen[b] or max(a, greatest_prec[a]) < greatest_prec[b]:
                    s[b] = max(a, greatest_prec[a])
                    seen[b] = False
                    p.append(b)
    for k in range(len(str(a))):
        for d in range(0, 10):
            b = int(str(a)[:k]+str(d)+str(a)[k+1:])
            if b in l7:
                if not seen[b] or max(a, greatest_prec[a]) < greatest_prec[b]:
                    s[b] = max(a, greatest_prec[a])
                    seen[b] = False
                    p.append(b)
