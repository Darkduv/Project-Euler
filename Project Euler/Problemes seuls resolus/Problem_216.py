from random import randint


def exp_mod(x, n, p):
    y = x % p
    m = n
    z = 1
    while m > 0:
        if m % 2 == 1:
            z *= y
            z %= p
        y *= y
        y %= p
        m //= 2
    return z


def is_fermat(N, a):
    return exp_mod(a, N - 1, N) == 1


def is_prime_pgp(N):
    for i in [2, 3, 5, 7]:
        if not is_fermat(N, i):
            return False
    return True


def aux_test(N, a, m, s):
    for d in range(0, s):
        if exp_mod(a, 2 ** d * m, N) == N - 1:
            return False
    if exp_mod(a, m, N) == 1:
        return False
    return True


def test_miller(N):
    M = N-1
    s = 0
    while M % 2 == 0:
        s += 1
        M //= 2

    for i in range(30):
        if aux_test(N, randint(1, N - 1), M, s):
            return False
    return True


L = []
for nn in range(2, 50*10**6+1):
    pn = 2*nn**2-1
    if is_prime_pgp(pn):
        L.append(pn)


from Tools import miller_rabin

L = []
for nn in range(2, 50*10**6+1):
    if nn % 7 not in [2, 5]:
        pn = 2 * nn ** 2 - 1
        L.append(pn)

L2 = []
for pn in L:
    if miller_rabin(pn, n_repeat=1):
        L2.append(pn)

L3 = []
for pn in L2:
    if miller_rabin(pn, n_repeat=5):
        L3.append(pn)

# sol = 5437849
