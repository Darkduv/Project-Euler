from os import chdir
from math import log
from Tools import numpy_sieve, timing, nb_to_digits, sum_digit, binary_search_inf, binary_search, is_prime


chdir("/Users/maximin/Desktop/Euler/linked_files")


# %% Problem 50

def problem_50(lim=10**6):
    L_6 = numpy_sieve(lim)
    i_end = len(L_6)
    s_M = 0
    nb_M = 1
    s = 0
    i, j = 0, 0
    nb = 0
    while j < i_end:
        while s < lim:
            s += L_6[j]
            j += 1
            nb += 1
            if s in L_6:
                if nb > nb_M:
                    s_M = s
                    nb_M = nb

        nb = nb_M - 1
        s = sum(L_6[i + 1:i + nb_M])
        j = i + nb_M
        if s + L_6[j] > lim:
            break
        i += 1
    print(s_M)  # sol = 997651


# %% Problem 51

def problem_51():
    l_7 = numpy_sieve(10 ** 7)
    i_start = binary_search_inf(l_7, 10**5)

    def make_pattern(n):
        m = str(n)
        for digit in m:
            if m.count(digit) == 3:
                yield [5 - i for i in range(len(m) - 1, -1, -1) if m[i] == digit]

    def apply_pattern(n, pat):
        n2 = 0
        k = 0
        while n != 0:
            n2 += (n % 10) * 10**k if k not in pat else 0
            n //= 10
            k += 1
        return n2

    def add(n, pat):
        for i in pat:
            n += 10**i
        return n

    viewed = set()
    for p in l_7[i_start:]:
        for pattern in make_pattern(p):
            p2 = apply_pattern(p, pattern)
            if p2 in viewed:
                continue
            viewed.add(p2)
            nb = 0
            for d in range(10):
                if (5 not in pattern or d != 0) and binary_search(l_7, p2)[0]:
                    nb += 1
                if nb + 9-d < 8:
                    break
                p2 = add(p2, pattern)
            if nb < 8:
                continue
            print(p)  # sol = 121313
            return


# %% Problem 52

def problem_52():
    def ok(n):
        l_n = nb_to_digits(n)

        def ok_bis(m):
            l_m = nb_to_digits(m)
            for i in l_n:
                if i not in l_m:
                    return False
                else:
                    l_m.remove(i)
            return True

        for k in range(2, 7):
            if not ok_bis(k * n):
                return False
        return True

    nb = 1008  # it's really easy to prove that n % 9 == 0 because of the constant sum of the digits
    # and n = 17.... or 18... or 19... are not possible since 17*6 > 100 => not the same number of digits
    # then 1.. * 2 has 2 or 3 as last digit (at the left), 1.. * 3 has 3, 4, or 5
    # 1..*4 has 4, 5, or 6;    1..*5 has 5, 6, 7 or 8 and   1.. * 6 has 6, 7, 8, or 9
    # so it's easy to see that n have more than 3 digits
    # -> if 1..*6 = 6.. then 1..*5 = 5.., 1..*4 = 4.., etc ..
    # so n has more than 6 digits (1, 2, 3, 4, 5, 6) -> sum = 3 [9] so a seventh digit is needed ...
    # -> if 1..*2 = 2.., n*3 = 3.. or 4.., n*4 = 4.. or 5..
    while not ok(nb):
        a = str(nb)
        if a[0] != '1':
            nb += 9 * 10 ** (len(a) - 1)
        elif a[1] == "7":
            nb += 3 * 10 ** (len(a) - 2) + 6
        else:
            nb += 9
    print(nb)  # sol = 142857


# %% Problem 53

def problem_53(c_nr_max=10**6, max_n=100):  # see overview, program F
    count = 0
    r = 0
    nCr = 1
    n = max_n
    while r < n / 2:
        C_right = (nCr * (n - r)) // (r + 1)
        if C_right <= c_nr_max:
            r += 1
            nCr = C_right
        else:
            C_up_right = (nCr * (n - r)) / n
            count += n - 2 * r - 1
            n -= 1
            nCr = C_up_right
    print(count)  # sol = 4075


# %% Problem 54
# Todo ? can something be optimized ??

