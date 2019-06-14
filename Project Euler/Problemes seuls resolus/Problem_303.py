# %% Problem 303
def f(n):
    not_visit = [True]*n
    pred = [(-1, -1)]*n
    pred[0] = 0, 0
    file = [0]
    again = True
    a, r = -1, -1
    while again:
        a = file.pop(0)
        for r in range(3):
            v = (10*a+r)%n
            if v == 0 and (a !=0 or r != 0):
                again = False
                break
            if not_visit[v] and v != 0:
                file.append(v)
                not_visit[v] = False
                pred[v] = a, r
    s = str(r)
    a2, r = pred[a]
    while a2 != a:
        s = str(r)+s
        a = a2
        a2, r = pred[a2]
    return int(s)


s = 0
for k in range(1, 10000 + 1):
    s += f(k) // k
print(s)  # sol = 1111981904675169
