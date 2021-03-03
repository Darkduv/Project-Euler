def base7(n):
    ll = []
    while n > 0:
        ll.append(n % 7)
        n //= 7
    return ll[::-1]


def f(n):
    l_n = base7(n)
    s = 0
    a = 1
    for i, d in enumerate(l_n):
        j = len(l_n) - 1 - i
        for k in range(0, d):
            s += 28 ** j * (k + 1) * a
        a *= (d + 1)
    return s


print(f"f(100)={f(100)}")  # sol = 2361
print(f"f(10**9)={f(10 ** 9)}")  # sol = 2129970655314432
