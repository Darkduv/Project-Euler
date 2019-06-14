# %% Problem 566


from math import sqrt


class MyTruc:
    a = 9
    b = 10
    c = 11
    prod = a * b * c

    def __init__(self, aa, bb):
        self.aa = aa
        self.bb = bb

    def __add__(self, other):
        one = MyTruc(self.prod, 0)
        aaa = self.aa + other.aa
        bbb = self.bb + other.bb
        added = MyTruc(aaa, bbb)
        while added >= one:
            aaa -= self.prod
            added = MyTruc(aaa, bbb)
        return added

    def __sub__(self, other):
        aaa = self.aa - other.aa
        bbb = self.bb - other.bb
        subbed = MyTruc(aaa, bbb)
        while subbed <= MyTruc(0, 0):
            aaa += self.prod
            subbed = MyTruc(aaa, bbb)
        return subbed

    def __eq__(self, other):
        x = self.aa
        xx = other.aa
        y = self.bb
        yy = other.bb
        return self.aa == other.aa and self.bb == other.bb

    def __float__(self):
        return self.aa + self.bb * sqrt(self.c)

    def __gt__(self, other):
        return self.__float__() > other.__float__()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return self.__float__() < other.__float__()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __hash__(self):
        return (self.aa, self.bb).__hash__()

    def __repr__(self):
        return "MyTruc({}, {})".format(self.aa, self.bb)


def F(a, b, c):

    MyTruc.a = a
    MyTruc.b = b
    MyTruc.c = c
    MyTruc.prod = a * b * c
    one = MyTruc(a * b * c, 0)
    # print(one)
    t1 = MyTruc(b * c, 0)
    t2 = MyTruc(a * c, 0)

    if False:  # if int(sqrt(c)) ** 2 == c:
        cc = int(sqrt(c))
        MyTruc.a = a
        MyTruc.b = b
        MyTruc.c = cc
        MyTruc.prod = a * b * cc
        one = MyTruc(a * b * cc, 0)
        # print(one)
        t1 = MyTruc(b * cc, 0)
        t2 = MyTruc(a * cc, 0)
        t3 = MyTruc(b * a, 0)

    else:
        MyTruc.a = a
        MyTruc.b = b
        MyTruc.c = c
        MyTruc.prod = a * b * c
        one = MyTruc(a * b * c, 0)
        # print(one)
        t1 = MyTruc(b * c, 0)
        t2 = MyTruc(a * c, 0)
        t3 = MyTruc(0, a * b)

    zero = MyTruc(0, 0)

    d = {zero: True, t1: False}
    L = [t1, t2, t3]
    i = 0
    t = t1
    nb = 1
    t_0 = t
    i_t = 0
    i_0 = 0

    while list(d.values()).count(False) != 0:
        try:
            i += 1
            i %= 3
            t_0 = t
            t += L[i]
            # print(t_0, t, nb)
            if t > t_0:
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
                    tttt = t - L_part[j - 1] + t_0
                    dd[tttt] = not value
                for j in dd:
                    d[j] = dd[j]
                # print("dd=", dd)
                # print("ok, d=", d)
            else:
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

                LLL = L_part[i_0:] + L_part[0:i_t+1]
                L_part2 = LLL.copy()

                i_0 = L_part2.index(t_0)
                i_t = L_part2.index(t)
                for j in range(i_t, i_0, -1):
                    value = d.pop(L_part2[j])
                    dd[t - L_part2[j - 1] + t_0] = not value

                    """
                    t_int = L_part2[j - 1]
                    if t_int < t_0:
                        t_int = t_int + one
                    jjj = t - t_int + t_0
                    if jjj > one:
                        jjj = jjj - one
                    dd[jjj] = not d.pop(L_part2[j])
                    """

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
            print("___________.:ERROR:.___________")
            print(nb, d, t_0, t, i_0, i_t, sep="\n")
            print("____________.:END:.____________")
            print(e)
            break
    # print("yo")
    return nb


def G(n):
    nb_tot = 0
    for a in range(9, n-1):
        for b in range(a+1, n):
            for c in range(b+1, n+1):
                nb_tot += F(a, b, c)
    return nb_tot


print(F(9, 10, 11))
print(F(10, 14, 16))  # 506
# print(F(15, 16, 17))  # 785232
print(G(11))
print(G(14))
# G(n) = sum 9<=a<b<c<=n F(a, b, c)
# G(11) = 60
# G(14) = 58020
# G(17) = 1269260
# G(19) =??     it was the question, wasn't ??
