# %% Problem 245


# C(n) can not be an unit fraction if n = p^k * a with k > 1 and p prime

from Tools import is_prime, phi, decompose_tout


def unit_co_resilience(n):
    return (n-1) % (n-phi(n)) == 0

s = 0
for i in range(2, 2*10**11+1):
    if not is_prime(i):
        if unit_co_resilience(i):
            s += i
            l = [b for a, b in decompose_tout(i)]
            if l.count(1) != len(l):
                print(i)
