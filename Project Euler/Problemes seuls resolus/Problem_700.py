A = 1504170715041707
M = 4503599627370517

i = 1
k = 2
s = A


def g(n):
    return (n*A) % M


while i+k < M:
    if g(i)+g(k) > M:
        i += k
        s += g(i)
    else:
        k += i

print(s)  # sol = 1517926517777556
