# %% Problem 622


def f(n):
    n //= 2
    ll = list(range(2*n))
    nb = 0
    while True:
        nb += 1
        ok = True
        for i in range(2*n):
            a = ll[i]
            if a < n:
                ll[i] *= 2
            else:
                ll[i] = (a-n)*2+1
            if ll[i] != i:
                ok = False
        if ok:
            break
    return nb


def f2(n):
    n //= 2
    ll = list(range(2*n))
    nb = 0
    while True:
        nb += 1
        for i in range(2*n):
            a = ll[i]
            if a < n:
                ll[i] *= 2
            else:
                ll[i] = (a-n)*2+1
        if ll[1] == 1:
            return nb


def f3(n):
    n //= 2
    nb = 0
    a = 1
    while True:
        nb += 1
        if a < n:
            a *= 2
        else:
            a = (a-n)*2+1
        if a == 1:
            break
    return nb
