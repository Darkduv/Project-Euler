from os import chdir
from Tools import timing, gcd, is_square, is_prime

chdir('/Users/maximin/Desktop/Euler/linked_files')


# %% Problem 60

# Todo : really not optimized ....
from Tools import numpy_sieve

def problem_60():

    l_7 = numpy_sieve(10 ** 7)
    l_7_2 = set(l_7)

    def ok(a, p):
        """

        Args: two (alleged) primes
        Returns: whether the numbers (a)(p) (p)(a) (by concatenating a and p)
        are both primes or not
        """
        if a % 3 != p % 3:  # (a)(p) and (p)(a) mod 3 == (a) + (p)
            # as a and p primes, a and p !== 0 [3], and we do not want
            # the sum to be a multiple of 3.
            # problem if a or p == 3 ?!
            return False
        b = a * 10 ** len(str(p)) + p
        c = p * 10 ** len(str(a)) + a

        if b > 10 ** 7 and is_prime(b, l_7) or (b < 10 ** 7 and b in l_7_2):
            return c > 10 ** 7 and is_prime(c, l_7) or (c < 10 ** 7 and c in l_7_2)
        else:
            return False

    def commute(l, p):
        for a in l:
            if a == p:
                continue
            if a in dd and p in dd[a]:
                if not dd[a][p]:
                    return False
            else:
                bool_ok = ok(a, p)
                if a not in dd:
                    dd[a] = dict()
                dd[a][p] = bool_ok
                if not bool_ok:
                    return False
        return True

    l_5_init = numpy_sieve(10 ** 5)
    l_5 = [a for a in l_5_init if a not in [2,5]]


    dd = dict()

    n = len(l_5)

    for i in range(n):
        a = l_5[i]
        dd[a] = dict()
        for j in range(i + 1, n):
            p = l_5[j]
            dd[a][p] = ok(a, p)

    for i in range(n):
        a = l_5[i]
        r = a % 3
        for j in range(i + 1, n):
            b = l_5[j]
            if (r != 0 and b % 3 != r) or not dd[a][b]:
                continue
            if r == 0:
                r = b % 3
            for k in range(j + 1, n):
                c = l_5[k]
                if c % 3 != r or not commute([a, b], c):
                    continue
                for l in range(k + 1, n):
                    d = l_5[l]
                    if d % 3 != r or not commute([a, b, c], d):
                        continue
                    for m in range(l + 1, n):
                        e = l_5[m]
                        if not e % 3 != r and commute([a, b, c, d], e):
                            print([a, b, c, d, e], a + b + c + d + e)


# %% Problem 61
from itertools import permutations
def problem_61():
    def t(n):
        n *= n + 1
        return n // 2

    def p(n):
        n *= 3 * n - 1
        return n // 2

    def h(n):
        n *= 2 * n - 1
        return n

    def hh(n):
        n *= 5 * n - 3
        return n // 2

    def o(n):
        n *= 3 * n - 2
        return n

    def s(n):
        return n * n

    def aux2(f):
        ll = {}
        k_ = 1
        while f(k_) < 10 ** 4:
            r = f(k_) % 100
            q = f(k_) // 100
            if r > 10 and q > 10:
                if r not in ll:
                    ll[r] = []
                ll[r].append(q)
            k_ += 1
        return ll

    list_f = [p, s, t, h, hh, o]
    l_d_f = [aux2(f) for f in list_f]

    def aux(l, d_f):
        ll = []
        for el in l:
            if el[-1] in d_f:
                for el2 in d_f[el[-1]]:
                    ll.append(el+[el2])
        return ll

    def aux3(l, l_i_f):
        if not l_i_f:
            return l
        i = l_i_f[-1]
        ll = aux(l, l_d_f[i])
        return aux3(ll, l_i_f[:-1])

    l0 = [[a] for a in l_d_f[5]]

    for lf in permutations(range(5)):
        li_f = list(lf)
        l1 = aux3(l0, li_f+[5])
        for eel in l1:
            if eel[0]==eel[-1]:
                print(eel[:-1])
                return sum(eel[:-1])*101
    # 8256+5625+2512+1281+8128+2882


# %% Problem 62

def problem_62():
    def aux(n):
        L = []
        q = n
        while q != 0:
            q, r = divmod(q, 10)
            L.append(r)
        return L[::-1]

    def is_a_permutation(a, n):
        l_n = aux(n)
        for i in aux(a):
            try:
                l_n.remove(i)
            except ValueError:
                return False
        if l_n != []:
            return False
        return True

    ok = False
    counter = 99
    L_cub = []
    while not ok:
        counter += 1
        n = counter ** 3
        L_cub = []
        L_n = aux(n)
        len_a = (len(L_n) + 1) // 3
        for a in range(10 ** (len_a - 1), 10 ** len_a):
            a_cub = a ** 3
            if is_a_permutation(a_cub, n) and a_cub >= n:
                if a_cub not in L_cub:
                    L_cub.append(a_cub)
            if len(L_cub) > 5:
                break
        if len(L_cub) == 5:
            print(L_cub)
            break

        if counter > 100000:
            print("defeat :-(")
            break


