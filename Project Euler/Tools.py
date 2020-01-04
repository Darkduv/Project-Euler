import numpy as np
from time import time
from random import randrange


def timing(f):
    def ff(*args, **kwargs):
        timer = time()
        result = f(*args, **kwargs)
        print("Execution of ", f.__name__, " in", time() - timer, "sec.")
        return result

    return ff


def decompose(n, l_primes=None):
    ll = []
    if l_primes is None:
        if n % 2 == 0:
            ll.append(2)
            while n % 2 == 0:
                n //= 2

        a = 3
        while n != 1 and a ** 2 <= n:
            if n % a == 0:
                ll.append(a)
                while n % a == 0:
                    n //= a
            a += 2
        if n != 1:
            ll.append(n)
        return ll
    else:
        for i in l_primes:
            if n % i == 0:
                while n % i == 0:
                    n //= i
                ll.append(i)
            if i ** 2 > n:
                if n > 1:
                    ll.append(n)
                break
        return ll


def decompose_danger(n, l_primes):
    ll = []
    for i in l_primes:
        if n % i == 0:
            while n % i == 0:
                n //= i
            ll.append(i)
        if i ** 2 > n:
            ll.append(n)
            return ll
    p = l_primes[-1] + 2
    while n != 1 and p ** 2 <= n:
        if n % p == 0:
            ll.append(p)
            while n % p == 0:
                n //= p
        p += 2
    if n != 1:
        ll.append(n)
    return ll


def decompose_tout(n, l_primes=None):
    if l_primes is None:
        ll = []
        if n % 2 == 0:
            acc = 0
            while n % 2 == 0:
                n //= 2
                acc += 1
            ll.append([2, acc])

        a = 3
        while n != 1 and a ** 2 <= n:
            if n % a == 0:
                acc = 0
                while n % a == 0:
                    n //= a
                    acc += 1
                ll.append([a, acc])
            a += 2
        if n != 1:
            ll.append([n, 1])
        return ll
    else:
        ll = []
        for i in l_primes:
            if n % i == 0:
                nb = 0
                while n % i == 0:
                    n //= i
                    nb += 1
                ll.append([i, nb])
            if n == 1:
                break
            if i ** 2 > n:
                ll.append([n, 1])
                break
        return ll


def phi(n, lp=None):
    ll = decompose(n, lp)
    prod1 = 1
    prod2 = 1
    for p in ll:
        prod1 *= p
        prod2 *= p - 1
    prod2 *= n
    return prod2 // prod1


def is_prime(p, lp=None):
    if lp is None:
        if p % 2 == 0:
            return False or p == 2
        a = 3
        while a <= int(p ** 0.5):
            if p % a == 0:
                return False
            a += 2
        return True and p != 1
    else:
        if p < lp[-1]:
            if p % 2 == 0:
                return p == 2
            return binary_search(lp, p)[0]
        for pp in lp:
            if pp ** 2 > p:
                return True
            if p % pp == 0:
                return False
        a = lp[-1] + 2
        while a <= int(p ** 0.5):
            if p % a == 0:
                return False
            a += 2
        return True and p != 1


def is_square(n):
    a = n ** 0.5
    return int(a) ** 2 == n or int(a + 1) ** 2 == n


def is_palindromic(n, base=10):
    reverse = 0
    k = n
    while k > 0:
        reverse = base * reverse + k % base
        k //= base
    return n == reverse


def make_palindrome(n, base, odd_length):
    res = n
    if odd_length:
        n //= base
    while n > 0:
        res = base * res + n % base
        n //= base
    return res


def anagram(a, b):
    a, b = str(a), str(b)
    a, b = list(a), list(b)
    a.sort()
    b.sort()
    return a == b


def gcd(a, b):
    a, b = abs(a), abs(b)
    if a < b:
        r = b % a
        return gcd(a, r)
    elif b == a:
        return b
    elif b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


def next_permutation(l, end=False):
    i = 0
    n = len(l)
    ok = False
    while i + 1 < n:
        if l[i] > l[i + 1]:
            ok = True
            break
        i += 1
    if ok:
        a = l[i + 1]
        m = min([el for el in l[:i + 1] if el > a])
        j = l.index(m)
        l[j] = a
        if end:
            return l[i::-1] + [m] + l[i + 2::], False
        else:
            return l[i::-1] + [m] + l[i + 2::]
    else:
        if end:
            return l, True
        else:
            return l


