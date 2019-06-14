# %% Problem 586

from Tools import is_square


def c_b(k, b0=0):
    b = b0+1
    while not is_square(4*k+5*b**2):
        b += 1
        if b >= (k/5)**0.5:
            return None
    return b, int((4*k+5*b**2)**0.5)


def g(k, r):
    cb = c_b(k)
    if cb is None:
        return False
    b1, c1 = cb
    cb = c_b(k, b1)
    if cb is None:
        return False
    b2, c2 = cb

    def f(a):
        return 5*a/(4*k+5*a**2)**0.5

    nb = 2
    m = f(b2)
    b3 = int(((m**2*b1**2+c1**2-2*m*b1*c1)/(m**2-5))/b1)
    while (k/5)**0.5 > b3 > 0:
        nb += 1
        if nb > r:
            return False
        b1, b2 = b2, b3
        m = f(b2)
        b3 = int(((m**2*b1**2+c1**2-2*m*b1*c1)/(m**2-5))/b1)
    return nb == r


def gg(k, r):
    b = c_b(k)
    nb = 0
    while b is not None:
        nb += 1
        b = c_b(k, b[0])
        if nb > r:
            return False
    return nb == r


def nb(k):
    pass