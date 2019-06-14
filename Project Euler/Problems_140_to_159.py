# %% Problem 140

# cf Problem 137, 138, 139  ---> tangentes ?

# ici -> intersection ??


# A_G(x) = (3*x**2+x)/(x**2+x-1)
# A_G(x) = n avec x rationnel => 5n**2+14n+1=y**2

# f(x) = sqrt(5x**2+14x+1)
def f_prime(x, y):
    return 5*x+7, y


x1, y1 = 0, 1
x2, y2 = 2, 7


def next(x1, y1, x2, y2):
    a, b = f_prime(x2, y2)
    x3 = (14*b**2 - 2*a*(b*y1-a*x1))//(a**2 - 5*b**2)-x1
    y3 = (a*(x3-x1))//b + y1
    return x3, y3

count = 2
s = x2+x1
while count < 30:
    if count == 20:
        print("G20 = ", x2)
    x3, y3 = next(x1, y1, x2, y2)
    x1, y1, x2, y2 = x2, y2, x3, y3
    count += 1
    s += x2
    print(x2)
print(s)


# %% Problem 144

a = 0
b = 10.1
c = 1.4
d = -9.6

m1 = (d - b) / (c - a)

a = 1.4
b = -9.6

nb = 0

while True:

    m2 = -4 * c / d
    m3 = (2 * m2 - m1 * (1 - m2 * m2)) / (1 - m2 * m2 + 2 * m1 * m2)

    m1 = m3
    if abs(a) <= 0.01 and b > 0:
        break
    if m1 == 1:
        c = a
        d = -b
    else:
        e = (2 * m1 * b + 8 * a) / (4 + m1 * m1)
        c = a - e
        d = b - m1 * e
        a, b = c, d
    nb += 1
print(a, " and nb= ", nb)  # nb = 354


# %% Problem 145

def reversible(n):
    if n % 10 == 0:
        return False
    s = n + int(str(n)[::-1])
    if s % 2 == 0:
        return False
    l_s = list(str(s))[::-1]
    if int(l_s[-1]) % 2 == 0:
        return False
    for i in l_s:
        if int(i) % 2 == 0:
            return False
    return True

nb = 0
for i in range(10**9):
    if reversible(i):
        nb += 1
print(nb)  # sol = 608720

# %% Problem 148


# %% Problem 149

Sk = [0]
for k in range(1, 56):
    Sk.append(((100003 - 200003*k + 300007*k**3) % 1000000) - 500000)
for k in range(56, 4000001):
    Sk.append(((Sk[k - 24] + Sk[k - 55]+1000000) % 1000000) - 500000)

mat = [[0]*2000 for _ in range(2000)]
for k in range(1, 4000001):
    i = (k-1) // 2000
    j = (k-1) % 2000
    mat[i][j] = Sk[k]

max_mat = 0
for l in mat:
    s = 0
    for a in l:
        if s < 0:
            s = a
        else:
            s += a
        if s > max_mat:
            max_mat = s
for j in range(2000):
    s = 0
    for i in range(2000):
        if s < 0:
            s = mat[i][j]
        else:
            s += mat[i][j]
        if s > max_mat:
            max_mat = s

for i0 in range(2000):
    for j0 in range(2000):
        if i0 == 0 or j0 == 0:
            i = i0
            j = j0
            s = 0
            while i < 2000 and j < 2000:
                if s < 0:
                    s = mat[i][j]
                else:
                    s += mat[i][j]
                if s > max_mat:
                    max_mat = s
                i += 1
                j += 1
        if j0 == 0 or i0 == 1999:
            i = i0
            j = j0
            s = 0
            while i > 0 and j < 2000:
                if s < 0:
                    s = mat[i][j]
                else:
                    s += mat[i][j]
                i -= 1
                j += 1
                if s > max_mat:
                    max_mat = s
print(max_mat)

# %% Problem 154


def v_p(n, p):  # return the valuation of p prime in n!
    s = 0
    m = p
    while n >= m:
        s += n//m
        m *=p
    return s

N = 200000
v2N = v_p(N, 2)
v5N = v_p(N, 5)
v_2 = [v_p(k, 2) for k in range(N+1)]
v_5 = [v_p(k, 5) for k in range(N+1)]


def ok(i, j):  # return if the coefficient of x^i*y^j*z^(200000-i-j) in (x+y+z)^200000 is divisible by 10**12
    s = v_2[i]+v_2[j]+v_2[N-i-j]
    if v2N - s < 12:
        return False
    s = v_5[i]+v_5[j]+v_5[N-i-j]
    if v5N - s < 12:
        return False
    return True

nb = 0
for i in range(N//3+1, N):
    if ok(i, i):
        nb += 3
    for j in range((N-i)//2, i):
        if N-i-j > j:
            continue
        elif N-j-i == j:
            a = 3
        else:
            a = 6
        if ok(i, j):
            nb += a
print(nb)


# %% Problem 157

# see prblemes seuls résolus ?

# %% Problem 158


def f(l, n):
    if n == 0:
        nb = 0
        print(l)
        for elel, ver in l:
            if ver != 0:
                nb += 1
        return nb

    lll = []
    for el, verif in l:
        for j in range(26):
            if j >= el:
                if verif == 0:
                    lll.append([j, 1])
            else:
                lll.append([j, verif])
    return f(lll.copy(), n-1)

l_ = [[i, 0] for i in range(26)]
print(f(l_, 1))

max = 0
i_max = 0
for n in range(2, 27):
    if f(l, n-1) > max:
        max = f(l, n-1)
        i_max = n


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def cPn(p, n):
    return fact(n) // (fact(p) * fact(n - p))


def p(n):
    return cPn(n, 26)*(2**n-n-1)


print(max(p(n) for n in range(2, 27)))