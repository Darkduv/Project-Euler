# %% Problem 185

from itertools import combinations
n = 16

list_nb = """5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct"""


l = list_nb.split("\n")
l = [[a[:n], a[n+2]] for a in l]
l = [[int(a), int(b)] for a, b in l]


def f(a, b, li):
    a, b = str(a), str(b)
    b2 = ""
    for j in range(n):
        ai, bi = a[j], b[j]
        if j in li:
            if ai == bi:
                b2 += bi
            else:
                b2 += "-"
        else:
            if ai != bi:
                b2 += bi
            else:
                b2 += "-"
        j += 1
    return b2


def f2(a, b, li):
    a, b = str(a), str(b)
    b2 = ""
    for j in range(n):
        ai, bi = a[j], b[j]
        if j in li:
            if ai == bi:
                b2 += "X"
            else:
                b2 += "-"
        else:
            if ai != bi:
                b2 += bi
            else:
                b2 += "-"
        j += 1
    return b2


c = 0
for a, k in l:
    if k == 0:
        c = a
        break

l2 = [[f(c, b, []), k] for b, k in l]


def verify(ll):
    for b, nb in ll:
        if b.count("X") > nb:
            return False
        if b.count("-") > n - nb:
            return False
    return True


def next_(ll):
    i0 = 0
    if not verify(ll):
        return False, []
    while ll[i0][0].count("-") == n - ll[i0][1]:
        cc = ll[i0][0]
        li = [j for j in range(n) if cc[j] != "-"]
        ll = [[f2(cc, b, li), nb] for b, nb in ll]
        i0 += 1
        if i0 >= len(ll):
            return True, ll
    cc, kk = ll[i0]
    end_end, ll_ok = False, []
    for li in combinations(range(n), kk):
        end = False
        for j in li:
            if cc[j] == "-":
                end = True
                break
        if end:
            continue
        ll2 = [[f2(cc, b, li), nb] for b, nb in ll]
        ok_end, ll_ok = next_(ll2)
        if ok_end:
            end_end = True
            break
    return end_end, ll_ok


ok, ll_end = next_(l2)
lok = ["a"]*n
ia = 0
for a, k in ll_end:
    for i in range(n):
        if a[i] != '-':
            lok[i] = l2[ia][0][i]
    ia += 1
for i in range(n):
    if lok[i] == "a":
        l_able = set("0123456789")
        for a, k in l:
            char = str(a)[i]
            if char in l_able:
                l_able.remove(char)
        lok[i] = l_able.pop()

s = "".join(lok)
print(int(s))  # 4640261571849533
