from time import time


def iterator(n):
    s = 290797
    for i in range(1, n+1):
        s = (s**2) % 50515093
        yield s

"""
A = []
N = 10000
M = 0

t = time()
count = 0
for s in iterator(N):
    d = dict()
    for l in A:
        m, nb = l
        mm = min(m, s)
        M += (mm * nb)
        # l[0] = m
        if mm in d:
            d[mm] += nb
        else:
            d[mm] = nb
    M += s
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
    A = [[a, d[a]] for a in d]
    if count % 10000000 == 0:
        pass
        #print(count, time()-t)
    count += 1

print(M)
print(time()-t)
"""
N = 2000000000
M = 0
A = dict()
t = time()
count = 0
for s in iterator(N):
    l = list(A.keys())
    for m in l:
        nb = A[m]
        if m <= s:
            M += (m * nb)
        else:
            M += s * nb
            if s in A:
                A[s] += nb
            else:
                A[s] = nb
            A.pop(m)
    M += s
    if s in A:
        A[s] += 1
    else:
        A[s] = 1
    if count % 10000000 == 0:
        print(count//10000000, "  ", time()-t)
    count += 1
print(M)
print(time()-t)