# %% Problem 479


def sp(k, n):  # cf calculate for the explanation of the formule.
    # we can already see that (ak+bk)(bk+ck)(ck+ak) = -(k-1)*(k+1)
    return ((pow(k-1, n+1, mod*k**2)*pow(k+1, n+1, mod*k**2)*(-1)**n - (k-1)*(k+1))//(k**2)) % mod


N = 10**6
mod = 10**9+7
s = 0
for k in range(1, N+1):
    s += sp(k, N)
    s %= mod
print(s)  # sol = 191541795
