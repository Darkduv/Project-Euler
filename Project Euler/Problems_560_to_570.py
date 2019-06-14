# %% Problem 561

from math import sqrt


def prod(m):
    def prime(n, ll):
        for j in ll:
            if n % j == 0:
                return False
        return True

    if m == 0:
        return 1

    elif m == 1:
        return 2

    else:
        i = 3
        l = [2]
        m -= 1
        while m > 0:
            if prime(i, l):
                l.append(i)
                m -= 1
            i += 2
        return l


def s(l, k, i): # ??????????
    return s(l, k-1, i)


def e(m, n):
    p = prod(m) ** n
    k = 0
    while p % 2 == 0:
        k += 1
        p //= 2
    return k


def q(n):
    s = 0
    for i in range(1, n + 1):
        s += e(904961, i)
    return s
# %% Problem 565

"""
def sum_divisor(n, d):
    s_tot = 0
    for j in range(1, n+1):
        s = 0
        for i in range(1, j+1):
            if j % i == 0:
                s += i
        if s % d == 0:
            s_tot += j
    return s_tot

print(sum_divisor(20, 7))

print(sum_divisor(10 ** 6, 2017))
"""
n = 10 ** 6
d = 2017

s_tot = 0
for j in range(1, n+1):
    if j % 2017 == 0:
        s_tot += j
    else:
        s = 0
        for i in range(1, j+1):
            if j % i == 0:
                s += i
        if s % d == 0:
            s_tot += j
print(s_tot)

from math import sqrt
from time import time


def decompo_bidon(n):
    if n % 2 == 0:
        return 2, n // 2
    for j in range(3, min(int(sqrt(n)) + 2, n+1), 2):
        if n % j == 0:
            return j, n // j
    return n, 1

timer = time()
NN = 10 ** 6
L = [0, 1, 3, 4, 7]
i = 5
s = 0
while i < NN:
    j, k = decompo_bidon(i)
    if k % j == 0:
        nb = L[k]
        k //= j
        nn = j*j
        while k % j == 0:
            k //= j
            nn *= j
        if k == 1:
            nb = (j * nn - 1) // (j - 1)
        else:
            nb += nn*L[k]

    else:
        nb = (j + 1) * L[k]
    L.append(nb)
    if nb % 2017 == 0:
        s += nb
    i += 1

print(s)

print(time() - timer)


# %% Problem 566


from math import sqrt


class MyTruc():
    a = 9
    b = 10
    c = 11
    prod = a * b * c

    def __init__(self, aa, bb):
        self.aa = aa
        self.bb = bb

    def __add__(self, other):
        return MyTruc(self.aa + other.aa, self.bb + other.bb)

    def __sub__(self, other):
        return MyTruc(self.aa - other.aa, self.bb - other.bb)

    def __eq__(self, other):
        x = self.aa
        xx = other.aa
        y = self.bb
        yy = self.bb
        return self.aa == other.aa and self.bb == other.bb

    def __float__(self):
        return self.aa + self.bb * sqrt(self.c)

    def __gt__(self, other):
        return self.__float__() > other.__float__()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        x = self.aa
        xx = other.aa
        y = self.bb
        yy = other.bb
        return self.__float__() < other.__float__()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __hash__(self):
        return (self.aa, self.bb).__hash__()

    def __repr__(self):
        return "MyTruc({}, {})".format(self.aa, self.bb)

nb = 1


def F(a, b, c):
    global nb
    MyTruc.a = a
    MyTruc.b = b
    MyTruc.c = c
    one = MyTruc(a * b * c, 0)
    # print(one)
    t1 = MyTruc(b * c, 0)
    t2 = MyTruc(a * c, 0)

    if int(sqrt(c)) ** 2 == c:
        t3 = MyTruc(b * a * int(sqrt(c)), 0)
    else:
        t3 = MyTruc(0, b * a)
    zero = MyTruc(0, 0)
    d = {zero: True, t1: False}
    L = [t1, t2, t3]
    i = 0
    t = t1

    while list(d.values()).count(False) != 0:
        try:
            i += 1
            i %= 3
            t_0 = t
            t += L[i]
            # print(t_0, t, nb)
            if t < one:
                L_part = [el for el in d]
                L_part.sort()
                ok = False
                for el in L_part:
                    if el > t:
                        ok = True
                        d[t] = d[el]
                        break
                    if el == t:
                        ok = True
                        break
                # line 37 of function F
                if not ok:
                    d[t] = d[L_part[0]]

                L_part = [el for el in d]
                L_part.sort()
                # print(L_part)
                # print(d)
                i_0 = L_part.index(t_0)
                i_t = L_part.index(t)
                # print(t, t_0)

                dd = {}
                # print(i_0, i_t)
                for j in range(i_t, i_0, -1):
                    value = d.pop(L_part[j])
                    dd[t - L_part[j - 1] + t_0] = not value
                for j in dd:
                    d[j] = dd[j]
                # print("dd=", dd)
                # print("ok, d=", d)
            else:
                t_1 = t
                t = t - one
                L_part = [el for el in d]
                L_part.sort()
                for el in L_part:
                    if el > t:
                        d[t] = d[el]
                        break
                    if el == t:
                        break
                # print("d = ", d)
                L_part = [el for el in d]
                L_part.sort()

                i_0 = L_part.index(t_0)
                i_t = L_part.index(t)

                dd = {}

                LLL = L_part[i_0:] + L_part[0:i_0]
                L_part = LLL
                i_0 = L_part.index(t_0)
                i_t = L_part.index(t)
                for index in range(i_t, i_0, -1):
                    t_int = L_part[index - 1]
                    if t_int < t_0:
                        t_int = t_int + one
                    jjj = t_1 - t_int + t_0
                    if jjj > one:
                        jjj = jjj - one
                    dd[jjj] = not d.pop(L_part[index])
                for j in dd:
                    d[j] = dd[j]
                # print("hard, d=", d)

            nb += 1
            if nb % 10000 == 0:
                # print(nb)
                pass

            if nb > 1000000:
                raise Exception("help!!!!!!")

        except ValueError as e:
            print(nb, d, t_0, t, i_0, i_t, sep="\n")
            print(e)
            break

    # print("yo")
    return nb

print(F(9, 10, 11))
print(F(10, 14, 16))


