# %% Problem 215

from itertools import combinations

# L, H = 9, 3
L, H = 32, 10

l0 = []
for k in range(L // 2 + 1):
    a = L - k * 2
    if a % 3 == 0:
        l0.append((k, a // 3))

l_row = []
for a, b in l0:
    for li in combinations(list(range(a + b)), a):
        ll = [3] * (a + b)
        for i in li:
            ll[i] = 2
        l_row.append(ll)


def ok(l1, l2):
    ll1 = [sum(l1[:j + 1]) for j in range(len(l1) - 1)]
    s2 = 0
    for b2 in l2[:-1]:
        s2 += b2
        if s2 in ll1:
            return False
    return True


d = {}
for row1 in l_row:
    d[str(row1)] = [row for row in l_row if ok(row, row1)]

d2 = {row: len(d[row]) for row in d}
for _ in range(3, H + 1):
    d3 = {}
    for row in d:
        d3[row] = sum(d2[str(row2)] for row2 in d[row])
    d2 = d3

print(sum(d2.values()))  # 806844323190414
