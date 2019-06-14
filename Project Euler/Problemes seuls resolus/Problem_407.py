from Tools import decompose


def function_m(n):
    p = decompose(n)[-1]
    q = n // p
    i = q-1
    while i > 0 and ((i*p)**2 - i*p) % n != 0:
        i -= 1
    nb = i*p
    i = q-1
    while i > 0 and ((i*p+1) ** 2 - i * p-1) % n != 0:
        i -= 1
    return max(nb, i*p+1)

S = 0
for j in range(2, 10**7+1):
    S += function_m(j)

# S = 39782849136421
# but took a very long time to be solved ...
