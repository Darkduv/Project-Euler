# %% Problem 315


from Tools import numpy_sieve
from To_be_studied import prime_sieve
l_AB = numpy_sieve(2*(10**7))
l_AB = prime_sieve(2*10**7)
l_fed = [i for i in l_AB if i > 10**7]

# Horizontal, top to bottom : 1, 2, 3
# Vertical, left, top to bottom: 4, 5
# Vertical, right, top to bottom: 6, 7
digit = {0: [1, 3, 4, 5, 6, 7], 1: [6, 7], 2: [1, 2, 3, 5, 6], 3: [1, 2, 3, 6, 7], 4: [2, 4, 6, 7], 5: [1, 2, 3, 4, 7],
         6: [1, 2, 3, 4, 5, 7], 7: [1, 4, 6, 7], 8: [1, 2, 3, 4, 5, 6, 7], 9: [1, 2, 3, 4, 6, 7]}
cost = {}
for i in digit:
    cost[i] = len(digit[i])


def cost_sam(n):
    s = 0
    for a in str(n):
        s += cost[int(a)]
    return s


def sam(n):
    s = cost_sam(n)
    while n >= 10:
        n = sum(int(a) for a in str(n))
        s += cost_sam(n)
    return s*2

total_cost_sam = 0
for n in l_fed:
    total_cost_sam += sam(n)


def cost_max(a, b):
    if a is None:
        return cost_sam(b)
    elif b is None:
        return cost_sam(a)
    l1 = [int(c) for c in str(a)][::-1]
    l2 = [int(c) for c in str(b)][::-1]
    s = 0
    m = len(l2)
    for k in range(m):
        for c in digit[l1[k]]:
            if c not in digit[l2[k]]:
                s += 1
        for c in digit[l2[k]]:
            if c not in digit[l1[k]]:
                s += 1
    for d in l1[m:]:
        s += cost[d]
    return s


def max(n):
    s = cost_max(None, n)
    while n >= 10:
        m = n
        n = sum(int(a) for a in str(m))
        s += cost_max(m, n)

    s += cost_max(n, None)
    return s

total_cost_max = sum(max(n) for n in l_fed)


print(total_cost_sam - total_cost_max)
# solution
# = 13625242.
