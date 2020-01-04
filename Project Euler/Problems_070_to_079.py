from Tools import phi, decompose_tout, numpy_sieve, anagram, gcd

# %% Problem 70

l_prime = numpy_sieve(4000)
l_test = []
n = 10**7
le = len(l_prime)
for i in range(le-1):
    for j in range(i+1, le):
        nb = l_prime[i] * l_prime[j]
        if nb < n:
            l_test.append(nb)
L_permute = []
for j in l_test[::-1]:
    if anagram(j, phi(j)):
        L_permute.append(j)

L_bis = [(i, i/phi(i)) for i in L_permute]
L_bis.sort(key=lambda x: x[1])
print(L_bis[0])


# %% Problem 71


a, b = 2, 5
for d in range(9, 1000001):
    for n in range((a * d) // b, (3 * d) // 7 + 1):
        if gcd(d, n) == 1:
            if a*d < n*b:
                a, b = n, d
print(a, b)

# %% Problem 72

d = dict()
l_erato = numpy_sieve(10**6)
for i in l_erato:
    d[i] = i - 1

s = 0
for i in range(2, 10**6+1):
    ll = decompose_tout(i, l_erato)
    p = 1
    for i, k in ll:
        p *= (i ** (k-1)) * d[i]
    s += p


# %% Problem 73


def gcd(a, b):
    if a < b:
        r = b % a
        return gcd(a, r)
    elif b == a:
        return b
    elif b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

nb = 3
for d in range(9, 12001):
    for n in range(d // 3 + 1, d // 2 + 1):
        if gcd(d, n) == 1:
            nb += 1
print(nb)

# %% Problem 74

l_fact = [1]
for i in range(1, 10):
    l_fact.append(l_fact[-1] * i)
# print(l_fact)


def next_one(n):
    s = 0
    while n > 0:
        s += l_fact[n % 10]
        n //= 10
    return s


nb = 0
for j in range(2, 1000000):
    i = j
    ll = []
    while i not in ll:
        ll.append(i)
        i = next_one(i)
        if len(ll) > 60:
            break
    if len(ll) == 60:
        nb += 1
print(nb)

# %% Problem 75


from Tools import gcd

L_max = 1500000
L = [0 for _ in range(L_max+1)]

for p in range(1, int((L_max/2)**0.5)):
    if p % 2 == 0:
        for q in range(1, min(p, int(L_max/(2*p)-p)+1), 2):
            if gcd(p, q) == 1:
                l = 2*p**2+2*p*q
                for k in range(l, L_max+1, l):
                    L[k] += 1
    else:
        for q in range(2, min(p, int(L_max / (2 * p) - p) + 1), 2):
            if gcd(p, q) == 1:
                l = 2 * p ** 2 + 2 * p * q
                for k in range(l, L_max + 1, l):
                    L[k] += 1

print(L.count(1))

# %% Problem 76

mat1 = [[1]*101 for i in range(101)]

for i in range(2, 101):
    for j in range(2, 101):
        mat1[i][j] = mat1[i][j-1]
        if i >= j:
            mat1[i][j] += mat1[i-j][j]

mat2 = [[1]*101 for i in range(101)]

for i in range(2, 101):
    for j in range(2, 101):
        mat2[i][j] = mat2[i][j-1]
        if i > j:
            mat2[i][j] += mat1[i-j][j]

print(mat2[5][5])


# %% Problem 77


L_6 = numpy_sieve(500)
ll = len(L_6)
mat1 = [[0]*ll for i in range(ll)]

for i in range(ll):
    mat1[0][i] = 1
    mat1[i][0] = (i + 1) % 2

for i in range(1, ll):
    for j in range(1, ll):
        mat1[i][j] = mat1[i][j-1]
        if i >= L_6[j]:
            mat1[i][j] += mat1[i-L_6[j]][j]

mat2 = [[0]*ll for i in range(ll)]

for i in range(4, ll, 2):
    mat2[i][0] = 1

for i in range(1, ll):
    for j in range(1, ll):
        mat2[i][j] = mat2[i][j-1]
        if i > L_6[j]:
            mat2[i][j] += mat1[i-L_6[j]][j]
print(mat2[ll-1][ll-1])

i = 0
while mat2[i][ll - 1] < 5000:
    i += 1
print(i)

# %% Problem 78


from Tools import partition

n = 1
d = dict()
while partition(n, d) != 0:
    n += 1
print(n)


# %% Problem 79
import os
os.chdir('/Users/maximin/Desktop/Euler/linked_files')


L = [False] * 10
with open('p079_keylog.txt', 'r') as f:
    for i in f:
        for n in i[:-1]:
            L[int(n)] = True
L = [i for i in range(10) if L[i]]

with open('p079_keylog.txt', 'r') as f:
    nb = 0
    for i in f:
        nb += 1
        l = []
        for a in i[:-1]:
            j = L.index(int(a))
            l.append((int(a), j))
        a, i0 = l[0]
        b, j = l[1]
        c, k = l[2]
        if i0 < j < k:
            pass
        elif i0 < k < j:
            L[j], L[k] = L[k], L[j]
        elif k < j < i0:
            L[i0], L[k] = L[k], L[i0]
        elif k < i0 < j:
            L[k], L[i0], L[j] = L[i0], L[j], L[k]
        elif j < i0 < k:
            L[i0], L[j] = L[j], L[i0]
        else:
            L[j], L[k], L[i0] = L[i0], L[j], L[k]

for i in L:
    print(i, end="")
print()
# ### n = 73162890
