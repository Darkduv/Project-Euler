p = 10**6

# M(n) = n+ek-(e+1)s
# so   n fixed point => ek = (e+1)s
# and if ek = (e+1)s then the fixed points are ]m-e(k-s) ; m - (e-1)(k-s)]

s = 0
for e in range(1, p+1):
    d = int(p/(e+1))
    s += 3*(1+2*p)*d*(d+1) + (1-2*e)*d*(d+1)*(2*d+1)

s //= 12
print(s)  # sol = 208517717451208352
