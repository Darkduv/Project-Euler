# %% Problem 225


def problem_225():
    def ok(nn):
        a, b, c = 1, 1, 1
        while a % nn != 0:
            a, b, c = b, c, (a+b+c) % nn
            if a == b and b == c:
                return a != 0
        return False
    nb = 0
    n = 1
    while nb < 124:
        n += 2
        if ok(n):
            nb += 1
    print(n)
# Todo : doesn't worth its difficulty of 45%
