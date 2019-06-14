# %% Problem 539


def P(n):
    a = 1
    b = n
    k = 1
    while b > a:
        a += k
        k *= 2
        b -= (b-a) % k
        if b <= a:
            return a
        b -= k
        k *= 2
        a += (b-a) % k
    return a


def S(n):
    s = 0
    for k in range(1, n+1):
        s += P(k)
    return s

s = 0
for k in range(1, 10**18+1):
    s += P(k)
    s %= 987654321
print(s)
