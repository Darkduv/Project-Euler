s = 30
a = 15 + 13
b = 8 + 7
pb = 8
pa = 13
n = 23416728348467685
while pa < n:
    s += a
    a, b = a + b + pb, a
    pa, pb = pa + pb, pa

s += pa
# sol = 842043391019219959
