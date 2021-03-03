# %% Problem 168
from Tools import gcd

s = 0
for d in range(2, 10):
    for a in range(d, 10):
        q = 10*d-1
        qq = q // gcd(q, a)
        ll = []
        prod = 10
        for n in range(2, 101):
            if prod == d:
                ll.append(n)
            prod *= 10
            prod %= qq
        for n in ll:
            b = ((10**(n-1)-d)//qq)*(a//gcd(q, a))
            nb = int(str(b)+str(a))
            s += int(nb)%10**5
            s %= 10**5

s += 45*(11+111+1111+11111*96)
s %= 10**5

print(s)  # 59206
