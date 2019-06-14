from math import log10


s = set()
for a in range(2, 7):
    for b in range(a, 40//a+1):
        c = int(10**(log10(10**12)/(a*b)))+1
        if c <= 2:
            break
        for k in range(2, c):
            if k**(a*b) <= 10**12:
                s.add(k**(a*b))
            else:
                break

for b in range(2, 10**3+1):
    for c in range(b, 10**6//b+1):
        d = int(log10(10**12)/log10(b*c))+1
        if d <= 2:
            break
        for k in range(2, d):
            if (b*c)**k <= 10 ** 12:
                s.add((b*c)**k)
            else:
                break

s.remove(16)
print(sum(s))  # 310884668312456458
