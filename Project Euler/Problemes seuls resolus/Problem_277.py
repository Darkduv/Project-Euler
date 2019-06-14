# %% Problem 277

d = {"D": 0, "U": 1, "d": 2}
sequence = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
l = []


def k_mod_r(bn, cn, n):  # an = bn * k + cn
    b, c = bn % 3, cn % 3
    r = d[sequence[n-1]]
    if b == 0:
        raise Exception
    r2 = (r-c)*b  # b = b^-1 mod 3
    r2 %= 3
    l.append(r2)
    if r == 0:
        bn2, cn2 = bn, (bn*r2+cn) // 3
    elif r == 1:
        bn2, cn2 = bn*4, (4*r2*bn+cn*4+2)//3
    else:
        bn2, cn2 = bn * 2, (2 * r2 * bn + cn * 2 - 1) // 3
    return bn2, cn2


b1, c1 = 1, 0
for i in range(1, len(sequence)+1):
    b1, c1 = k_mod_r(b1, c1, i)

ak, bk = 1, 0
for a in l[::-1]:
    ak *= 3
    bk *= 3
    bk += a

a1 = bk
while a1 <= 10**15:
    a1 += ak
print(a1)  # a1 = 1125977393124310
