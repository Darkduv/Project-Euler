# %% Problem 141

from Tools import is_square


s = set()
for b in range(1, 10**6):
    for p in range(1, 10**6):
        if p**2*b >= 10**6:
            break
        a = p+1
        c = a**3*b**2*p + p**2*b
        while c <= 10**12:
            if is_square(c):
                s.add(c)
            a += 1
            c = a ** 3 * b ** 2 * p + p ** 2 * b

print(sum(s))  # sol = 878454337159
# Todo: Too long ?
