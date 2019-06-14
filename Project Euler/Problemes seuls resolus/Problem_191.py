# %% Problem 191

L = [1, 2, 4, 7]
for k in range(4, 31):
    L.append(L[-1]+L[-2]+L[-3])
n = 0
for i in range(1, 31):
    n += L[i-1]*L[30-i]

print(n+L[30])
