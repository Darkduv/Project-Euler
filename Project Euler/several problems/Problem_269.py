def f_m(M, n):
    s_tot = set()
    d = len(M)
    s_i = [set() for _ in range(d)]
    s_i[0].add("0")
    for i in range(1, d):
        a = M[i][0]
        if a is not None:
            s_i[i].add(a)
    for k in range(n-1):
        s_i2 = [set() for _ in range(d)]
        for i in range(d):
            for j in range(d):
                for mm in s_i[j]:
                    if M[i][j]is not None:
                        s_i2[i].add(mm+M[i][j])
        s_tot.update(s_i2[0])
        s_i = s_i2
    s_tot2 = set(int(a) for a in s_tot)
    return s_tot2


len_matrix = [0, 20, 8, 5, 3, 2, 2, 2, 2, 2]


def matrix(a):
    lm = len_matrix[a]
    M = [[None] * lm for _ in range(lm)]
    for r in range(lm):
        r2 = r
        if a == 3:
            if r >= lm-1:
                r2 -= lm
        elif a == 2:
            if r >= lm-2:
                r2 -= lm
        elif a == 1:
            if r >= lm-10:
                r2 -= lm
        for a0 in range(r2 % a, 10, a):
            M[r2][(a0-r2)//a] = str(a0)
    return M


def poly(a):
    def aux(x):
        s = 0
        for c in str(a):
            s *= x
            s += int(c)
        return s
    return aux


def verify(a):
    for b in range(10, 20):
        if a % b == 0:
            bb = 10 - b
            if poly(a)(bb) == 0:
                return True
    return False


def f(n):
    s_final = {str(i*10) for i in range(1, 10**(n-1))}
    for a in range(1, 10):
        s_final.update(f_m(matrix(a), n))
    s_f2 = set(int(a) for a in s_final if verify(int(a)))
    return len(s_f2)

"""
if b root of poly(a) : 
-> (a%10)%b = 0
-> a%(10-b) = 0
-> (sum digit a)%(1-b) = 0 
"""