L = [[] for __ in range(10)]
for i in range(10):
    for j in range(10-i):
        L[i].append(1)

for _ in range(3, 21):
    LL = [[] for ___ in range(10)]
    for i in range(10):
        for j in range(10-i):
            LL[i].append(sum(L[j][k] for k in range(10-i-j)))
    L = LL

s = 0
for i in range(1, 10):
    for j in range(10-i):
        s += L[i][j]

print(s)  # s = 378158756814587
