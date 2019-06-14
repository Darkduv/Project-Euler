from queue import deque


def nb_circle(x):
    return int(x**0.5)

f_tot = deque()
for a in [1, 1, 2, 1, 3, 2, 4, 1, 5, 3, 6, 2, 7, 8, 4, 9, 1, 10, 11, 5]:
    f_tot.append(a)
_next = 12
f_to_do = deque()
for a in [3, 6, 2, 7, 8, 4, 9, 1, 10, 11, 5]:
    f_to_do.append(a)
nb = 20

while nb < 10**9:
    nb += 1
    a = f_to_do.popleft()
    k = 0
    while k < nb_circle(a):
        k += 1
        f_to_do.append(_next)
        f_tot.append(_next)
        _next += 1
print("yo")
s = 0
for i in range(10**3):
    s += f_tot.popleft()