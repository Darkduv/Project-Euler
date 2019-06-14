# %% Problem_282

MOD = 14**8


def ackermann(m, n):
    if m == 0:
        return n + 1
    if m == 1:
        return 2 + (n+3) - 3
    if m == 2:
        return 2*(n+3) - 3
    if m == 3:
        return pow(2, (n+3), MOD) - 3
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1) % MOD)

s = 0
for i in range(7):
    s += (ackermann(i, i) % (14**8))
print(s)
