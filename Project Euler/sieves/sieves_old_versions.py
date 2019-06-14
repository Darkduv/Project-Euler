def oldsieve2(limit):
    sieve_bound = (limit - 1) // 2
    sieve_tab = [True] * (sieve_bound + 1)
    cross_limit = (int(limit ** 0.5 + 0.1) + 1) // 2
    l = [2]
    for i in range(1, cross_limit + 1):
        if sieve_tab[i]:
            l.append(2 * i + 1)
            for j in range(2 * i * (i + 1), sieve_bound + 1, 2 * i + 1):
                sieve_tab[j] = False
    for j in range(cross_limit + 1, sieve_bound + 1):
        if sieve_tab[j]:
            l.append(2 * j + 1)
    return l


def olderatosthene(n):
    n_root = int(n ** 0.5)
    sieve = list(range(n + 1))
    sieve[1] = 0

    for i in range(2, n_root + 1):
        if sieve[i] != 0:
            m = n // i - i
            sieve[i * i: n + 1:i] = [0] * (m + 1)

    sieve = [x for x in sieve if x != 0]
    return sieve


def olderatosthene2(n):
    n_root = int(n ** 0.5) // 2
    sieve = [2] + list(range(3, n + 1, 2))
    length = len(sieve)
    for i in range(1, n_root + 1):
        if sieve[i] != 0:
            j = 2*i+1
            a = (j * j - 1) // 2
            m = n//j - j
            sieve[a: length + 1: j] = [0] * (m//2 + 1)

    sieve = [x for x in sieve if x != 0]
    return sieve
