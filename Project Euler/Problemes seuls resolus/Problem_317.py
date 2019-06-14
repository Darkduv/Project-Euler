# %% Problem 317

# we can find that V = pi*v0^2/g *(h+1/2*v0^2/g)^2

from math import pi
v0 = 20
g = 9.81
h = 100
a = v0**2/g
print(pi*a*(h+a/2)**2)  # sol = 1856532.8455
