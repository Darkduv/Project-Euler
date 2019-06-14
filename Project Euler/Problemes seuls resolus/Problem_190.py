# %% Problem 190

# p = x1^*x2^ ...
# so p max when log(p) max, that is sum(k*log(xk)) = S
# when this sum is max, his gradient == 0
# and with x1 = m - x2 - ... we have dS/d xk = k/xk - 1/x1
# so xk have to be k*x1 so m = x1*sum(k for k in range(1, m+1))


def p_max(m):
    x = 2/(m+1)
    p = 1
    for k in range(1, m+1):
        p *= (x*k)**k
    return int(p)

print(sum(p_max(i) for i in range(2, 16)))
