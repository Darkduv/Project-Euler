# %% Problem 128

# It can be shown that a such candidate is of the form 3*k*(k-1)+1 or +2

from Tools import is_prime


test = is_prime


def next_pd3(k):
    if k == 1:
        return [1, 2], 2
    while True:
        a, b, c, d, e = 6*k-1,  12*k+5, 6*k+1, 6*k+5, 12*k-7
        if not test(a):
            k += 1
        else:
            tbc, tde = test(b) and test(c), test(d) and test(e)
            if not tbc and not tde:
                k += 1
            else:
                p = 3*k*(k-1)+2
                if tbc and tde:
                    return [p, p+6*k-1], k+1
                elif tbc:
                    return [p], k+1
                else:
                    return [p+6*k-1], k+1


lim = 2000
N = 0
kk = 1
latest = []
while N < lim:
    latest, kk = next_pd3(kk)
    N += len(latest)

print(latest[-1 - (N-lim)])

# sol = 14516824220
