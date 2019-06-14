# %% Problem 155
# long and took lot of memory space

from fractions import Fraction
L_tot = set()
L = [set(), {Fraction(1)}]
ONE = Fraction(1)


def add(l, a, b=ONE):
    if a+b not in L_tot:
        l.add(a+b)
        L_tot.add(a+b)
    if a*b/(a+b) not in L_tot:
        l.add(a*b/(a+b))
        L_tot.add(a*b/(a+b))


for i in range(2, 19):
    L2 = set()
    for c in L[i-1]:
        add(L2, c)
    for j in range(2, i//2+1):
        for c1 in L[j]:
            for c2 in L[i-j]:
                add(L2, c1, c2)
    L.append(L2)

print(sum(len(l) for l in L))
# sol = 3857447
