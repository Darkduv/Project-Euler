# %% Problem 491


nb_tot = [[[[0]*10] for _ in range(11)] for k in range(11)]  # there was [] instead of [[0]*10] but the inspector found
# a type's problem next ( in the extend([l+[a] ..     )

for n in range(0, 11):
    if n <= 2:
        nb_tot[n][1] = [[n]]
    for nb in range(2, 11):
        if nb*2 < n:
            continue
        for a in [0, 1, 2]:
            if n - a < 0:
                break
            nb_tot[n][nb].extend([l + [a] for l in nb_tot[n-a][nb-1]])

l = nb_tot[10][10]
l2 = [a for a in l if (sum(a[i]*i for i in range(10))*2+9) % 11 == 0]


def opposite(prop):
    return [2-i for i in prop]

fact8 = 8*7*6*5*4*3*2*1
fact9 = 9*fact8
fact10 = 10*fact9

N = 0
for a in l2:
    double = a.count(2)
    if a[0] == 0:
        n1 = fact10 // (2**double)
    elif a[0] == 1:
        n1 = 9*fact9//(2**double)
    else:
        n1 = 9*8*fact8 // (2**double)

    N += n1 * fact10//(2**(opposite(a).count(2)))
print(N)  # 194505988824000
