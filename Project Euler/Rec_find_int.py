import numpy as np
from fractions import Fraction


def det(m):
    n = len(m)
    if n == 1:
        return m[0, 0]
    else:
        l = []
        for i in range(n):
            l.append([m[i, j] for j in range(1, n)])
        a = 0
        for i in range(n):
            a += (-1)**i*m[i, 0]*det(np.matrix([l[j] for j in range(n) if j != i]))
        return a


def minor(i, j, m):
    mm = []
    n = len(m)
    for k in range(n):
        mmk = []
        if k == i:
            continue
        for l in range(n):
            if l == j:
                continue
            mmk.append(m[k, l])
        mm.append(mmk)
    return det(np.matrix(mm))


def co_matrix(m):
    if det(m) == 0:
        raise ValueError("non bij matrix")
    mm = []
    n = len(m)
    for i in range(n):
        mmi = []
        for j in range(n):
            mmi.append(minor(i, j, m)*(-1)**(i+j))
        mm.append(mmi)
    return np.matrix(mm)


def in_rational(m):
    n = len(m)
    mm = m.copy()
    for i in range(n):
        for j in range(n):
            mm[i, j] = Fraction(mm[i, j])
    return mm


def print_matrix(m):
    print("[", end='')
    n, n2 = m.shape
    for i in range(n):
        print("[", end='')
        for j in range(n2):
            print(str(m[i, j]), end='')
            if j != n2-1:
                print(", ", end='')
            elif i != n-1:
                print("]")
            else:
                print("]]")


def mat1_2(l, n):
    l2 = []
    for i in range(n+1):
        l2.append(l[i:i+n])
    return np.matrix(l2[:-1]), np.matrix(l2[1:])


def rec_lin(l):
    n = 1
    m1, m2 = mat1_2(l, n)
    while det(m1) != 0 and n < 100 and 2 * (n+1) + 1 < len(l):
        n += 1
        m1, m2 = mat1_2(l, n)
    if 2 * (n+1) + 1 < len(l):
        print("list too small")
    if det(m1) == 0:
        if n == 1:
            print('please give a list beginning by a non zero value')
            return
        try:
            m1, m2 = mat1_2(l, n-1)
            m3 = (in_rational(co_matrix(m1).transpose())/Fraction(det(m1)))*m2
            return m3[:, -1]
        except np.linalg.linalg.LinAlgError:
            print("float problem ?")
            print("n= ", n)
    else:
        m3 = (in_rational(co_matrix(m1).transpose())/Fraction(det(m1)))*m2
        print("m3[0] = ", [m3[0, i] for i in range(n)], "  and  m3[-1] = ", [m3[-1, i] for i in range(n)])
        print("m3[i+1, i]= [", end='')
        for i in range(1, n-2):
            print(m3[i+1, i], end='')
            print(', ', end='')
        print(m3[n-2, n-1], ']\n', sep='')
        print("n=", n)
        ok = input("print(m3) ?  1 or 0 ?\n")
        if ok:
            print_matrix(m3)

# Example:

if __name__ == "__main__":

    L = [2, 5, 21, 42, 152, 296, 1050, 2037, 7205, 13970, 49392, 95760, 338546, 656357, 2320437, 4498746, 15904520,
         30834872, 109011210, 211345365, 747173957, 1448582690, 5121206496, 9928733472, 35101271522, 68052551621,
         240587694165, 466439127882, 1649012587640, 3197021343560]

    print_matrix(rec_lin(L))
