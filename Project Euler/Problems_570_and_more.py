# %% Problem 571


def pan_b(b, n):
    # L = []
    ok = [False for _ in range(b)]
    n_ok = 0
    while n > 0:
        n, r = int.__divmod__(n, b)
        # L.append(r)
        if not ok[r]:
            n_ok += 1
            ok[r] = True
        if n_ok == b:
            return True
    return False


def n_super_pan(nb, n):
    ok = True
    for b in range(4, n):  # deja vérifié pour b = n par construct. Et ok pour b=4 => ok pour b=2, idem avec 9 et 3
        if not pan_b(b, nb):
            ok = False
            break
    return ok


def next_permut(l):
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
        return l[i::-1] + [m] + l[i + 2::]


class PotentialPanNumber:
    def __init__(self, b):
        self.base = b
        self.list = ([1, 0] + [i for i in range(2, b)])[::-1]
        # self.ok = [1 for _ in range(b)]
        # self.len = b

    def value(self):
        nb = 0
        for r in self.list[::-1]:
            nb *= self.base
            nb += r
        return nb

    def incr(self):
        self.list = next_permut(self.list)
        # print(self, self.list)
        return self.value()


from time import time

t = time()
n = PotentialPanNumber(12)
count = 0
s = 0
while count < 10:
    nb = n.incr()
    if n_super_pan(nb, 12):
        count += 1
        s += nb
print(s)

print(time() - t)  # sol =  30510390701978


#######

# %% Problem 575
# %% Todo : it doesn't work :-(

def ok(i, j, n):
    return 0 <= i < n and 0 <= j < n


def neighbour(i, j, n):
    L = [(i, j + 1), (i + 1, j), (i - 1, j), (i, j - 1), (i, j)]
    return [(i, j) for i, j in L if ok(i, j, n)]


def aux1(L, n):
    M = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            p = 0
            L_neighbour = neighbour(i, j, n)
            v = len(L_neighbour)
            for ii, jj in L_neighbour:
                M[ii][jj] += L[i][j] * 1 / v
    return M


def aux2(L, n):
    M = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            p = 0
            L_neighbour = neighbour(i, j, n)
            v = len(L_neighbour)
            for ii, jj in L_neighbour:
                if ii == i and jj == j:
                    M[ii][jj] += 1 / 2 * L[i][j]
                else:
                    M[ii][jj] += L[i][j] * 1 / (2 * v - 2)
    return M


from math import sqrt


def square_numbered(n):
    L = []
    for m in range(1, n + 1):
        i = (m ** 2 - 1) // n
        j = (m ** 2 - 1) % n
        L.append((i, j))
    return L


def p_575(n, nb):
    L_prob = []
    for i in range(n):
        for j in range(n):
            L = [[0] * n for i in range(n)]
            LL = [[0] * n for i in range(n)]
            LL[i][j] = 1
            L[i][j] = 1
            for k in range(nb):
                L = aux1(L, n)
                LL = aux2(LL, n)
            L_prob.append((L, LL))
    L_tot = [[[0, 0]] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for L1, L2 in L_prob:
                L_tot[i][j][0] += L1[i][j]
                L_tot[i][j][1] += L2[i][j]
    s = 0
    for l in L_prob[-1][0]:
        print(l)
        s += sum(l)
    print(s)
    p1, p2 = 0, 0
    for i_s, j_s in square_numbered(n):
        p1 += L_tot[i_s][j_s][0]
        p2 += L_tot[i_s][j_s][1]
    return (p1 / (n ** 2 * nb) + p2 / (n ** 2 * nb)) / 2


print(p_575(5, 500))

# %% Problem 577

L = [0, 0, 0, 1, 3]
for n in range(5, 12346):
    a = 3 * (L[-1] - L[-2]) + L[-3]
    a += 0 if n % 3 != 0 else n // 3
    L.append(a)
print(sum(L))  # 265695031399260211

# %% Problem 587

from math import asin, pi, sqrt


def f(n):
    a = -asin((sqrt(2 * n) + 1) / (sqrt(2 * n) + n + 1)) / 2 - (sqrt(2 * n) + 1) * sqrt(
        n * (2 * sqrt(2 * n) + n + 2) / (sqrt(2 * n) + n + 1) ** 2) / (2 * (sqrt(2 * n) + n + 1)) + (4 * sqrt(
        2 * n) + 2 * n ** (3 / 2) * sqrt(2) + 7 * n + 2) / (2 * (sqrt(2 * n) + 1 + n) ** 2) - 1 / 1000 * (1 - pi / 4)
    return a


n = 1
while f(n) > 0:
    n += 1
print(n)  # sol =  	2240
