# %% Problem 323


lj = [0, 0.5]
for k in range(2, 100):
    lj.append((lj[-1]+1)/2)

N = 0
for k in range(1, 50):
    N += k*(lj[k]**32 - lj[k-1]**32)
print(N)
