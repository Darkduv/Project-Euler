# %% Problem 506

from Tools import bezout


L = [(123432, 0, 0), (123432, 1, 1), (23432, 12, 2), (3432, 123, 3), (432, 1234, 4), (32123432, 0, 0), (123432, 123, 3),
     (432, 12343, 5), (2123432, 123, 3), (432123432, 0, 0), (123432, 1234, 4), (32123432, 123, 3), (432123432, 12, 2),
     (3432123432, 1, 1), (23432123432, 0, 0)]
L_q0_r = [0, 1, 2, 3, 4, 32, 123, 43, 2123, 432, 1234, 32123, 43212, 34321, 23432]

NN = 1000
N, R = int.__divmod__(NN, 15)
mod = 123454321

u, v = bezout(9, mod)  # 1 = 9*v+u*mod
while v < 0:
    v += mod
inv_9 = v

u2, v = bezout(999999, mod)  # 1 = 9*v+u*mod
while v < 0:
    v += mod
inv_9_6 = v


def v(n):
    q, r = int.__divmod__(n, 15)
    a, b, lb = L[r]
    s = b+123432*inv_9_6*(pow(10**6, q-1, mod)-1)*10**lb + pow(10, 6*q-6+lb, mod)*a
    return s % mod


def s_v_15q_r(Q, r):
    a, b, lb = L[r]
    s = L_q0_r[r]
    s += (Q % mod) * (b-1234321*inv_9_6*10**lb)
    s %= mod
    c = pow(10**6, Q, mod) - 1
    c *= inv_9_6
    c %= mod
    c *= (1234321*inv_9_6+b)*10**lb
    c %= mod
    s += c
    s %= mod
    return s

s_tot = 0
# s_tot += 1+2+3+4+32+123+43+2123+432+1234+32123+43212+34321+23432  # sum(v_r) for r in range(15)
for r in range(15):
    s_tot += s_v_15q_r(N-1, r)

"""
s_v_sup_to_NN = 0

for r in range(R+1, 15):
    a, b, lb = L[r]
    s_v_sup_to_NN += a*pow(10**6, N, mod)*10**lb+lb
    s_v_sup_to_NN %= mod

s_tot -= s_v_sup_to_NN
"""
s_tot += sum(v(N*15+r) for r in range(R+1))

s_tot %= mod
print(s_tot)
