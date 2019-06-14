# %% Problem 230
from Tools import binary_search_inf

A = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
# A = '1415926535'
# B = '8979323846'

f = [0, 1, 1]
for _ in range(75):
    f.append(f[-1]+f[-2])

k0 = len(A)


def d(i):
    if i <= k0:
        return int(A[i-1])
    elif i <= 2*k0:
        return int(B[i - 1 - k0])
    i0 = binary_search_inf(f, i/k0)
    k = i0-2
    i -= k0*f[i0-1]
    while i > k0:
        if i < k0*f[k]:
            k -= 2
        else:
            i -= k0*f[k]
            k -= 1
    return int([A, B][(k + 1) % 2][i - 1])


print(sum(10**n*d((127+19*n)*7**n) for n in range(18)))  # 850481152593119296
