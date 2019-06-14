# %% 500

from math import log
from Tools import numpy_sieve, quick_expo


def problem_500(exp_div=500500):
    L = numpy_sieve(10**7)
    modulo = 500500507  # n_max = 13*38500039
    Li = [1]
    Lk = [-1, 0]
    for _ in range(2, exp_div+1):
        mini = log(L[len(Li)])
        i_min = len(Li)
        for k in Lk:
            p = log(L[k])*2**Li[k]
            if p < mini:
                i_min = k
        if i_min == len(Li):
            Li.append(1)
            if Lk[1] == -1:
                Lk[1] = len(Li)-1
        else:
            Li[i_min] += 1
            if i_min == len(Li)-1:
                Lk[Li[i_min]-1] = -1
            elif Li[i_min+1] == Li[i_min]-1:
                Lk[Li[i_min]-1] = i_min + 1
            else:
                Lk[Li[i_min] - 1] = -1

            if i_min == 0:
                Lk.append(0)
            elif Li[i_min-1] == Li[i_min]:
                pass
            else:
                Lk[Li[i_min]] = i_min
        # if _ == 4:
        #     print(Li, Lk)

    prod = 1
    for i in range(len(Li)):
        prod *= quick_expo(L[i], 2**Li[i]-1, modulo)
        prod %= modulo
    print(prod)
