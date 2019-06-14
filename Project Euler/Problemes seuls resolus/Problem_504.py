# %% Problem 504

from Tools import is_square


m = 100


def f(a, b):
    n = 0
    for k in range(1, a):
        n += (b*k-1)//a
    return n


dic = dict()

for aa in range(1, m+1):
    for bb in range(1, m+1):
        dic[(aa, bb)] = f(aa, bb)


def nb(a, b, c, d):
    s = 0
    s += dic[(a, b)]
    s += dic[(b, c)]
    s += dic[(c, d)]
    s += dic[(d, a)]
    s += a+b+c+d-3
    return s


ll = []
for aa in range(1, m+1):
    for bb in range(aa+1, m+1):
        for cc in range(aa+1, m+1):
            for dd in range(bb, m+1):
                if is_square(nb(aa, bb, cc, dd)):
                    ll.append((aa, bb, cc, dd))

n_tot = 0
for aa, bb, cc, dd in ll:
    if bb == dd:
        n_tot += 1
        # print(aa, bb, cc, dd, "ll", 1)
    else:
        n_tot += 2
        # print(aa, bb, cc, dd, "ll", 2)
n_tot *= 4

ll2 = []
for aa in range(1, m+1):
    bb = aa
    for cc in range(aa+1, m+1):
        for dd in range(cc, m+1):
            if is_square(nb(aa, bb, cc, dd)):
                ll2.append((aa, bb, cc, dd))

for aa, bb, cc, dd in ll2:
    if cc == dd:
        n_tot += 4
        # print(aa, bb, cc, dd, "ll2", 4)
    else:
        n_tot += 8
        # print(aa, bb, cc, dd, "ll2", 8)

ll3 = []
for aa in range(1, m+1):
    cc = aa
    for bb in range(aa+1, m+1):
        for dd in range(bb, m+1):
            if is_square(nb(aa, bb, cc, dd)):
                ll3.append((aa, bb, cc, dd))

for aa, bb, cc, dd in ll3:
    if bb == dd:
        n_tot += 2
        # print(aa, bb, cc, dd, "ll3", 2)
    else:
        n_tot += 4
        # print(aa, bb, cc, dd, "ll3", 4)

ll4 = []
for aa in range(1, m+1):
    cc = aa
    bb = aa
    for dd in range(bb, m+1):
        if is_square(nb(aa, bb, cc, dd)):
            ll4.append((aa, bb, cc, dd))

for aa, bb, cc, dd in ll4:
    if bb == dd:
        n_tot += 1
        # print(aa, bb, cc, dd, "ll4", 1)
    else:
        n_tot += 4
        # print(aa, bb, cc, dd, "ll4", 4)

print(n_tot)

# sol = 694687
