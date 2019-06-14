# %% Problem 371


n = 1000
l_prod = [1]
for k in range(1, n+1):
    l_prod.append(l_prod[-1]*k)
s = 999/1000**2
for k in range(2, 501):
    s += k*sum((l_prod[n]*l_prod[k-1])//(l_prod[n-k+i]*l_prod[i]*l_prod[k-i-1]) for i in range(0, k))/n**(k+2)
print(s)