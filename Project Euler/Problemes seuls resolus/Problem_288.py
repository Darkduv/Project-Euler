# %% Problem 288
s0 = 290797
p = 61
lt = []
q=10**7
d=10
for _ in range(q+1):
    lt.append(s0%p)
    s0 = s0**2 % 50515093

s_tot = 0
for k in range(1, q-d):
    s_tot += sum(lt[n+k]*p**n for n in range(d))
    s_tot %= p**d
for k in range(q-d, q+1):
    s_tot += sum(lt[n+k]*p**n for n in range(q-k+1))
    s_tot %= p**d
print(s_tot)  # sol = 605857431263981935
