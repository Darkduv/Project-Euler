# %% Problem 256

from math import ceil


def free(m, n):  # return if a m*n room is a fre-tatami room
    if m > n:
        return free(n, m)
    if m % 2 == 1 and n % 2 == 1:
        return True
    if m in [1, 2, 3]:
        return False
    if m % 2 == 0:
        for a_m in [0, 1, m-2, m-1, m, m+1]:
            if a_m > n:
                break
            b_m = ceil((n - a_m) / (m + 1))
            c_m = (n - a_m) // (m - 1)
            if b_m == c_m:
                if ((n-a_m) - (m-1)*b_m) % 2 == 0:
                    return False
            if b_m < c_m:
                return False
        return True
    else:
        for a_m in [0, m-1, m+1]:
            if a_m > n:
                break
            if (n-a_m) % 2 != 0:
                continue
            b_m = ceil((n - a_m) / (m + 1))
            c_m = (n - a_m) // (m - 1)
            if b_m <= c_m:
                return False
        return True


def nb_free(aa, bb, cc, dd, ee, ff, gg):
    area = 2 ** aa * 3 ** bb * 5 ** cc * 7 ** dd * 11 ** ee * 13 ** ff * 17 ** gg
    nb = 0
    for ii in range(aa+1):
        for jj in range(bb+1):
            for kk in range(cc+1):
                for ll in range(dd+1):
                    for mm in range(ee+1):
                        for nn in range(ff+1):
                            for oo in range(gg+1):
                                side = 2**ii*3**jj*5**kk*7**ll*11**mm*13**nn*17**oo
                                if side ** 2 > area:
                                    break
                                if free(side, area//side):
                                    nb += 1
    return nb


mini = 10**9
for a in range(1, 10):
    p = 2 ** a
    if p >= mini:
        break
    for b in range(0, a + 5):
        p2 = p * 3 ** b
        if p2 >= mini:
            break
        for c in range(0, b + 5):
            p3 = p2 * 5 ** c
            if p3 >= mini:
                break
            for d in range(0, c + 5):
                p4 = p3 * 7 ** d
                if p4 >= mini:
                    break
                for e in range(0, d + 5):
                    p5 = p4 * 11 ** e
                    if p5 >= mini:
                        break
                    for f in range(0, e + 5):
                        p6 = p5 * 13 ** f
                        if p6 >= mini:
                            break
                        for g in range(0, f + 5):
                            p7 = p6 * 17 ** g
                            if p7 >= mini:
                                continue
                            if (a + 1) * (b + 1) * (c + 1) * (d + 1) * (e + 1) * (f + 1) * (g + 1) < 400:
                                continue
                            if nb_free(a, b, c, d, e, f, g) == 200:
                                mini = p7
print(mini)  # sol = 85765680
