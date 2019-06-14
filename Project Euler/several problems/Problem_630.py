from fractions import Fraction

N = 2500
s = 290797

summit = []
for n in range(N):
    s1 = (s ** 2) % 50515093
    s2 = (s1 ** 2) % 50515093
    t = (s1 % 2000 - 1000, s2 % 2000 - 1000)
    summit.append(t)
    s = s2

d = {}
inf = float('inf')


def value(i, j):
    x1, y1 = summit[i]
    x2, y2 = summit[j]
    if x1 == x2:
        return inf
    else:
        return Fraction(y2 - y1, x2 - x1)


n_tot = 0


def line(i, j):
    global n_tot
    a = value(i, j)
    x1, y1 = summit[i]
    if a != inf:
        b = y1 - a*x1
    else:
        b = x1
    if a in lines and b in lines[a]:
        return False
    elif a in lines:
        lines[a].add(b)
    else:
        lines[a] = {b}
    n_tot += 1
    return True


lines = dict()

for i in range(N):
    for j in range(i+1, N):
        line(i, j)

s_tot = 0
for a in lines:
    s_tot += (n_tot - len(lines[a]))*len(lines[a])
print(s_tot)