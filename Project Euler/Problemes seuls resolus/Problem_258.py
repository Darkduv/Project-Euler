# %% Problem 258

import numpy as np

mod = 20092010
N = 2000
class Polynomial:
    def __init__(self, list_, n):
        self.coefficient = np.zeros((n,), dtype=int)
        self.coefficient[:len(list_)] = list_
        self.taille = n

    def __getitem__(self, item):
        return self.coefficient[item]

    def __add__(self, other):
        return Polynomial((self.coefficient + other.coefficient)% mod, self.taille)

    def __sub__(self, other):
        return Polynomial((self.coefficient - other.coefficient) % mod, self.taille)

    def __mod__(self, m):
        return Polynomial(self.coefficient % m, self.taille)

    def __mul__(self, other):
        n = self.taille
        if self.taille == 1:
            return Polynomial([(self[0]*other[0])%mod], 1)
        else:
            A0 = self.coefficient[:n//2]
            A1 = self.coefficient[n//2:]

            B0 = other.coefficient[:n//2]
            B1 = other.coefficient[n//2:]
            A0 = Polynomial(A0, n//2)
            A1 = Polynomial(A1, n // 2)
            B0 = Polynomial(B0, n // 2)
            B1 = Polynomial(B1, n // 2)
            T0 = A0*B0
            T1 = A1*B1
            T2 = (A0+A1)*(B0+B1)
            tab = np.zeros((2*n,), dtype=int)
            tab[:T0.taille] += T0.coefficient
            tamp = np.zeros((n,), dtype=int)
            tamp[:T2.taille] += T2.coefficient
            tamp[:T1.taille] -= T1.coefficient
            tamp[:T0.taille] -= T0.coefficient
            tab[n//2:n+n//2] += tamp
            tab[n:n+T1.taille] += T1.coefficient
            return Polynomial(tab % mod, 2*n)

    def prune(self):
        if self.taille > 2*N -1:
            self.coefficient[:N-1] += self.coefficient[N:2*N-1]
            self.coefficient[1:N] += self.coefficient[N:2*N-1]
            tamp = self.coefficient[:N] % mod
            self.coefficient = np.zeros((2048,), dtype=int)
            self.coefficient[:N] = tamp
            self.taille = 2048
        elif self.taille > N:
            n = self.taille - N
            self.coefficient[:n] += self.coefficient[N:N+n]
            self.coefficient[1:n+1] += self.coefficient[N:N+n]
            self.coefficient[N:N+n] = np.zeros((n,), dtype=int)
            self.coefficient %= mod


P = Polynomial([1, 1], 2048)  # P(A) = A^2000 = A+1

n = (10**18)//2000
x = P
z = Polynomial([1], 2048)
y = x
while n != 0:
    if n % 2 == 1:
        z *= y
        z.prune()
    n //= 2
    y *= y
    y.prune()
    print(n)

def fois_l(M, n):
    ML = np.zeros((n, n), dtype=int)
    ML[:, 1:] = M[:, :-1]
    ML[:, 0] = M[:, -1]
    ML[:, 1] = (ML[:,1] + M[:,-1]) % mod
    return ML

n = 2000
L = np.zeros((n, n), dtype=int)
L[0:-1,1:] = np.eye(n-1, dtype=int)
L[n-1,0:2] = [1, 1]
Lk = []
Lk.append(np.eye(n, dtype=int))
for k in range(1, 2000):
    Lk.append(fois_l(Lk[-1], n)%mod)

A = np.zeros((n, n), dtype=int)
for k in range(2000):
    A += z[k] * Lk[k]
    A %= mod

aa = np.dot(A, np.ones((n,), dtype=int))
print(aa[0]%mod)  # sol = 12747994