from os import chdir
from itertools import permutations
from Tools import timing, gcd, numpy_sieve, nb_to_digits, digits_to_nb, binary_search_inf, is_palindromic
from Tools import is_square, binary_search

chdir('/Users/maximin/Desktop/Euler/linked_files')


# %% Problem 30

def problem_30():

    d2 = {i ** 5 - i: i for i in range(10)}
    d = {i: i ** 5 - i for i in range(10)}

    def aux(n):
        s = 0
        while n != 0:
            s += (n % 10) ** 5
            n //= 10
        return s

    def ok(n, s):
        a = (-s) % 10
        bbb = 100 * n - s + 9 * a - d[a]
        if bbb == 0:
            return True, [(a, 1), (a, 0)]
        if bbb in d2:
            return True, [(a, d2[bbb])]
        return False, []

    tot = 0
    for j in range(1, 10 ** 4):
        boo, l_ab = ok(j, aux(j))
        if boo:
            for a1, a2 in l_ab:
                tot += j*100+10*a1+a2
    print(tot)  # sol = 443839


# %% Problem 31

def problem_31():
    total = 200

    # At the start of each loop iteration, ways[i] is the number of ways to use {any copies
    # of the all the coin values seen before this iteration} to form an unordered sum of i
    ways = [1] + [0] * total
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    print(str(ways[-1]))  # sol = 73682


# %% Problem 32

