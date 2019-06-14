import numpy as np


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


def mat1_2(l, n):
    l2 = []
    for i in range(n+1):
        l2.append(l[i:i+n])
    return np.matrix(l2[:-1]), np.matrix(l2[1:])


def rec_lin(l):
    n = 1
    m1, m2 = mat1_2(l, n)
    while abs(det(m1)) >= 10**-12 and n < 100 and 2*(n+1) + 1 < len(l):
        n += 1
        m1, m2 = mat1_2(l, n)

    # problem of odrder of if elif ?
    if abs(det(m1)) < 10**-12:
        try:
            m1, m2 = mat1_2(l, n-1)
            m3 = (m1**-1)*m2
            return [m3[i, -1] for i in range(n-1)]
        except np.linalg.linalg.LinAlgError:
            print("float problem ?")
            print("n= ", n)
    elif 2 * (n+1) + 1 < len(l):
        print("list too small")
    else:
        m3 = (m1 ** -1) * m2
        print("m3[0] = ", [m3[0, i] for i in range(n)], "  and  m3[-1] = ", [m3[-1, i] for i in range(n)])
        print("n=", n)
        ok = input("print(m3) ?  1 or 0 ?\n")
        if ok:
            print(m3)

# Example:

if __name__ == "__main__":

    L = [2, 5, 21, 42, 152, 296, 1050, 2037, 7205, 13970, 49392, 95760, 338546, 656357, 2320437, 4498746, 15904520,
         30834872, 109011210, 211345365, 747173957, 1448582690, 5121206496, 9928733472, 35101271522, 68052551621,
         240587694165, 466439127882, 1649012587640, 3197021343560]

    print(rec_lin(L))
