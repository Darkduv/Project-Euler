def s(q, t, m):
    ss = -9*q-6-t
    ss += (t+6+(t*(t+1))//2)*pow(10, q, m)
    return ss % m


a, b = 1, 0
sol = 0
mod = 1000000007
for _ in range(2, 91):
    a, b = a+b, a
    sol += s(a // 9, a % 9, mod)
    sol %= mod
print(sol)
# sol = 922058210
