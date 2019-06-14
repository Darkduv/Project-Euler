# %% Problem 135

from itertools import product
from Tools import numpy_sieve, decompose_tout, timing


@timing
def p135():
    l_p = numpy_sieve(10**6)

    def nb_ok(n):
        l = decompose_tout(n, l_p)
        n_l = len(l)

        l2 = []
        nb_div = 0
        for i in range(n_l):
            l2.append(list(range(l[i][1]+1)))
        for c in product(*l2):
            a = 1
            for i in range(n_l):
                a *= l[i][0]**c[i]
            if 3*a**2-n > 0:
                nb_div += 1
        return nb_div

    l = []
    nb = 0
    for n in range(1155, 10**6):
        if n % 4 == 3 and nb_ok(n) == 10:
            nb += 1
            l.append(n)
        if n % 4 == 0:
            if n % 8 != 0:
                if nb_ok(n//4) == 10:
                    nb += 1
                    l.append(n)
            elif n % 16 == 0:
                if nb_ok(n//16) == 10:
                    l.append(n)
                    nb += 1
    print(nb)
    # print(l)

p135()  # 4989
