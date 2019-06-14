from Tools import numpy_sieve

c_max = 120000
lp = numpy_sieve(c_max)
l = [[] for _ in range(c_max)]
for p in lp:
    for k in range(p, c_max, p):
        l[k].append(p)


def prod(ll):
    pr = 1
    for el in ll:
        pr *= el
    return pr

rad = [prod(li) for li in l]

# a < b < c
s_tot = 0
l_tot = []

# a == 1
for c in range(3, c_max):
    b = c-1
    if rad[b] * rad[c] < c:
        s_tot += c
        l_tot.append(c)

# a > 1


def dis_join(a1, a2):
    for factor in l[a1]:
        if factor in l[a2]:
            return False
    return True

for c in range(4, c_max):
    if rad[c]*2*3 >= c:
        continue
    for b in range(c//2+1, c-1):
        if rad[c]*rad[b]*2 >= c:
            continue
        if not dis_join(b, c):
            continue
        a = c-b
        if dis_join(a, b) and dis_join(a, c) and rad[a]*rad[b]*rad[c] < c:
            s_tot += c
            l_tot.append(c)

print(s_tot)  # 18407904
# TODO : Breaks the 1-min rule.
