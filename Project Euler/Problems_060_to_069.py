from os import chdir
from Tools import timing, gcd, is_square, is_prime

chdir('/Users/maximin/Desktop/Euler/linked_files')


# %% Problem 60

# Todo : really not optimized ....

def problem_60():
    from Tools import numpy_sieve
    l_7 = numpy_sieve(10 ** 7)
    l_7_2 = set(l_7)

    def ok(a, p):
        if a % 3 != p % 3:
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

    l_5 = numpy_sieve(10 ** 5)
    l_5.remove(2)
    l_5.remove(5)

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

    def aux(l, f):
        ll = []
        for el in l:
            k_ = 1
            while f(k_) < 10 ** 4:
                if f(k_) // 100 == el:
                    r = f(k_) % 100
                    if r not in ll and r > 10:
                        ll.append(r)
                k_ += 1
        ll.sort()
        return ll

    ii = 2
    n = t(ii)
    while n < 10000:
        m = n % 100
        l_f = [s, p, h, hh, o]
        for i in l_f:
            l = [m]
            ll = aux(l, i)
            for j in l_f:
                if j == i:
                    continue
                lll = aux(ll, j)
                for k in l_f:
                    if j == k or k == i:
                        continue
                    llll = aux(lll, k)

                    for kk in l_f:
                        if kk == i or kk == j or kk == k:
                            continue
                        lllll = aux(llll, kk)
                        for kkk in l_f:
                            if kkk == i or kkk == j or kkk == k or kkk == kk:
                                continue
                            llllll = aux(lllll, kkk)

                            if n // 100 in llllll:
                                print(n, i, j, k, kk, kkk)
        ii += 1
        n = t(ii)

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

def problem_63():
    n = 1
    nb = 0
    while n < 22:
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


def max_path(trig):
    paths = [trig[0][0]]
    for l in trig[1:]:
        paths2 = [l[0] + paths[0]]
        for i in range(1, len(l) - 1):
            a = max(paths[i - 1], paths[i])
            paths2.append(a + l[i])
        paths2.append(l[-1] + paths[-1])
        paths = paths2
    print(max(paths))


def problem_67():
    triangle = []
    with open("p067_triangle.txt", "r") as f:
        for row in f:
            triangle.append([int(nb) for nb in row[:-1].split(" ")])
    return max_path(triangle)  # sol = 7273


# %% Problem 68

def problem_68():
    def aux(l):
        if len(l[0]) == 10:
            return l
        ll = []
        for el in l:
            for i in range(1, 11):
                if i not in el:
                    ll += aux([el + [i]])
        return ll

    l_able = [[i] for i in range(1, 11)]
    l_able = aux(l_able)

    l_magic = []
    for el in l_able:
        m = el[8] + el[9] + el[1]
        next_ = False

        for i in range(0, 7, 2):
            if m != sum(el[i:i + 3]):
                next_ = True
                break

        if not next_:

            i = el.index(10)
            if i not in [2, 4, 6, 8, 1]:
                l_magic.append(el)

    maxi = 0
    l = []
    for el in l_magic:
        m = min(el[0], *el[3::2])
        if m == maxi:
            l.append(el)
        elif m > maxi:
            l = [el]
            maxi = m

    print(l)

    l_str = []
    for el in l:
        a, b, c, d, e, f, g, h, i, j = el
        ii = []
        for el_ in [a, b, c, d, c, e, f, e, g, h, g, i, j, i, b]:
            if el_ == 10:
                ii += [1, 0]
            else:
                ii += [el_]
        l_str.append(ii)

    l_str_to_sort = []
    for el in l_str:
        i = el.index(maxi)
        el += el[:i]
        el = el[i:]
        l_str_to_sort.append(el)
    print(l_str_to_sort)

    l_str_to_sort.sort()
    print(l_str_to_sort[-1])

    s = 0
    for i in l_str_to_sort[-1]:
        s *= 10
        s += i
    print(s)  # sol = 6531031914842725


# %% Problem 69


def problem_69():
    # n/phi(n) is `maximal` then n = p1*p2*... where p1, p2 etc are primes
    # and it's easy to prove that
    # answer = 510510   (2*3*5*7*11*13*17 !!!!)
    print(2 * 3 * 5 * 7 * 11 * 13 * 17)


if __name__ == "__main__":
    @timing
    def problem_60_to_69():
        for i in range(60, 70):
            print("p" + str(i) + ": ", end="")
            eval("problem_" + str(i) + "()")


    problem_60_to_69()  # Execution of  problem_60_to_69  in ?
