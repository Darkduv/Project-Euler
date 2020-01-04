# %% 500

from math import log
from Tools import numpy_sieve, quick_expo


def problem_500(exp_div=500500):
    l7 = numpy_sieve(10 ** 7)
    modulo = 500500507  # n_max = 13*38500039
    li = [1]
    lk = [-1, 0]
    for _ in range(2, exp_div + 1):
        mini = log(l7[len(li)])
        i_min = len(li)
        for k in lk:
            p = log(l7[k]) * 2 ** li[k]
            if p < mini:
                i_min = k
        if i_min == len(li):
            li.append(1)
            if lk[1] == -1:
                lk[1] = len(li) - 1
        else:
            li[i_min] += 1
            if i_min == len(li) - 1:
                lk[li[i_min] - 1] = -1
            elif li[i_min + 1] == li[i_min] - 1:
                lk[li[i_min] - 1] = i_min + 1
            else:
                lk[li[i_min] - 1] = -1

            if i_min == 0:
                lk.append(0)
            elif li[i_min - 1] == li[i_min]:
                pass
            else:
                lk[li[i_min]] = i_min
        # if _ == 4:
        #     print(Li, Lk)

    prod = 1
    for i in range(len(li)):
        prod *= quick_expo(l7[i], 2 ** li[i] - 1, modulo)
        prod %= modulo
    print(prod)

# sol = 35407281
