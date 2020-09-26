from math import log2


def s2(n):
    return sum(int(a) for a in bin(n)[2:])


def decompose(n):
    a = int(log2(n))
    k = n - 2**a + 1
    return a, k


def solve(n):
    a, k = decompose(n)
    return (a-1)*(k+1)+4 + 4*(a-3)*2**(a-2) + s2(k)


print(f"solve(10**7) = {solve(10**7)}")
print(f"sol = solve(10**16) = {solve(10**16)}")  # sol = 501985601490518144
