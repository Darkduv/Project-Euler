# %% Problem 250

s = [pow(i, i, 250) for i in range(1, 250250+1)]
d = {}
for i in range(len(s)):
    a = s[i]
    d2 = {a: 1}
    for b in d:
        c = (a+b) % 250
        d2[c] = (d2.get(c, 0)+d[b]) % 10**16
    for a in d2:
        d[a] = (d2[a]+d.get(a, 0)) % 10**16

print(d[0])  # sol = 1425480602091519
