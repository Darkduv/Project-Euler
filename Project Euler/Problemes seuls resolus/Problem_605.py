# %% Problem 605

# we have Pn(k) = 2^(n-k)*((k-1)*(2^n-1) + n) / (2^n - 1)^2 = pn/qn
# and the gcd(pn, qn) divide n and (k-1)*(2^n-1)
# it appears here that n is prime, k-1 < n and 2^n - 1 = 1 mod n so gcd(pn, qn)=1

mod = 10**8
n = mod + 7
k = 10**4 + 7
pn = pow(2, n-k, mod)
pn *= (pow(2, n, mod)-1)*(k-1)+n
pn %= mod
qn = pow(2, n, mod) - 1
qn *= qn
qn %= mod

print((pn*qn) % mod)  # sol = 59992576 ?? (solved, but this solution has not been verified)
