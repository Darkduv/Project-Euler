# %% Problem 151

d = {}


def cut(n):
    return list(range(n-1, 0, -1))


def pick(ll):
    if ll == (1,):
        return 1
    a = 0
    for i in range(len(ll)):
        l2 = list(ll[:i]) + list(ll[i + 1:]) + cut(ll[i])
        l2.sort()
        c = tuple(l2)
        if c in d:
            a += d[c]
        else:
            s = pick(c)
            d[c] = s
            a += s
    a /= len(ll)
    a += 1 if len(ll) == 1 else 0
    return a


s_tot = pick((5,))
print("{:6f}".format(s_tot-2))