# %% Problem 304


from Tools import numpy_sieve

l_8 = numpy_sieve(10**8+8)

l_14 = [i for i in range(10**14, 10**14+1+10**7)]

for p in l_8:
    a = ((10**14)//p)*p-10**14
    b = (((10**14+1+10**10)//p)+1)*p-10**14
    if a < 0:
        a += p
    m = len(l_14[a:b:p])
    l_14[a:b:p] = [0]*m

l_14 = [i for i in l_14 if i != 0]
r = 1234567891011


def my_pow(a, b, n):
    r2 = r*2
    if n == 0:
        return 1, 0
    elif n == 1:
        if b < 0:
            b = -((-b) % r)
        else:
            b %= r
        return a % r, b
    if n % 2 == 0:
        aa, bb = my_pow(a, b, n//2)
        e = aa*bb
        if e < 0:
            e = -((-e) % r2)
        else:
            e %= r2
        return ((((aa**2)+(bb**2)*5)//2) % r2), e
    else:
        c, d = my_pow(a, b, n // 2)
        e = c * d
        if e < 0:
            e = -((-e) % r2)
        else:
            e %= r2
        cc, dd = ((c ** 2 + (d ** 2) * 5)//2) % r2, e
        bb = (cc*b+a*dd)//2
        if bb < 0:
            bb = -((-bb) % r2)
        else:
            bb %= r2
        aa = (cc*a+5*dd*b)//2
        if aa < 0:
            aa = -((-aa) % r2)
        else:
            aa %= r2
        return aa, bb


def fibo(n):
    a1, b1 = my_pow(1, 1, n)
    a2, b2 = my_pow(1, -1, n)
    if b1 - b2 < 0:
        print(n)
        raise ValueError
    return int(((b1-b2)//2) % r)

s = 0
for n in range(0, 100000):
    s += fibo(l_14[n])
    s %= r
print(s)
# sol == 283988410192
