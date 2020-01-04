# %% Problem 233

from Tools import is_square


def f(n):
    nb = 0
    for x in range(n // 2 + 1, int((n/2)*(1+2**0.5))+1):
        c_2 = n ** 2 - 4 * x ** 2 + 4 * n * x
        if is_square(c_2):
            nb += 1
        if nb > 105:
            return 500
    return nb * 4


s = 0
for n in range(1, 100000000001):
    if f(n) == 420:
        s += n
print(s)

n = 3646

# %% Problem 235

sn = 5000
sm = -2 * 10**11
s, r, d = 0, 1, 0.1
while abs(s - sm) > 1:
    s = sum([(300 - k) * r**(k-1) for k in range(1, sn+1)])
    r += d if s > sm else -d
    d /= 2
print("Answer to PE 235 = %.12f" % r)  # 1.002322108633

# %% Problem 243

from Tools import phi


def resilient(n):
    return phi(n), n-1

n = 9699690
a = 1
b = 0

while 94744 * a >= 15499 * b:
    n += 9699690
    a, b = resilient(n)


# %% Problem 250


L = [p.__pow__(p, 250) for p in range(1, 250251)]


LL = [L[0], None]

nb = 0
if L[0] == 0:
    nb += 1

for p in range(250250):
    l = []
    for i in LL:
        if i is not None:
            l.append((i+L[p]) % 250)
            if (i + L[p]) % 250 == 0:
                nb += 1
    LL.extend(l)

print(nb)
