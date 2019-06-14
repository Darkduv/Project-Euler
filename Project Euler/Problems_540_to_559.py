# %% Problem 549


from Tools import decompose_tout, numpy_sieve

l = numpy_sieve(10**8)
l_set = set(l)


def s(n):
    if n in l_set:
        return n
    d = dict(decompose_tout(n, l))
    nb_tot = sum(d.values())
    m = 1
    nb = 0
    while nb < nb_tot:
        m += 1
        for p in d:
            mm = m
            while mm % p == 0 and d[p] > 0:
                mm //= p
                nb += 1
                d[p] -= 1
    return m


def sum_s(n):
    acc = 0
    for i in range(2, n+1):
        acc += s(i)
    return acc

print(sum_s(10**8))


# %% Problem 559


def ascent(tab, j):
    for i in range(len(tab)):
        if tab[i][j] > tab[i][j+1]:
            return False
    return True


def p(k, n):
    pass
