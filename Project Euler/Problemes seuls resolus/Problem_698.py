# %% Problem 698

from itertools import permutations
from Tools import fact

l_a = [0, 1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33, 111, 112, 113]


def compute_lk(la):
    l_k = {}
    for i, a in enumerate(la):
        for j, b in enumerate(la[:i + 1]):
            for c in la[:j + 1]:
                s = a + b + c
                if s not in l_k:
                    l_k[s] = []
                l_k[s].append((a, b, c))

    digits = list(l_k.keys())
    digits.sort()
    return l_k, digits


def find_nb_digits(n, digits, l_k):
    nb = 0

    for d in digits[1:]:
        s = 0
        for a, b, c in l_k[d]:
            s2 = fact(d) // (fact(a) * fact(b) * fact(c))
            if a == b and b == c:
                s += s2
            elif a == b or b == c or a == c:
                s += s2 * 3
            else:
                s += s2 * 6
        if nb + s > n:
            return d, nb
        nb += s
    raise ValueError("l_k is too small for this problem")


def nb_l(a, b, c):
    return fact(a + b + c) // (fact(a) * fact(b) * fact(c))


def f(nb, n, l_comb):
    for d in range(3):
        s2 = 0
        l2 = []
        for abc in l_comb:
            abc2 = abc[:]
            if abc2[d] == 0:
                continue
            abc2[d] -= 1
            s2 += nb_l(*abc2)
            if abc2 not in l2:
                l2.append(abc2)
        if nb + s2 >= n:
            return d + 1, nb, l2, s2
        nb += s2


def prob(nb, n, k, l_comb):
    aa = ""
    for _ in range(k):
        digit, nb, l_comb, s = f(nb, n, l_comb)
        aa += str(digit)
    return int(aa)


def permute_all(l_comb):
    l2 = []
    for a in l_comb:
        for b in permutations(a):
            if list(b) not in l2:
                l2.append(list(b))
    return l2


def solve(n, la):
    digits, l_k = compute_lk(la)
    d, nb = find_nb_digits(n, digits, l_k)
    l_possible = permute_all(l_k[d])
    return prob(nb, N, d, l_possible)


N = 111111111111222333
print(f"the solution of problem 698 is : {solve(N, l_a) % 123123123}")  # sol = 57808202
