from Tools import numpy_sieve, binary_search_inf


def eratosthene_crazy(n):
    l = [0]*(n//2)
    for i in range(len(l)):
        if l[i] == 0:
            l[i] = 2*i + 3
        p = 2*i + 3
        if p**2 > n:
            return l
        i0 = 2*i**2 + 6*i + 3
        for k in range(i0, len(l), p):
            if l[k] == 0:
                l[k] = p
    return l

l_p = eratosthene_crazy(10**6*50)


def lpd(n):  # the least prime divisor
    return l_p[(n-3)//2]


def ok_aux(p, n):
    return 3*n < p**2


def ok(n):  # is it n == 4P or 16P or P where P prime ?
    if n % 32 == 0:
        return False
    elif n % 16 == 0:
        k = n // 16
        p = lpd(k)
        if p == 0 or p == k:
            return True
        return ok_aux(p, k)
    elif n % 8 == 0:
        return False
    elif n % 4 == 0:
        k = n // 4
        p = lpd(k)
        if p == 0 or p == k:
            return True
        return ok_aux(p, k)
    elif n % 4 == 3:
        k = n
        p = lpd(k)
        if p == 0 or p == k:
            return True
        return ok_aux(p, k)
    else:
        return False


def number(n):
    nb = 0
    for i in range(n):
        if ok(i):
            nb += 1
    return nb

print("Problem 136: ", number(10**6*50))

# the 'good' n's are n == 4P or 16P or P where P prime and n == 4*1 and n == 16*1
# so :
maxi = 10**6*50
l_pp = numpy_sieve(maxi)
tot = 0
for a in l_pp:
    if a % 4 == 3:
        tot += 1
tot += binary_search_inf(l_pp, maxi//4) + 1
tot += binary_search_inf(l_pp, maxi//16) + 1
print(tot)
