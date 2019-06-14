def factor(n):
    ff, factors, prime_gaps = 1, [], [2, 4, 2, 4, 6, 2, 6, 4]
    if n < 1:
        return []
    while True:
        for gap in ([1, 1, 2, 2, 4] if ff < 11 else prime_gaps):
            ff += gap
            if ff * ff > n:  # If ff > n ** 0.5
                if n == 1:
                    return factors
                else:
                    return factors + [(n, 1)]
            if not n % ff:
                e = 1
                n //= ff
                while not n % ff:
                    n //= ff
                    e += 1
                factors.append((ff, e))


def prime(p):
    l = factor(p)
    return len(l) == 1 and l[0][1] == 1


def f(d, i, length=10):
    s = 0
    n = d*int("0"+"1"*i)*10**(length-i)+d*int("0"+"1"*(length-1-i))
    k = 10**(length-1-i)
    for j in [1, 2, 4, 5, 7, 8]:
        if j == d:
            continue
        m = n+j*k
        if prime(m):
            s += m
    return s


def f2(d, length=10):
    ss = 0
    for i in range(length):
        ss += f(d, i, length)
    return ss


# for d in 0, 2, 8, f doesn't work

s_tot = sum(f2(d) for d in range(1, 10))

# for d = 0

for i in range(1, 10):
    for j in range(1, 10, 2):
        n = i*10**9 + j
        if prime(n):
            s_tot += n


# for d = 2, 8 ?

for d in [2, 8]:
    for i1 in range(1, 10):
            n = int("1"*9)*10*d - d*(10**i1)
            for j1 in range(10):
                if i1 == 9 and j1 == 0:
                    continue
                for j2 in range(1, 10, 2):
                    m = n+j1*10**i1+j2
                    if prime(m):
                        s_tot += m


print(s_tot)
# s_tot = 612407567715