def problem_54():
    l_hands = []
    with open("p054_poker.txt", "r") as f:
        for i in f:
            t_card = i[:-1].split(" ")
            l_hands.append([t_card[:5], t_card[5:]])
    d_value = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    for i in range(2, 10):
        d_value[str(i)] = i

    def straight(hand):
        l_cards = [d_value[card[0]] for card in hand]
        l_cards.sort()
        for i0 in range(4):
            if l_cards[i0] + 1 != l_cards[i0 + 1]:
                return False, 0
        return True, l_cards[-1]

    def flush(hand):
        s = hand[0][1]
        for card in hand:
            if card[1] != s:
                return False
        return True

    def values(hand):
        return [d_value[s[0]] for s in hand]

    def ranks_hands(hand):
        bool1, card = straight(hand)
        if flush(hand):
            if bool1:
                if card == 14:
                    return 10, 0, 0  # Royal Flush
                else:
                    return 9, card, 0  # Straight Flush
            else:
                l_val = values(hand)
                l_val.sort()
                n = 0
                for val in l_val:
                    n *= 100
                    n += val
                return 6, n, 0  # Flush

        elif bool1:
            return 5, card, 0  # Straight

        else:
            l_cards = values(hand)
            for card in l_cards[:2]:
                if l_cards.count(card) == 4:
                    return 8, card, 0  # Four

            for card in l_cards[:3]:
                if l_cards.count(card) == 3:
                    ll = [s for s in l_cards if s != i]
                    if ll[0] == ll[1]:
                        return 7, card, 0  # Full House
                    else:
                        return 4, card, max(ll)  # Three

            for card in l_cards[:]:
                if l_cards.count(card) == 2:
                    ll = [s for s in l_cards if s != card]
                    for j in ll:
                        if ll.count(j) == 2:
                            return 3, max(card, j), min(card, j)
                    return 2, card, max(ll)
            return 1, max(l_cards), 0

    nb = 0
    for hand1, hand2 in l_hands:
        if ranks_hands(hand1) >= ranks_hands(hand2):
            nb += 1
    print(nb)  # sol = 376


# %% Problem 55:

def problem_55():
    def pal(n):
        return n.__str__() == n.__str__()[::-1]

    def aux(n):
        m = int(n.__str__()[::-1])
        return m + n

    def lychrel(n):
        for repeat in range(0, 50):
            n = aux(n)
            if pal(n):
                return False
        return True

    nb = 0
    for i in range(1, 10000):
        if lychrel(i):
            nb += 1
    print(nb)  # sol = 249


# %% Problem 56

def problem_56():
    nb_m = 0

    for a in range(1, 100):
        p = 1
        for b in range(1, 100):
            p *= a
            nb = sum_digit(p)
            if nb > nb_m:
                nb_m = nb
    print(nb_m)  # sol = 972


# %% Problem 57

def problem_57():
    def nbr(c):
        return int(log(c))

    a, b = 1, 1
    nb = 0
    for i in range(1000):
        a, b = 2 * b + a, a + b
        if nbr(a) > nbr(b):
            nb += 1
    print(nb)  # sol = 153


# %% Problem 58
# Todo ? ## could be better by memorising the index of the last prime
def problem_58():
    l_6 = numpy_sieve(10**6)
    nb, i = 0, 0
    a = 1
    while True:
        i += 1
        ii = i << 1
        a += ii << 2
        b = a - ii
        c = b - ii
        d = c - ii

        for j in [b, c, d]:
            if is_prime(j, l_6):
                nb += 1

        if nb * 10 <= (ii << 1):
            print(ii+1)  # sol = 26241
            break


# %% Problem 59

