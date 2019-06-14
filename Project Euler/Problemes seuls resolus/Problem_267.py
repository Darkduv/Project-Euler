# %% Problem 267


# if f allows the player to get more than £1,000,000,000, then it exists d such that
#  g(f, d) = (1+2f)^d*(1-f)^(1000-d) > 10**9
# and we can see that f |-> g(f, d) for a given d have its max in f = (3d-1000)/2000


def g(dd):
    p, q = 3*dd-1000, 2000  # f_max = p/q
    return ((q+2*p)**dd*(q-p)**(1000-dd)) // q**1000

d = 334
while g(d) < 10**9:
    d += 1


s = 0
a = 1
for i in range(d):
    s += a
    a *= (10**3-i)
    a //= i + 1
s = 2**10**3 - s

print('{:.12f}'.format(s/2**(10**3)))  # sol = 0.999992836187
