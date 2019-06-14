# %% Problem_159

L = [n % 9 if n % 9 != 0 else 9 for n in range(10**6)]
for a in range(2, 10**6):
    for b in range(2, 10**6):
        if a * b >= 10**6:
            break
        L[a*b] = max(L[a*b], L[a]+L[b])

print(sum(L)-10)  # sol = 14489159