def problem_59():
    l_code = [79, 59, 12, 2, 79, 35, 8, 28, 20, 2, 3, 68, 8, 9, 68, 45, 0, 12, 9, 67, 68, 4, 7, 5, 23, 27, 1, 21, 79,
              85, 78, 79, 85, 71, 38, 10, 71, 27, 12, 2, 79, 6, 2, 8, 13, 9, 1, 13, 9, 8, 68, 19, 7, 1, 71, 56, 11, 21,
              11, 68, 6, 3, 22, 2, 14, 0, 30, 79, 1, 31, 6, 23, 19, 10, 0, 73, 79, 44, 2, 79, 19, 6, 28, 68, 16, 6, 16,
              15, 79, 35, 8, 11, 72, 71, 14, 10, 3, 79, 12, 2, 79, 19, 6, 28, 68, 32, 0, 0, 73, 79, 86, 71, 39, 1, 71,
              24, 5, 20, 79, 13, 9, 79, 16, 15, 10, 68, 5, 10, 3, 14, 1, 10, 14, 1, 3, 71, 24, 13, 19, 7, 68, 32, 0, 0,
              73, 79, 87, 71, 39, 1, 71, 12, 22, 2, 14, 16, 2, 11, 68, 2, 25, 1, 21, 22, 16, 15, 6, 10, 0, 79, 16, 15,
              10, 22, 2, 79, 13, 20, 65, 68, 41, 0, 16, 15, 6, 10, 0, 79, 1, 31, 6, 23, 19, 28, 68, 19, 7, 5, 19, 79,
              12, 2, 79, 0, 14, 11, 10, 64, 27, 68, 10, 14, 15, 2, 65, 68, 83, 79, 40, 14, 9, 1, 71, 6, 16, 20, 10, 8,
              1, 79, 19, 6, 28, 68, 14, 1, 68, 15, 6, 9, 75, 79, 5, 9, 11, 68, 19, 7, 13, 20, 79, 8, 14, 9, 1, 71, 8,
              13, 17, 10, 23, 71, 3, 13, 0, 7, 16, 71, 27, 11, 71, 10, 18, 2, 29, 29, 8, 1, 1, 73, 79, 81, 71, 59, 12,
              2, 79, 8, 14, 8, 12, 19, 79, 23, 15, 6, 10, 2, 28, 68, 19, 7, 22, 8, 26, 3, 15, 79, 16, 15, 10, 68, 3, 14,
              22, 12, 1, 1, 20, 28, 72, 71, 14, 10, 3, 79, 16, 15, 10, 68, 3, 14, 22, 12, 1, 1, 20, 28, 68, 4, 14, 10,
              71, 1, 1, 17, 10, 22, 71, 10, 28, 19, 6, 10, 0, 26, 13, 20, 7, 68, 14, 27, 74, 71, 89, 68, 32, 0, 0, 71,
              28, 1, 9, 27, 68, 45, 0, 12, 9, 79, 16, 15, 10, 68, 37, 14, 20, 19, 6, 23, 19, 79, 83, 71, 27, 11, 71, 27,
              1, 11, 3, 68, 2, 25, 1, 21, 22, 11, 9, 10, 68, 6, 13, 11, 18, 27, 68, 19, 7, 1, 71, 3, 13, 0, 7, 16, 71,
              28, 11, 71, 27, 12, 6, 27, 68, 2, 25, 1, 21, 22, 11, 9, 10, 68, 10, 6, 3, 15, 27, 68, 5, 10, 8, 14, 10,
              18, 2, 79, 6, 2, 12, 5, 18, 28, 1, 71, 0, 2, 71, 7, 13, 20, 79, 16, 2, 28, 16, 14, 2, 11, 9, 22, 74, 71,
              87, 68, 45, 0, 12, 9, 79, 12, 14, 2, 23, 2, 3, 2, 71, 24, 5, 20, 79, 10, 8, 27, 68, 19, 7, 1, 71, 3, 13,
              0, 7, 16, 92, 79, 12, 2, 79, 19, 6, 28, 68, 8, 1, 8, 30, 79, 5, 71, 24, 13, 19, 1, 1, 20, 28, 68, 19, 0,
              68, 19, 7, 1, 71, 3, 13, 0, 7, 16, 73, 79, 93, 71, 59, 12, 2, 79, 11, 9, 10, 68, 16, 7, 11, 71, 6, 23, 71,
              27, 12, 2, 79, 16, 21, 26, 1, 71, 3, 13, 0, 7, 16, 75, 79, 19, 15, 0, 68, 0, 6, 18, 2, 28, 68, 11, 6, 3,
              15, 27, 68, 19, 0, 68, 2, 25, 1, 21, 22, 11, 9, 10, 72, 71, 24, 5, 20, 79, 3, 8, 6, 10, 0, 79, 16, 8, 79,
              7, 8, 2, 1, 71, 6, 10, 19, 0, 68, 19, 7, 1, 71, 24, 11, 21, 3, 0, 73, 79, 85, 87, 79, 38, 18, 27, 68, 6,
              3, 16, 15, 0, 17, 0, 7, 68, 19, 7, 1, 71, 24, 11, 21, 3, 0, 71, 24, 5, 20, 79, 9, 6, 11, 1, 71, 27, 12,
              21, 0, 17, 0, 7, 68, 15, 6, 9, 75, 79, 16, 15, 10, 68, 16, 0, 22, 11, 11, 68, 3, 6, 0, 9, 72, 16, 71, 29,
              1, 4, 0, 3, 9, 6, 30, 2, 79, 12, 14, 2, 68, 16, 7, 1, 9, 79, 12, 2, 79, 7, 6, 2, 1, 73, 79, 85, 86, 79,
              33, 17, 10, 10, 71, 6, 10, 71, 7, 13, 20, 79, 11, 16, 1, 68, 11, 14, 10, 3, 79, 5, 9, 11, 68, 6, 2, 11, 9,
              8, 68, 15, 6, 23, 71, 0, 19, 9, 79, 20, 2, 0, 20, 11, 10, 72, 71, 7, 1, 71, 24, 5, 20, 79, 10, 8, 27, 68,
              6, 12, 7, 2, 31, 16, 2, 11, 74, 71, 94, 86, 71, 45, 17, 19, 79, 16, 8, 79, 5, 11, 3, 68, 16, 7, 11, 71,
              13, 1, 11, 6, 1, 17, 10, 0, 71, 7, 13, 10, 79, 5, 9, 11, 68, 6, 12, 7, 2, 31, 16, 2, 11, 68, 15, 6, 9, 75,
              79, 12, 2, 79, 3, 6, 25, 1, 71, 27, 12, 2, 79, 22, 14, 8, 12, 19, 79, 16, 8, 79, 6, 2, 12, 11, 10, 10, 68,
              4, 7, 13, 11, 11, 22, 2, 1, 68, 8, 9, 68, 32, 0, 0, 73, 79, 85, 84, 79, 48, 15, 10, 29, 71, 14, 22, 2, 79,
              22, 2, 13, 11, 21, 1, 69, 71, 59, 12, 14, 28, 68, 14, 28, 68, 9, 0, 16, 71, 14, 68, 23, 7, 29, 20, 6, 7,
              6, 3, 68, 5, 6, 22, 19, 7, 68, 21, 10, 23, 18, 3, 16, 14, 1, 3, 71, 9, 22, 8, 2, 68, 15, 26, 9, 6, 1, 68,
              23, 14, 23, 20, 6, 11, 9, 79, 11, 21, 79, 20, 11, 14, 10, 75, 79, 16, 15, 6, 23, 71, 29, 1, 5, 6, 22, 19,
              7, 68, 4, 0, 9, 2, 28, 68, 1, 29, 11, 10, 79, 35, 8, 11, 74, 86, 91, 68, 52, 0, 68, 19, 7, 1, 71, 56, 11,
              21, 11, 68, 5, 10, 7, 6, 2, 1, 71, 7, 17, 10, 14, 10, 71, 14, 10, 3, 79, 8, 14, 25, 1, 3, 79, 12, 2, 29,
              1, 71, 0, 10, 71, 10, 5, 21, 27, 12, 71, 14, 9, 8, 1, 3, 71, 26, 23, 73, 79, 44, 2, 79, 19, 6, 28, 68, 1,
              26, 8, 11, 79, 11, 1, 79, 17, 9, 9, 5, 14, 3, 13, 9, 8, 68, 11, 0, 18, 2, 79, 5, 9, 11, 68, 1, 14, 13, 19,
              7, 2, 18, 3, 10, 2, 28, 23, 73, 79, 37, 9, 11, 68, 16, 10, 68, 15, 14, 18, 2, 79, 23, 2, 10, 10, 71, 7,
              13, 20, 79, 3, 11, 0, 22, 30, 67, 68, 19, 7, 1, 71, 8, 8, 8, 29, 29, 71, 0, 2, 71, 27, 12, 2, 79, 11, 9,
              3, 29, 71, 60, 11, 9, 79, 11, 1, 79, 16, 15, 10, 68, 33, 14, 16, 15, 10, 22, 73]

    def encrypt(l, key):
        i = 0
        ll = []
        for el in l:
            ll.append(el ^ key[i])
            i += 1
            i %= 3
        return ll

    def freq(l):
        ll = dict()
        for i in l:
            if i in ll:
                ll[i] += 1
            else:
                ll[i] = 1
        ll = [(ll[i], i) for i in ll]
        ll.sort(reverse=True)
        return ll

    def decode(i):
        l1 = l_code[i::3]
        l2 = freq(l1)
        # we assume that " " -> ord = 32 probably is the most important character
        return l2[0][1] ^ 32

    key1 = [decode(i) for i in range(3)]

    l_original = encrypt(l_code, key1)
    print(sum(l_original))  # sol = 107359


# %% Problems 50 to 59

if __name__ == "__main__":
    @timing
    def problem_50_to_59():
        for i in range(50, 60):
            print("p"+str(i)+": ", end="")
            eval("problem_"+str(i)+"()")


    problem_50_to_59()  # Execution of  problem_50_to_59  in 6.37 sec.
