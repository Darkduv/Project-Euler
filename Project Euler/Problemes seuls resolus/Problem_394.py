# %% Problem 394

from math import log

"""see mathematical E, probability, ... and a very long demonstration"""


def f(x):
    return 7/9+2/9*x**-3+2/3*log(x)


print(round(f(40), 10))  # sol = 3.2370342194
