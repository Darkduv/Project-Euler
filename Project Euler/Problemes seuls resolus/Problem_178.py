# %% Problem 178

l = [{}, {(i, i, i, i): 1 for i in range(1, 10)}]

for _ in range(2, 41):
    d = {}
    for (k, a, b, c) in l[-1]:
        if c < 9:
            d[k, max(a, c+1), b, c+1] = d.get((k, max(a, c+1), b, c+1), 0) + l[-1][k, a, b, c]
        if c > 0:
            d[k, a, min(b, c-1), c - 1] = d.get((k, a, min(b, c-1), c - 1), 0) + l[-1][k, a, b, c]
    l.append(d)

n = 0
for i in range(10, 41):
    for k, a, b, c in l[i]:
        if a == 9 and b == 0:
            n += l[i][k, a, b, c]
print(n)  # sol = 126461847755
