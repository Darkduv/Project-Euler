# %% Problem 146

from random import randrange


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n, REPEAT=2):  # see 'to_be_studied'
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(REPEAT):
        a = 0
        while a == 0:
            a = randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def problem_146():
    ll = []
    for k in range(1, 15 * 10 ** 6 + 1):
        if k % 3 == 0 or (10 * k) % 7 in [0, 1, 2, 5, 6] or k % 13 == 0:
            continue
        n = 10 * k
        if miller_rabin(n ** 2 + 1) and miller_rabin(n ** 2 + 3) \
                and miller_rabin(n ** 2 + 7) and miller_rabin(n ** 2 + 9):
            ll.append(n)
    l_bis = []
    for n in ll:
        if miller_rabin(n ** 2 + 13) and miller_rabin(n ** 2 + 27):
            l_bis.append(n)

    l_ter = []
    for n in l_bis:
        ok = True
        for a in range(1, 28, 2):
            test = miller_rabin(n ** 2 + a, REPEAT=10)
            if a in [1, 3, 7, 9, 13, 27]:
                if not test:
                    ok = False
                    break
            else:
                if test:
                    ok = False
                    break
        if ok:
            l_ter.append(n)

    return sum(l_ter)

#  sol = 676333270
