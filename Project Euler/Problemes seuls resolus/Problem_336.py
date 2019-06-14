# %% Problem 336


def nb(l):
    nb_move = 0
    for k in range(len(l)):
        i = l.index(k)
        if i == k:
            continue
        else:
            if i != len(l)-1:
                l[i:] = l[:i-1:-1]
                if k != 0:
                    l[k:] = l[:k-1:-1]
                else:
                    l = l[::-1]
                nb_move += 2
            else:
                return False or (k == len(l)-2 and nb_move == len(l)*2 - 4)
    return nb_move == len(l)*2 - 3


def more(a):
    a = [0]+[i+1 for i in a]
    a.reverse()
    l = [a[:i]+a[i:][::-1] for i in range(1, len(a)-1)]
    return l


lk = [[], [], [], [[1, 0, 2]]] + [[] for _ in range(9)]
for k in range(4, 12):
    for b in lk[k-1]:
        lk[k].extend(more(b))

l11 = lk[11]
l11.sort()
print("".join(["ABCDEFGHIJKLMNO"[i] for i in l11[2010]]))  # sol = CAGBIHEFJDK
