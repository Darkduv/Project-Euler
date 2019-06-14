# %% Problem 220


D = [(1j, -1)]
for _ in range(1, 40):
    a, b = D[-1]
    D.append((a-b, a+b))


def my_bin(n):
    l = []
    while n > 0:
        n, r = int.__divmod__(n, 2)
        l.append(r)
    return l


def position(n):
    l = my_bin(n)
    pos = D[len(l)-1][0]
    e = 1
    for i in range(len(l)-2, -1, -1):
        if l[i]:
            pos -= D[i][0]*e

        if not l[i + 1] and l[i]:
            e *= -1
    x, y = int(pos.real), int(pos.imag)
    print("{},{}".format(x, y))

position(10**12)
# see grep's post at page of the thread
