# %% Problem 566


from math import sqrt


class ExceptionInCycle(Exception):
    pass


class MyTruc():
    a = 9
    b = 10
    c = 11
    prod = a * b * c

    def __init__(self, aa, bb):
        self.aa = aa
        self.bb = bb

    def __add__(self, other):
        return MyTruc(self.aa + other.aa, self.bb + other.bb)

    def __sub__(self, other):
        return MyTruc(self.aa - other.aa, self.bb - other.bb)

    def __eq__(self, other):
        return self.aa == other.aa and self.bb == other.bb

    def __float__(self):
        return self.aa + self.bb * sqrt(self.c)

    def __gt__(self, other):
        return self.__float__() > other.__float__()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        return self.__float__() < other.__float__()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __hash__(self):
        return (self.aa, self.bb).__hash__()

    def __repr__(self):
        return "MyTruc({}, {})".format(self.aa, self.bb)


class AngleGenerator:
    def __init__(self, *args):
        self.l = args
        self.k = 0
        self.len = len(args)

    def __next__(self):
        ans = self.l[self.k]
        self.k += 1
        self.k %= self.len
        return ans


class Cell:
    def __init__(self, x):
        self.element = x
        self.next = None
        self.last = None

    def __str__(self):
        return "(" + str(self.element) + " -> " + str(self.next) + ")"

    def join_right(self, after):
        self.next = after
        after.last = self

    def join_left(self, after):
        after.next = self
        self.last = after


class CyclicList:
    def __init__(self):
        self.start = None
        self.lecture_head = None
        self.__len = 0

    def empty(self):
        return self.start is None

    def push(self, x):
        c = Cell(x)
        if self.empty():
            c.next = c
            c.last = c
            self.start = c
            self.lecture_head = c
        else:
            n = self.lecture_head.next
            c.join_left(self.lecture_head)
            c.join_right(n)
            self.lecture_head = c

        self.__len += 1

    def pop(self):
        assert not self.empty(), "the cycle is empty"
        if self.__len == 1:
            x = self.lecture_head.element
            self.lecture_head = None
            self.start = None
            self.__len = 0
            return x
        else:
            x = self.lecture_head.element
            n = self.lecture_head.next
            l = self.lecture_head.last
            self.lecture_head = l
            self.lecture_head.join_right(n)
            self.__len -= 1
            return x

    def move_head_back(self):
        if not self.empty():
            self.lecture_head = self.lecture_head.last

    def move_head_forward(self):
        if not self.empty():
            self.lecture_head = self.lecture_head.next

    def read(self):
        if not self.empty():
            x = self.lecture_head.element
            self.move_head_forward()
            return x
        else:
            raise ExceptionInCycle("we can't read an empty cycle")

    def value(self):
        if not self.empty():
            x = self.lecture_head.element
            return x
        else:
            raise ExceptionInCycle("we can't read an empty cycle")

    def __len__(self):
        return self.__len


class Piece:
    def __init__(self, a, b):
        self.val = a
        self.bool = b

    def __repr__(self):
        return "Piece({},{})".format(self.val, self.bool)


class FuseException(Exception):
    pass


class Fuse:
    def __init__(self, lim=100000000):
        self.count = 0
        self.lim = lim

    def __next__(self):
        self.count += 1
        if self.count > self.lim:
            raise FuseException("Infinite Loop ?!   :-(   \n We make the function end after {} iterations, \n as"
                                "you wished".format(self.lim))

    def value(self):
        """

        :rtype: int
        """
        return self.count


nb = 1
l_angle = []
d = None


