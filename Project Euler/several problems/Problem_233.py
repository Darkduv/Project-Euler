# %% Problem 233

from Tools import is_square


def next_x(n, x=0):
    x += 1
    while not is_square(2*n**2-(2*x-n)**2) and x <= n:
        x += 1
    return x if x <= n else 0


def ok_too_much_brute(n):
    x = next_x(n)
    nb = 0
    while x != 0:
        nb += 1
        x = next_x(n, x)
        if nb > 105:
            return False
    return nb == 105


def ok(n):
    def f(x, y):
        return -(n-2*x)/(n-2*y)
    # x1, y1 = 0, 0
    x2 = next_x(n)
    if x2 == 0:
        return False
    y2 = int((-(2*n**2-(2*x2-n)**2)**0.5 + n)/2-10**-4)
    x1, y1 = x2, y2
    x2 = next_x(n, x1)
    if x2 == 0:
        return False
    y2 = int((-(2 * n ** 2 - (2 * x2 - n) ** 2) ** 0.5 + n) / 2 - 10 ** -4)
    m = f(x2, y2)
    nb = 2
    while x2 < n:
        nb += 1
        if nb > 105:
            return False
        a, b = x1, y1
        c = (4*m**2*a**2-4*(2*b-n)*m*a+4*b**2-4*b*n)/(4*m**2+4)  # x1*x3 = c
        x1, y1, x2 = x2, y2, int(c/a+10**-4)
        y2 = int(m*(x2-a)+b-10**-4)
        m = f(x2, y2)
    return nb == 105

s = 0
for n in range(105, 10**11+1):
    if ok(n):
        s += n
