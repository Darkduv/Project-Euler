# %% Problem 697

# We have P(X_n < a) = (a/c)*(sum_{k=0}^{n-1} ln(c/a)^k/k!)

# or see https://en.wikipedia.org/wiki/Incomplete_gamma_function

from math import exp, log
from Tools import dichotomy


s_k_fact = 0
for k in range(1, 10**7-50000):
    s_k_fact += log(k)
ln_fact = {}
for k in range(10**7-50000, 10**7):
    s_k_fact += log(k)
    ln_fact[k] = s_k_fact


def f(log_c):
    llc = log(log_c)
    s = 0
    for n in range(10**7-50000, 10**7):
        s += exp(n*llc - ln_fact[n] - log_c)
    return s


def g(c, p=0.25):
    return f(c)-p


sol = dichotomy(g, 10**7, 10**7*1.001, 0.001)/log(10)
print(f"sol = {sol:.2f}")  # sol = 4343871.06
