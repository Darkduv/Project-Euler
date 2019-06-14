# %% Problem 293


from Tools import numpy_sieve

l_8 = numpy_sieve(10**8)

pseudo_fortunate = []


def pseudo(n):
    m = 2
    nb = 0
    while True:
        broken = False
        for a in l_8:
            if (n+m) % a == 0 and n+m != a:
                broken = True
                break
            if a**2 >= n+m:
                return m
        if not broken:
            p = l_8[-1]
            while p**2 < n+m:
                p += 2
                if (n+m) % p == 0 and n+m == p:
                    return m
                if (n+m) % p == 0:
                    break
        m += 1
        nb += 1
        if nb > 10**9 + 8:
            raise ValueError("we have gone too much further !!!!")


def sum_pseudo(i, n, lim):
    while n*l_8[i] <= lim:
        n *= l_8[i]
        p = pseudo(n)
        if p not in pseudo_fortunate:
            pseudo_fortunate.append(p)
        sum_pseudo(i+1, n, lim)


def f_problem_293(n):
    global pseudo_fortunate
    pseudo_fortunate = []
    sum_pseudo(0, 1, n)
    print(sum(pseudo_fortunate))


print(f_problem_293(10**9))  # sol = 2209
