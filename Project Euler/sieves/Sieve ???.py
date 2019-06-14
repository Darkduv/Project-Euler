# view thread problem 179


from Tools import timing

sep = 10**8
cp_index = 1  # to set it as an integer
size = 1


def next_prime1(n):
    global cp_index
    if n < 2:
        cp_index = 0
        return 2
    if n & 1 == 0:
        n += 1
    else:
        n += 2
    n <<= 1
    while sieve[n]:
        n += 1
    cp_index = n
    return 2*n+1


def next_prime2():
    global cp_index
    n = cp_index + 1
    if n == len(sieve):
        return None
    while sieve[n]:
        n += 1
        if n == len(sieve):
            return None
    cp_index = n
    return 2 * n + 1


def is_prime(n):
    if n == 2:
        return True
    if n & 1 == 0 or n >= size or n == 1:
        return False
    return not sieve[n >> 1]


@timing
def init_sieve(n):
    global cp_index, size

    class Prime:
        prime = None
        index = None
        pass

    h = Prime()
    cp_index = 0
    if n < sep:
        n = sep
    limit1 = n
    size = n
    limit = (limit1 // sep + 1)*sep
    limit_d2 = limit // 2
    w = int(limit**0.5 + 0.1)
    small_sieve = [None]*(w+1)
    w1 = int(w**0.5 + 0.1)
    i = 5
    while i <= w:
        small_sieve[i] = True
        i += 6
    i = 7
    while i <= w:
        small_sieve[i] = True
        i += 6
    small_sieve[2] = True
    small_sieve[3] = True
    i = 5
    while i <= w1:
        if small_sieve[i]:
            j = i*i
            k = 2*i
            while j <= w:
                small_sieve[j] = False
                j += k
        i += 2
    small_count = 0
    i = 3
    while i <= w:
        if small_sieve[i]:
            small_count += 1
        i += 2
    p = [Prime()]*(small_count+1)
    h.prime = 2
    h.index = 4
    p[0] = h
    i = 3
    count = 1
    while i <= w:
        if small_sieve[i]:
            h2 = Prime()
            h2.prime = i
            h2.index = (i*i) // 2
            p[count] = h2
            count += 1
        i += 2
    del small_sieve
    sieve = [None]*(limit_d2+1)
    i = 4
    while i <= limit_d2:
        sieve[i] = True
        i += 3

    # start bigsieve
    max_index = sep - 1
    while max_index < limit_d2:
        i = 2
        while i <= small_count:
            j = p[i].index
            if j <= max_index:
                k = p[i].prime*3
                while True:
                    sieve[j] = True
                    j += k
                    if j > max_index:
                        break
                p[i].index = j
            i += 1
        max_index += sep

    for i in range(2, small_count+1):
        k = p[i].prime
        if k % 6 == 1:
            p[i].index = (k*k+4*k) // 2
        else:
            p[i].index = (k*k+2*k) // 2
        max_index = sep - 1
        while max_index < limit_d2:
            i = 2
            while i <= small_count:
                j = p[i].index
                if j <= max_index:
                    k = 3*p[i].prime
                    while True:
                        sieve[j] = True
                        j += k
                        if j > max_index:
                            break
                    p[i].index = j
                i += 1
            max_index += sep
        # del p
    return sieve

sieve = init_sieve(10**9)


l = []
p = 2
while p is not None and p < 10 ** 9:
    l.append(p)
    p = next_prime2()
