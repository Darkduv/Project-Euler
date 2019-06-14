from math import sin, asin, tan, sqrt, cos, pi

d = (100-10*sqrt(2)*5)/2  # the distance between A and the marsh on the (AB) line.


def f(i):
    i1 = i
    i2 = asin(9/10*sin(i1))
    i3 = asin(8/9 * sin(i2))
    i4 = asin(7/8 * sin(i3))
    i5 = asin(6/7 * sin(i4))
    i6 = asin(5/6 * sin(i5))
    i7 = asin(10/5*sin(i6))

    l1 = tan(i1)*d/sqrt(2) - d/sqrt(2)
    l2 = l1 - 10 + 10*tan(i2)
    l3 = l2 - 10 + 10*tan(i3)
    l4 = l3 - 10 + 10*tan(i4)
    l5 = l4 - 10 + 10*tan(i5)
    l6 = l5 - 10 + 10*tan(i6)
    ok = (d/sqrt(2) - l6) - d/sqrt(2)*tan(i7)

    t = d/sqrt(2)/cos(i1)/10
    t += 10/cos(i2)/9
    t += 10/cos(i3)/8
    t += 10/cos(i4)/7
    t += 10/cos(i5)/6
    t += 10/cos(i6)/5
    t += sqrt(1/2*l6**2+(-l6/sqrt(2)+d)**2)/10
    return ok, t


def dichotomy(g, a: float, b: float, eps):
    assert g(a)[0]*g(b)[0] <= 0
    while b-a > eps:
        m = (b+a)/2
        if g(a)[0]*g(m)[0] >= 0:
            a = m
        else:
            b = m
    return (a+b)/2

i0 = dichotomy(f, pi/4, pi/3, 10**-6)
print('{:.10f}'.format(f(i0)[1]))