# %% Problem 63
# -- optimised --
def problem_63():
    """
    Looking for a, n \in N^2 such as :
    10^n > a^n >= 10^(n-1)  .... (this means that a^n is a n-digit)
    <=> 10 > a >= 10^(1-1/n)

    therefore, as a \in N, a <= 9. So 10^(1-1/n) <= 9
    =>  1-1/n <= log_10(9)
    => 1/(1-log_10(9)) >= n
    => 21.85.. >= n
    => n < 22
    """
    n = 1
    nb = 0
    while n < 22:  # if n
        for a in range(1, 10):
            if 10 ** n > a ** n >= 10 ** (n - 1):
                nb += 1
        n += 1
    print(nb)


# %% Problem 64


def problem_64():
    def period(D):
        h1, k1 = 1, 0
        a_i = int(D ** 0.5)
        r = 1, 1, -a_i, 1
        h2, k2 = a_i, 1
        L = []
        while r not in L:
            L.append(r)
            a, b, c, d = r
            a2, b2 = a * b * d ** 2, a ** 2 * d ** 2 * D - c ** 2 * b ** 2
            c2, d2 = -c * b ** 2 * d, a ** 2 * d ** 2 * D - c ** 2 * b ** 2
            a, b, c, d = a2, b2, c2, d2
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

    c = 0
    for N in range(2, 10001):
        if not is_square(N) and period(N) % 2 == 1:
            c += 1
    print(c)


# %% Problem 65

def problem_65():
    a, b = 1, 1
    for j in range(98, 0, -1):
        a, b = b, a
        c = ((j+1)//3)*2 if j % 3 == 2 else 1
        a += c*b
    a, b = b, a
    c = 2
    a += c*b
    nb = 0
    while a > 0:
        nb += a % 10
        a //= 10
    print(nb)  # sol = 272


# %% Problem 66


def problem_66():
    def a_b(D):
        h1, k1 = 1, 0
        a_i = int(D ** 0.5)
        r = 1, 1, -a_i, 1
        h2, k2 = a_i, 1
        while h2 ** 2 - D * k2 ** 2 != 1:
            a, b, c, d = r
            a2, b2 = a * b * d ** 2, a ** 2 * d ** 2 * D - c ** 2 * b ** 2
            c2, d2 = -c * b ** 2 * d, a ** 2 * d ** 2 * D - c ** 2 * b ** 2
            a, b, c, d = a2, b2, c2, d2
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

    x_max = 9
    D_max = 5
    for D in range(10, 1001):
        if not is_square(D):
            x = a_b(D)[0]
            if x > x_max:
                D_max = D
                x_max = x
    print(D_max)


# %% Problem_67

# -- could max_path be optimised with numpy ? --
from Tools import max_path

def problem_67():
    triangle = []
    with open("p067_triangle.txt", "r") as f:
        for row in f:
            triangle.append([int(nb) for nb in row[:-1].split(" ")])
    return max_path(triangle)  # sol = 7273


# %% Problem 68

def problem_68():
    """
    for the concatenated string to be maximal,
    necessarily the lowest numbers are in the center.
    Therefore if we sum all "rays", we have sum(1+...+10) + sum(1+..+5),
    as the numbers in the center are counted two times.
    So the sum is 70. the rays have same sum. so the sum over one ray is 14

    14 = 10 + (4 ?)  -> 10+1+3 (can't be 10+2+2)
    14 = 6 + (8 ?)  ->  6 + 5 + 3
    14 = 9 + (5) -> 9 + 1 + 4 or +2+3 but '3' is already used 2 times.
    so 9+1+4.
    14 = 8 + (6) -> 1, 5 or 2,4 . 1 already used. so (8,2,4) it is.
    14 = 7 + (7) -> we have at this moment only 7,5,2 available.

    There, we know that the string will begin with 6,5,3 to be the greatest.
    and 3 is also used by 10 :
    s = 6,5,3,10,3,1 ...
    1 is also used by 9:
    s=6,5,3,10,3,1,9,1,4 ... and so on
    """
    s = 6531031914842725
    return s  # sol = 6531031914842725


# %% Problem 69


def problem_69():
    # n/phi(n) is `maximal` when phi/n minimal.
    # and phi/n == prod(1-p_i), for p_i prime divisor of n)

    # so, the minimal phi/n for n <= N is the n <= N such as n as the
    # greatest number of prime divisor and the smallest prime divisors :

    # n = p1*p2*... where p1, p2 etc are primes, the smallest one
    # and it's easy to prove that ;p

    # answer = 510510   (2*3*5*7*11*13*17 !!!!)
    print(2 * 3 * 5 * 7 * 11 * 13 * 17)


if __name__ == "__main__":
    @timing
    def problem_60_to_69():
        for i in range(60, 70):
            print("p" + str(i) + ": ", end="")
            eval("problem_" + str(i) + "()")


    problem_60_to_69()  # Execution of  problem_60_to_69  in ?
