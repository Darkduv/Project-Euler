# %% Problem 147

L = [[0]*48, [0]+list(range(48))]
for a in range(2, 44):
    ll = [0, a-1]
    for b in range(2, 48):
        e = L[a-1][b]*2-L[a-2][b]+2*(ll[b-1]+L[a-2][b-1]-2*L[a-1][b-1])-ll[b-2]-L[a-2][b-2]+2*L[a-1][b-2]
        if a == b:
            e += 6*(a-1)-1
        elif a == b+1:
            e += (a-1)
        elif a+1 == b:
            e += (b-1)
        ll.append(e)
    L.append(ll)

A, B = 47, 43
s = 0
for a in range(1, A+1):
    for b in range(1, B+1):
        s += (a+1)*a*b*(b+1)
s //= 4
s += sum(sum(a[:A+1]) for a in L[:B+1])
print(s)  # sol = 846910284