def partition(n, d):  # cf Problem 78 # cf wikipedia or something like that
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    k_inf = int((1 - (1 + 24 * n) ** 0.5) / 6)
    k_sup = int((1 + (1 + 24 * n) ** 0.5) / 6)
    s = 0
    for k in range(k_inf, k_sup + 1):

        if k != 0:
            if n - k * (3 * k - 1) // 2 in d:
                s += int((-1) ** (k - 1)) * d[n - k * (3 * k - 1) // 2]
            else:
                pp = partition(n - k * (3 * k - 1) // 2, d)
                d[n - k * (3 * k - 1) // 2] = pp
                s += int((-1) ** (k - 1)) * pp
            s %= 1000000
    return s


def period(D):  # period of the development in continued Fraction of sqrt(D)
    h1, k1 = 1, 0
    a_i = int(D ** 0.5)
    r = 1, 1, -a_i, 1
    h2, k2 = a_i, 1
    L = []
    while r not in L:
        L.append(r)
        a, b, c, d = r
        a, b, c, d = (a * b * d ** 2, a ** 2 * d ** 2 * D - c ** 2 * b ** 2, -c * b ** 2 * d,
                      a ** 2 * d ** 2 * D - c ** 2 * b ** 2)
        d1 = gcd(abs(a), abs(b))
        a //= d1
        b //= d1
        a_i = int(a * (D ** 0.5) / b + c / d)
        c -= a_i * d
        d2 = gcd(abs(c), abs(d))
        c //= d2
        d //= d2
        r = a, b, c, d
        h1, h2 = h2, a_i * h2 + h1
        k1, k2 = k2, a_i * k2 + k1
    return len(L) - L.index(r)


def a_b(D):  # x0, y0 minimals positive integers such that x^2 - D*y^2 = 1
    h1, k1 = 1, 0
    a_i = int(D ** 0.5)
    r = 1, 1, -a_i, 1
    h2, k2 = a_i, 1
    while h2 ** 2 - D * k2 ** 2 != 1:
        a, b, c, d = r
        a, b, c, d = (a * b * d ** 2, a ** 2 * d ** 2 * D - c ** 2 * b ** 2, -c * b ** 2 * d,
                      a ** 2 * d ** 2 * D - c ** 2 * b ** 2)
        d1 = gcd(abs(a), abs(b))
        a //= d1
        b //= d1
        a_i = int(a * (D ** 0.5) / b + c / d)
        c -= a_i * d
        d2 = gcd(abs(c), abs(d))
        c //= d2
        d //= d2
        r = a, b, c, d
        h1, h2 = h2, a_i * h2 + h1
        k1, k2 = k2, a_i * k2 + k1

    return h2, k2


def sum_divisor(n):
    ll = decompose_tout(n)
    s = 1
    for p, k in ll:
        s *= p ** (k + 1) - 1
        s //= (p - 1)
    return s


def bezout(u, n):  # return y, x where u*x + n*y = 1
    try:
        q, r = divmod(n, u)
        if r == 1:
            return 1, -q
        v, k = bezout(r, u)
        return k, v - k * q
    except ZeroDivisionError:
        print(u, n)
        raise Exception


def numpy_sieve(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    a, = np.nonzero(sieve)
    return np.r_[2, 3, ((3 * a + 1) | 1)]


def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def binary_search(l, n):
    a, b = 0, len(l) - 1
    if l[a] == n:
        return True, 0
    elif l[b] == n:
        return True, b
    elif l[b] < n:
        return False, b
    while b - a > 1:
        m = (a + b) // 2
        c = l[m]
        if c == n:
            return True, m
        elif c > n:
            b = m
        else:
            a = m
    return False, a


def binary_search_inf(l, n):
    ok, i = binary_search(l, n)
    return i


def sum_digit(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s


def nb_to_digits(n, b=10):
    ll = []
    while n > 0:
        ll.append(n % b)
        n //= b
    return ll[::-1]


def digits_to_nb(l, b=10):
    n = 0
    for i in l:
        n *= b
        n += i
    return n


def quick_expo(x, n, mod=None):
    z = 1
    y = x
    if mod:
        while n != 0:
            if n % 2 == 1:
                z *= y
                z %= mod
            n //= 2
            y *= y
            y %= mod
        return z % mod
    else:
        while n != 0:
            if n % 2 == 1:
                z *= y
            n //= 2
            y *= y
        return z


def dichotomy(g, a: float, b: float, eps):
    assert g(a) * g(b) <= 0
    while b - a > eps:
        m = (b + a) / 2
        if g(a) * g(m) >= 0:
            a = m
        else:
            b = m
    return (a + b) / 2


def quick_fibonacci(n):
    if n < 0:
        raise ValueError("n<0")

    def _fib(nn):
        if nn == 0:
            return 0, 1
        else:
            a, b = _fib(nn // 2)
            c = a * (2 * b - a)
            d = b * b + a * a
            if nn % 2 == 0:
                return c, d
            else:
                return d, c + d

    return _fib(n)[0]


def v_p(n, p):
    """p_valuation of n! """
    n_tot = 0
    q = p
    while q <= n:
        n_tot += n//q
        q *= p
    return n_tot


# --- Miller-Rabin primality test.py----------------------------------------------------------------
def miller_rabin(n, n_repeat=20):
    """
    Check n for primality:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:
    http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)
    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(n_repeat):
        a = 0
        while a == 0:
            a = randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s - 1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1
