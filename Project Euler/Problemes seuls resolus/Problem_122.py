# %% Problem 122

lm = [k for k in range(201)]
lm[1], lm[2] = 0, 1


def after(l, maxi=200):
    l_ok = []
    for i in range(len(l)):
        for j in range(len(l)-1, i-1, -1):
            a = l[i]
            b = l[j]
            if a+b <= l[-1]:
                break
            if a+b > maxi or a+b in l_ok:
                continue
            l_ok.append(a+b)
            if lm[a+b] > len(l):
                lm[a+b] = len(l)
            yield l + [a+b]
l0 = [1, 2]
for l1 in after(l0):
    for l2 in after(l1):
        for l3 in after(l2):
            for l4 in after(l3):
                for l5 in after(l4):
                    for l6 in after(l5):
                        for l7 in after(l6):
                            for l8 in after(l7):
                                for l9 in after(l8):
                                    for l10 in after(l9):
                                        after(l10)

print(sum(lm))
