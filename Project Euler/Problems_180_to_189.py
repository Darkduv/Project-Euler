# %% Problem 183


from math import exp, log
from Tools import gcd
e = exp(1)


def k_max_first(n):
    i = int(n/e)
    j = i - 9 if i >= 10 else 1
    m = log(n/j)*j
    j += 1
    while log(n/j)*j > m:
        m = log(n/j)*j
        j += 1
    return j-1


def k_max(n):
    i = int(n/e)
    j = i + 1
    if n ** i * j ** j > n**j*i**i:
        return i
    return j


def terminating(k):
    while k % 2 == 0:
        k //= 2
    while k % 5 == 0:
        k //= 5
    return k == 1


def d(n):
    k = k_max(n)
    if terminating(k/gcd(k, n)):
        return -n
    return n


s = 0
for n in range(5, 10001):
    s += d(n)
print(s)

# %% Problem 184

l1 = []
N = 105
for a in range(1, N):
    for b in range(1, N):
        if a**2 + b**2 >= N**2:
            break
        l1.append((a, b))
nb1 = 0
dd = dict()
for a, b in l1:
    for c, d in l1:
        if d*a > b*c:
            nb1 += 1
            dd[(c, d)] = 1 + dd.get((c, d), 0)
nb = nb1*(len(l1))
nb += len(l1)*(N-1)**2
nb += (N-1)*(len(l1)**2+nb1*2)
for a, b in dd:
    nb += dd[(a, b)]*dd.get((b, a), 0)
nb *= 4
print(nb)  # sol = 1725323624056


# %% Problem 185

# solved, see "alone solved Problems"

# %% Problem 186

class UnionSet:

    def __init__(self, length):
        self.parent = list(range(length))
        self.row = [0]*length

    def __getitem__(self, item):
        if self.parent[item] != item:
            rep = self[self.parent[item]]
            self.parent[item] = rep
            return rep
        else:
            return item

    def fusion(self, x, y):
        if self.row[x] < self.row[y]:
            self.parent[x] = y
        elif self.row[y] < self.row[x]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.row[x] += 1


class UnionSetSpecial(UnionSet):
    def __init__(self, length):
        UnionSet.__init__(self, length)
        self.nb = [1] * length

    def fusion(self, x, y):
        if x == y:
            return
        if self.row[x] < self.row[y]:
            self.nb[y] += self.nb[x]
            self.parent[x] = y
        elif self.row[y] < self.row[x]:
            self.nb[x] += self.nb[y]
            self.parent[y] = x
        else:
            self.nb[x] += self.nb[y]
            self.parent[y] = x
            self.row[x] += 1


def problem_186():
    N_network = 10 ** 6
    facebook = UnionSetSpecial(N_network)  # manage the list of friends' groups

    def make_friend(u, v):
        u, v = facebook[u], facebook[v]
        facebook.fusion(u, v)

    PM_phone = 524287
    calls = 0  # number of 'successful' calls made
    Sk = []
    k = 1

    while facebook.nb[facebook[PM_phone]] < N_network*99/100:  # nb of friends of the PM < N * 99%
        for _ in range(2):
            if k <= 55:
                Sk.append((100003 - 200003*k + 300007*k**3) % 10**6)
                k += 1
            else:
                Sk.append((Sk[-55]+Sk[-24]) % 10**6)
                del Sk[0]
        caller, called = Sk[-2], Sk[-1]
        if called == caller:
            continue
        make_friend(caller, called)
        calls += 1
        if calls > 2500000:
            break
    print(calls)


# sol = 2325629

# %% Problem 187

from Tools import numpy_sieve

l = numpy_sieve(5*10**7)
le = len(l)

nb = 0

for i in range(le):
    ok = False
    for j in range(i, le):
        if l[i] * l[j] < 10 ** 8:
            nb += 1
            ok = True
        else:
            break
    if not ok:
        break
print(nb)


# %% Problem 188


from Tools import phi, timing


@timing
def prob188():
    m = 10**8
    l = [m]
    for i in range(1850):
        m = phi(m)
        if m == 1:
            break
        l.append(m)

    a = 1
    for b in l[::-1]:
        a = pow(1777, a, b)
    return a

print(prob188())

# %% Problem 189

from itertools import product


def other(a):
    if a == 0:
        return [1, 2]
    elif a == 1:
        return [0, 2]
    else:
        return [0, 1]


def ok_l1(l):
    l_aux = [other(a) for a in l]
    return product(*l_aux)


def ok(*l):
    for a in [0, 1, 2]:
        if a not in l:
            yield a


def next1(d):
    d2 = dict()
    for l in d:
        for l2 in ok_l1(l):
            d2[l2] = d[l] + d2.get(l2, 0)
    return d2


def ok_l2(l):
    l_aux = [other(l[0])]
    for i in range(len(l)-1):
        l_aux.append(list(ok(l[i], l[i+1])))
    l_aux.append(other(l[-1]))
    return product(*l_aux)


def next2(d):
    d2 = dict()
    for l in d:
        for l2 in ok_l2(l):
            d2[l2] = d[l] + d2.get(l2, 0)
    return d2


d = {(0,): 1, (1,): 1, (2,): 1}
for i in range(7):
    d = next1(d)
    d = next2(d)
print(sum(d.values()))