def problem_32():
    s = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            for k in range(1, 10):
                if i == k or j == k:
                    continue
                for ll in range(1, 10):
                    if ll == k or ll == i or ll == j:
                        continue
                    n = int(str(i) + str(j) + str(k) + str(ll))
                    d = 1
                    while d ** 2 < n:
                        if n % d == 0:
                            ss = str(n) + str(d) + str(n // d)
                            ss = list(ss)
                            ss.sort()
                            if ss == list("123456789"):
                                s += n
                                break
                        d += 1
    print(s)  # sol = 45228


# %% Problem 33

# One can prove that the only possibilities are (ab/ca = b/c) or (ba/ac = b/c)
# for the first one we got 0 < a < b < c <= 9 and for the second one, 0 < b < c < a <= 9

def problem_33():
    L = []
    for b in range(1, 9):
        for c in range(b+1, 10):
            q, r = divmod(9*b*c, 10*b-c)  # second case
            if r == 0 and c < q < 10:
                L.append((b, c))
            q, r = divmod(9*b*c, 10*c-b)  # first one
            if r == 0 and 0 < q < b:
                L.append((b, c))
    num = 1
    denominator = 1
    for n, d in L:
        num *= n
        denominator *= d
    delta = gcd(num, denominator)
    print(denominator//delta)  # sol = 100


# %% Problem 34

def problem_34():

    l_fact = [1]
    for i in range(1, 10):
        l_fact.append(l_fact[-1] * i)

    s_tot = 0
    for i in range(10):
        for j in range(i, 10):
            for k in range(j, 10):
                for l in range(k, 10):
                    for m in range(l, 10):
                        for n in range(m, 10):
                            ll = [i, j, k, l, m, n]

                            s = sum(l_fact[e] for e in ll if e != 0)
                            for nb0 in range(0, ll.count(0)+1):
                                s += nb0
                                s1 = list(str(s))
                                s1.sort()
                                s2 = [str(e) for e in ll if e != 0]+["0"]*nb0
                                s2.sort()
                                if s1 == s2:
                                    s_tot += s

    print(s_tot-3)  # 40730


# %% Problem 35

def problem_35():
    l_primes = numpy_sieve(10**6)
    l_primes2 = []
    for i in l_primes[4:]:
        a = True
        for j in nb_to_digits(i):
            if j % 2 == 0:
                a = False
                break
        if a:
            l_primes2.append(i)

    nb = 4  # 2, 3, 5, 7
    l_primes3 = []
    for i in l_primes2:
        L = nb_to_digits(i)
        if digits_to_nb(L[1:] + L[0:1]) in l_primes2:
            if len(L) == 2:
                nb += 1
            else:
                l_primes3.append(i)

    n = len(l_primes3)
    m = n - 1
    while m < n:
        l_primes4 = []
        for i in l_primes3:
            L = nb_to_digits(i)
            if digits_to_nb(L[1:] + L[0:1]) in l_primes3:
                l_primes4.append(i)
        l_primes3 = l_primes4
        n, m = m, len(l_primes3)
    print(n+nb)


# %% Problem 36

def problem_36(limit=10**6):
    def make_palindrome2(n, odd_length):
        res = n
        if odd_length:
            n >>= 1
        while n > 0:
            res = (res << 1) + (n & 1)
            n >>= 1
        return res

    s = 0
    i = 1
    p = make_palindrome2(i, True)
    while p < limit:
        if is_palindromic(p, 10):
            s += p
        i += 1
        p = make_palindrome2(i, True)
    i = 1
    p = make_palindrome2(i, False)
    while p < limit:
        if is_palindromic(p, 10):
            s += p
        i += 1
        p = make_palindrome2(i, False)
    print(s)  # sol = 872187


# %% Problem 37:

def problem_37():
    l_6 = numpy_sieve(1000000)
    l0 = [2, 3, 5, 7]
    l2 = []
    for k in range(5):
        l3 = []
        for i in [1, 3, 5, 7, 9]:
            for p in l0:
                a = p * 10 + i
                if a in l_6:
                    l3.append(a)
        l2.extend(l3[:])
        l0 = l3
    l0 = [2, 3, 5, 7]
    l4 = []
    for k in range(5):
        l3 = []
        for i in [1, 2, 3, 5, 7, 9]:
            for p in l0:
                a = p + i * 10 ** (k + 1)
                if a in l_6:
                    l3.append(a)
        l4.extend(l3[:])
        l0 = l3
    s = 0
    nb = 0
    for p in l2:
        if p in l4:
            s += p
            nb += 1
        if nb == 11:
            break

    print(s)  # sol = 748317


# %% Problem 38

def problem_38():  # function quite obscure. i don't remember the meaning of the calculations

    def f(start):
        m = ""
        k = 1
        l_ok = [False]*9
        while len(m) < 9:
            m2 = str(start*k)
            for digit in m2:
                if l_ok[int(digit)-1]:
                    return False, -1
                else:
                    l_ok[int(digit)-1] = True
            m += m2
            k += 1
        return len(m) == 9, int(m)

    maxi = 918273645
    am, bm, cm = 1, -1, -1
    for a in range(1, 9):
        if a < am:
            continue
        ok, n = f(90+a)
        if ok:
            am = a
            maxi = max(maxi, n)

        for b in range(1, 9):
            if bm > b or b == a:
                continue
            ok, n = f(900+10*a+b)
            if ok:
                maxi = max(maxi, n)
                bm = b
            for c in range(1, 9):
                if c < cm or c == b or c == a:
                    continue
                ok, n = f(9000+100*a+10*b+c)
                if ok:
                    maxi = max(maxi, n)
                    cm = c
    print(maxi)  # sol = 932718654


# %% Problem 39

def problem_39():
    max_p = 1000
    s = [set() for _ in range(max_p + 1)]
    for a in range(23):
        for b in range(a):
            p = 2 * a * (a + b)
            if p > max_p:
                break
            k = 1
            while k * p < max_p:
                L = [k * (a ** 2 - b ** 2), k * (a ** 2 + b ** 2), 2 * k * a * b]
                L.sort()
                t = tuple(L)
                # noinspection PyTypeChecker
                s[k * p].add(t)
                k += 1
    nb_m, p_m = 0, 0
    for p, set_p in enumerate(s):
        nb = len(set_p)
        if nb > nb_m:
            nb_m = nb
            p_m = p
    print(p_m)  # sol = 840


# %% Problem 40

def problem_40():
    s = "0"
    for i in range(1, 200000):
        s += str(i)
    p = 1
    for k in range(7):
        p *= int(s[10**k])
    print(p)


# %% Problem 41

def problem_41():
    l_8 = numpy_sieve(10**7)
    for p in permutations(list("7654321")):
        p = int("".join(p))
        if p in l_8:
            print(p)  # sol = 7652413
            break


# %% Problem 42

def problem_42():
    l_t = []
    for i in range(30):
        l_t.append((i * (i+1)) // 2)
    l_t = set(l_t)

    def code(word):
        n = 0
        for letter in word:
            n += (ord(letter)-64)
        return n

    with open("p042_words.txt", 'r') as f:
        words = f.readline()
        nb = 0
        for i in words.split(","):
            if code(i[1:-1]) in l_t:
                nb += 1
    print(nb)  # sol = 162


# %% Problem 43

def problem_43():
    l_p = [0, 0, 0, 0, 2, 3, 5, 7, 11, 13, 17]
    L = {length: (length-3, l_p[length]) for length in range(11)}

    def f(nb):
        if len(nb) == 10:
            yield nb
        else:
            for d in range(10):
                if str(d) in nb:
                    continue
                a = nb+str(d)
                if len(a) <= 3:
                    for b in f(a):
                        yield b
                else:
                    i0, p = L[len(a)]
                    if int(a[i0:]) % p == 0:
                        for b in f(a):
                            yield b
    s = 0
    for i in range(10):
        s += sum(int(nn) for nn in f(str(i)))

    print(s)  # sol = 16695334890


# %% Problem 44

def problem_44():
    def pent(n):
        return (n * (3*n-1)) // 2

    a = 1
    while True:
        d = pent(a)
        a += 1
        dd = 2 * d
        i = 1
        ok = False
        while i * (3 * (i + 2) - 1) <= dd:
            if dd % i == 0:
                j = dd // i
                if j % 3 != 2:
                    i += 1
                    continue
                i2 = (j + 1) // 3
                if i2 < i:
                    i += 1
                    continue
                if (i + i2) % 2 != 0:
                    i += 1
                    continue
                k = (i + i2) // 2
                s = 3 * k ** 2 - k - d
                delta = 1 + 24 * s
                if is_square(delta) and int(delta ** 0.5 + 1) % 3 == 0:
                    ok = True
                    print(d)
                    break
            i += 1
        if ok:
            break
    # sol = 5482660


# %% Problem 45
# Tn=n(n+1)/2,  Pn=n(3n−1)/2, Hn=n(2n−1)
# so if Tj = Pn = Hm we got m = (j+1)/2 so j is odd
# and n = (  1+sqrt(1+12j+12j^2)  )  / 6
# so we need k such that (6*k + 5)^2 = 1+12j+12j^2
# that is 36*k^2 + 60*k +24 = 12*j + 12*j^2  =>    3*k^2 + 5*k + 2 = j + j^2

# let's define f(k) = sqrt(3*k^2 + 5*k + 2).
# f(0) = 3, f(164=k0) = 571 = y0 # so the next k verifies the following : ( (12k0+10)/y0 *(k-0) + 3) ^2 = 12*k**2+20*k+9
# so k = ( -6* (12*k0+10)/y0  +20  ) /(   ((12*k0+10)/y0)^2 -12 )

def problem_45():
    y0 = 571
    k0 = 164
    k = 6*(12*k0+10) * y0 - 20 * y0 ** 2
    k //= - (12*k0+10) ** 2 + 12 * y0**2

    y = ((12*k0+10) * k+3*y0)//y0
    n = (y-1)//2
    print(n*(n+1)//2)  # sol = 1533776805


# %% Problem 46
# todo ?
def problem_46():
    l_10000 = numpy_sieve(10000)[1:]
    ll = set(i for i in range(7, 10 ** 4, 2))
    for n in range(70):
        for p in l_10000:
            a = p + 2 * n ** 2
            if a > 10000:
                break
            if a in ll:
                ll.remove(a)
    print(min(ll))  # sol = 5777


# %% Problem 47

def problem_47():
    ll = numpy_sieve(10**3)

    l0 = [0]*10**6
    for p in ll:
        for i in range(2*p, len(l0), p):
            l0[i] += 1
    i = 0
    while i + 3 < len(l0):
        if l0[i] != 4:
            i += 1
            continue
        else:
            end = False
            for j in range(1, 4):
                if l0[i+j] != 4:
                    i += j+1
                    end = True
                    break
            if end:
                continue
            print(i)
            break  # sol = 134043


# %% Problem 48

def problem_48():
    s = 0
    for i in range(1, 1001):
        s += pow(i, i, 10**10)
        s %= 10**10
    print(s)  # sol = 9110846700


# %% Problem 49

def problem_49():
    l4 = numpy_sieve(10 ** 4)
    i0 = binary_search_inf(l4, 1000)
    l4 = l4[i0 + 1:]

    def permut_ok(n):
        m2 = str(n)
        m = list(m2)
        m.sort()
        for i in range(1, 3):
            n2 = n + i * 3330
            if not binary_search(l4, n2)[0]:
                return False, ""
            n2 = str(n2)
            nn2 = list(n2)
            nn2.sort()
            if nn2 != m:
                return False, ""
            m2 += n2
        return True, m2

    for p in l4:
        if p != 1487:
            ok, s = permut_ok(p)
            if ok:
                print(s)  # sol = 296962999629
                break


# %% Problems 30 to 49

if __name__ == "__main__":
    @timing
    def problem_30_to_49():
        for i in range(30, 50):
            print("p"+str(i)+": ", end="")
            eval("problem_"+str(i)+"()")


    problem_30_to_49()  # Execution of  problem_30_to_49  in  2.70
