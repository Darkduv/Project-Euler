# %% Problem 614

L = [0]*(10**7+1)
L[0] = 1
L[1] = 1
L[2] = 0


def ok(a):
    return a % 2 != 0 or a % 4 == 0

for k in range(3, 10**7+1):
    if not ok(k):
        continue
    for j in range(k+1):
        if j + k > 10**7:
            break
        if j == k and ok(k):
            L[j+k] -= 1
        L[j+k] += L[j]
        L[j+k] %= 10**9+7

