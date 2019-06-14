import queue

n = 3
a = 0
s = [0]
p = queue.deque()
p.append((s, a))
nb = []
seen = [s]
while len(p):
    s, a = p.pop()
    if len(s) < 2 ** n - n+1:
        b = (a % (2 ** (n - 1))) << 1
        for r in range(2):
            if b+r not in s:
                s2 = s + [b+r]
                if s2 in seen:
                    continue
                p.append((s2, b+r))
                seen.append(s2)

    else:
        b = a
        add = True
        for _ in range(n-1):
            b = (b % (2 ** (n - 1))) << 1
            if b in s:
                add = False
                break
        if add:
            nb.append(s)


def code(L):
    c = 0
    for i in L:
        c <<= 1
        c += i % 2
    return c


print(sum(code(a) for a in nb))  # sol = 209110240768
