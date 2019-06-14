# %% Problem 142

dd = {}
for a in range(1, 1000):
    for b in range(a+2, 1000, 2):
        x = (a**2 + b**2) // 2
        dd[x] = dd.get(x, []) + [(a, b)]
l = list(dd.keys())
l.sort()
end = False
for x in l:
    if len(dd[x]) == 1:
        pass
    for i in range(len(dd[x])):
        for j in range(i+1, len(dd[x])):
            a, b = dd[x][i]
            c, d = dd[x][j]
            y = (b**2-a**2)//2
            z = (d**2-c**2)//2
            if int((y-z)**0.5)**2 == y-z and int((y+z)**0.5)**2 == y+z:
                end = True
                print(x+y+z)
                break
    if end:
        break

# sol = 1006193
