def ok(n):
    s = list(str(n))
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i+1] == s[i+2]:
            return False
    return True

s = 0
for k in range(1, 10**11):
    if ok(k):
        s += 1/k

from math import log
import heapq

S = log(10**12)


class FilePrioCheat():
    def __init__(self):
        self.file = []
        self.last = None

    def push(self, x):
        heapq.heappush(self.file, x)

    def pop(self):
        x = heapq.heappop(self.file)
        while x == self.last:
            x = heapq.heappop(self.file)
        self.last = x
        return x

table = FilePrioCheat()
for k in range(8):
    for nb in range(1, 10**(9-k)):
        for nb2 in range(10**k):
            table.push(nb*10**(k+3) + nb2)
for i in range(1, 10):
    for k in range(9):
        for nb in range(10**(9-k)):
            for nb2 in range(10**k):
                table.push(nb*10**(k+3)+111*i*10**k + nb2)
try:
    while True:
        n = (table.pop())
        S -= 1/n
except IndexError:
    print(S)


from math import log
S = log(10**12)
table = dict()
for k in range(8):
    for nb in range(1, 10**(9-k)):
        for nb2 in range(10**k):
            table[(nb*10**(k+3) + nb2)] = 0
for i in range(1, 10):
    for k in range(9):
        for nb in range(10**(9-k)):
            for nb2 in range(10**k):
                table[nb*10**(k+3)+111*i*10**k + nb2] = 0

for i in table.keys():
    S -= 1/i

print(S)