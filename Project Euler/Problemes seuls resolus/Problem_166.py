# %% Problem 166


L = [[] for _ in range(28)]
for a in range(10):
    for b in range(10):
        for c in range(10):
            L[a+b+c].append([a, b, c])


L_3 = []
nb1 = 0
nb2 = 0
for n in range(19):
    if n == 18:
        nb1 *= 2
        nb2 *= 2
    for m in range(max(n-9, 0), n+1):
        for l1 in L[m]:
            for mm in range(max(n-9, 0), n+1):
                for l2 in L[mm]:
                    if l2[0] > l1[1]:
                        continue
                    end = False
                    for i in range(3):
                        if l1[i] + l2[i] > n or l1[i] + l2[i] < n - 18:
                            end = True
                            break
                    if end:
                        continue
                    if l1[0] + l2[1] > n or l1[0] + l2[1] < n - 18:
                        continue
                    if l2[2] > n or l2[2] < n - 27:
                        continue
                    for mmm in range(max(n - 9, 0), n + 1):
                        for l3 in L[mmm]:
                            end = False
                            for i in range(3):
                                if l1[i] + l2[i] + l3[i] > n or l1[i] + l2[i] + l3[i] < n - 9:
                                    end = True
                                    break
                            if end:
                                continue
                            if l1[0] + l2[1] + l3[2] > n or l1[0] + l2[1] + l3[2] < n - 9:
                                continue
                            if l2[2] + l3[1] > n or l2[2] + l3[1] < n - 18:
                                continue
                            if 2*l1[0] + l1[1] + l1[2] + l2[0] - l2[2] + l3[0] - l3[1] != n:
                                continue
                            if sum(l1) + sum(l2) + sum(l3) + sum([l1, l2, l3][i][i] for i in range(3)) != 3*n:
                                continue
                            if l2[0] < l1[1]:
                                nb1 += 2
                            else:
                                nb2 += 1
print(nb1+nb2)

# 7130034  (put a long time to run :-(   )
