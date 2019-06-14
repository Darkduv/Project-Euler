# %% Problem 163

# https://oeis.org/A210687


def t(n=36):
    return (1678 * n ** 3 + 3117 * n ** 2 + 88 * n - n % 2 * 345 - n % 3 * 320 - n % 4 * 90 - (
                n ** 3 - n ** 2 + n) % 5 * 288) // 240


print(t())
