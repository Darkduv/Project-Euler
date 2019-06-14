# %% Problem 435

# F_n(x) = (x-f(n+1)*x^(n+1) - x^(n+2)*f_n)/(1-x-x^2)


def fibonacci(n, bb, d):
    if n in d:
        return d[n]
    k, r = n//2, n % 2
    if r == 0:
        a = fibonacci(k+1, bb, d)**2-fibonacci(k-1, bb, d)**2
    else:
        a = fibonacci(k+1, bb, d)**2+fibonacci(k, bb, d)**2
    a %= bb
    d[n] = a
    return a


def f_n_x(n, x, mod):
    d = {0: 0, 1: 1, 2: 1}
    bb = -x - x ** 2 + 1
    f2 = fibonacci(n, mod * bb, d)
    f1 = fibonacci(n + 1, mod * bb, d)
    return ((x - f1 * pow(x, n + 1, mod * bb) - f2 * pow(x, n + 2, mod * bb)) % (mod * bb)) // bb

m = 1307674368000
print(sum(f_n_x(10**15, x, m) for x in range(101)) % m)
