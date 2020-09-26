# %% Problem 197


def f(x):
    return int(2**(30.403243784-x**2))*10**-9

u0 = -1
u = u0
for i in range(10**4):
    u0, u = u, f(u)
c = u0+u

print(c)

# 1.710637717
