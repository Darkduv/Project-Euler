# %% Problem 431
from math import pi, cos, sin, sqrt, tan
from Tools import dichotomy


def int_simpson(f, a, b, n):
    h = (b-a)/n
    s = (f(a)+f(b))/6 + 2/3*(f(a+h/2))
    x = a+h
    for i in range(n-1):
        s += f(x)/3
        s += 2/3*f(x+h/2)
        x += h
    return s*h


def function1(theta, x, r):
    a = r**2-x**2*sin(theta)**2
    return 3*x**2*cos(theta)**2*sqrt(a)+a*sqrt(a)


def function2(x, r=3, alpha=30):
    return 4/3*int_simpson(lambda theta: function1(theta, x, r), a=0, b=pi / 2, n=10**3)*tan(alpha/180*pi)


def solve(r=3, alpha=30):
    a = int(function2(0, r, alpha)**0.5+1)
    b = int(function2(r, r, alpha)**0.5)
    l = []
    for i in range(a, b+1):
        l.append(dichotomy(lambda x: function2(x, r, alpha)-i**2, 0, r, 10**10))
    return l


def problem():
    return round(sum(x for x in solve(6, 40)), 9)

# sol = 23.386029052 ???