def F(a, b, c, k_lim):
    global nb, l_angle, d  # see remark below
    MyTruc.a = a
    MyTruc.b = b
    MyTruc.c = c
    one = MyTruc(a * b * c, 0)
    # print(one)
    t1 = MyTruc(b * c, 0)
    t2 = MyTruc(a * c, 0)

    if int(sqrt(c) + 10 ** -4) ** 2 == c:
        t3 = MyTruc(b * a * int(sqrt(c)), 0)
    else:
        t3 = MyTruc(0, b * a)
    zero = MyTruc(0, 0)
    d = CyclicList()
    d.push(Piece(zero, True))
    d.push(Piece(t1, False))
    L = AngleGenerator(t1, t2, t3)
    t = L.__next__()
    counter = Fuse(k_lim)
    counter.__next__()
    nb = 1
    while True:
        nb += 1  # just a global variable to have an idea of the progress of the computing, looking from the console,
        # outside the function
        try:
            counter.__next__()
            t_0 = t
            t += L.__next__()
            l_angle = []
            if t >= one:
                t -= one
                x = None
                while not d.empty():
                    d.move_head_forward()
                    x = d.value()
                    if t_0 >= x.val:
                        d.move_head_back()
                        break
                    else:
                        d.pop()
                        l_angle.append(x)

                while not d.empty():
                    d.move_head_forward()
                    x = d.value()
                    if t < x.val:
                        d.move_head_back()
                        break
                    else:
                        d.pop()
                        if x.val != t:
                            l_angle.append(Piece(x.val + one, x.bool))
                        else:
                            break

                if x is not None:
                    bool_end = x.bool
                else:
                    d.move_head_forward()
                    bool_end = d.value()
                    d.move_head_back()

                y = d.value().bool
                ok = False
                if y == (not bool_end):
                    d.pop()
                    if l_angle == []:
                        d.push(Piece(t, y))
                    else:
                        tt = t_0 + t + one - l_angle[-1].val
                        if tt > one:
                            tt -= one
                        d.push(Piece(tt, y))
                        l_angle = l_angle[:-1]
                        ok = True
                for piece in l_angle[::-1]:
                    tt = t_0 + t + one - piece.val
                    if tt > one:
                        tt -= one
                    d.push(Piece(tt, piece.bool))
                if not ok:
                    if l_angle == [] and y == bool_end:
                        d.push(Piece(t, not bool_end))
                    elif l_angle != []:
                        y = d.value().bool
                        d.push(Piece(t, not y))
                else:
                    d.push(Piece(t, not d.value().bool)) #????
                if len(d) == 1 and d.value().bool:
                    return counter.value()

            else:
                x = None
                while not d.empty():
                    d.move_head_forward()
                    x = d.value()
                    if t_0 >= x.val or x.val > t:
                        d.move_head_back()
                        break
                    else:
                        d.pop()
                        if x.val != t:
                            l_angle.append(x)
                        else:
                            break

                if x is not None:
                    bool_end = x.bool
                else:
                    d.move_head_forward()
                    bool_end = d.value()
                    d.move_head_back()

                y = d.value().bool
                ok = False
                if y == (not bool_end):
                    d.pop()
                    if l_angle == []:
                        d.push(Piece(t, y))
                    else:
                        d.push(Piece(t_0 + t - l_angle[-1].val, y))
                        l_angle = l_angle[:-1]
                        ok = True
                for piece in l_angle[::-1]:
                    d.push(Piece(t_0 + t - piece.val, piece.bool))
                if not ok:
                    if l_angle == [] and y == bool_end:
                        d.push(Piece(t, not bool_end))
                    elif l_angle != []:
                        y = d.value().bool
                        d.push(Piece(t, not y))
                else:     #   to report for t > one ???
                    d.push(Piece(t, not d.value().bool))
                if len(d) == 1 and d.value().bool:
                    return counter.value()

        except ValueError as e:
            print(e)
            print("It was a ValueError, sponsored by IMakeYouCrazy")
            raise e

        except FuseException:
            print("loop forced to quit")
            for i in range(len(d)):
                p = d.read()
                print(p, p.val.__float__())
            break

        """
        except Exception as e:
            print(e)
            print(e.__context__)
            print("It was an Exception, sponsored by IMakeYouEvenMoreCrazy")
            raise e
        """

# print("yo")
# return nb

print(F(9, 10, 11, 70))
print(F(10, 14, 16, 600))

aa, bb, cc = 9, 10, 11
s = 0

def G(n):
    global aa, bb, cc, s
    s = 0
    for a in range(9, n+1):
        for b in range(a+1, n + 1):
            for c in range(b+1, n + 1):
                s += F(a, b, c, 10**8)
                aa, bb, cc = a, b, c
    return s
