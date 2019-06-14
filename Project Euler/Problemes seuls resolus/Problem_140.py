# %% Problem 140

# golden_nuggets = [2, 5, 21, 42, 152] and it appears that u(n+5) = u(n+4) +7 * u(n+3)-7*u(n+2) -u(n+1)+u(n)
# so:

L = [2, 5, 21, 42, 152]
for i in range(6, 31):
    L.append(L[-5]-L[-4]-7*L[-3]+7*L[-2]+L[-1])

print(sum(L))


from math import sqrt
N = 211345365
lim = N**2  # arbitrary, hoping it will work !!


def l1():
    global a, b
    return a + b*sqrt(5)


def l2():
    global a, b
    return a - b*sqrt(5)


def n_k_a_b(k, u, v):
    c = int(1/2*(l1()**(k-1)*(u-v*sqrt(5))+l2()**(k-1)*(u+v*sqrt(5)))-7+0.1)
    if c > lim*5:
        return 0
    if c % 5 == 0:
        return c//5
    return 0

a, b = 9, 4


def next1(b):
    from Tools import is_square
    while not is_square(1+5*b**2):
        b += 1
    return int(sqrt(1+5*b**2)+0.05), b


def next2(v):
    a = 44+5*v**2
    while int(a**0.5+0.1)**2 != a:
        v += 1
        a = 44 + 5 * v ** 2
    return int(a**0.5+0.1), v


def ok(n):
    a = 5*n**2 + 14*n+1
    return int(a**0.5+0.1)**2 == a


ll_n = []

v = 0
for _ in range(30):
    u, v = next2(v+1)
    for k in range(30):
        c = n_k_a_b(k, u, v)
        if c > 0 and c not in ll_n:
            if not ok(c):
                # print(c, a, b, u, v)
                pass
            else:
                ll_n.append(c)
a, b = next1(b)
v = 0
for loop in range(20):
    u, v = next2(v+1)
    for k in range(25):
        c = n_k_a_b(k, u, v)
        if c > 0 and c not in ll_n:
            if not ok(c):
                # print(c, a, b, u, v)
                pass
            else:
                ll_n.append(c)
ll_n.sort()
print(ll_n[:30])
print(ll_n.index(N))  # must be 19
print(sum(ll_n[:30]))
