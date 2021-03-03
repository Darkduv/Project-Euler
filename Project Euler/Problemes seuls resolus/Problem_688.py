from math import sqrt


def i_k(N, k):
    return (N-(k*(k-1))//2)//k


def s_ik(N, k):
    ik = i_k(N, k)
    return k*((ik-1)*ik)//2 + ik*(N-(k*(k-1+2*ik))//2)+ik


N=10**16
k_max = int((-1+sqrt(1+8*N))/2)
s = 0
for k in range(1, k_max+1):
    s += s_ik(N, k)
    s %= 1000000007
print(s)

# sol=110941813
