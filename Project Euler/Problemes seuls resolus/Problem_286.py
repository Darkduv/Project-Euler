# %% Problem 286

from Tools import dichotomy


def prob(q):
    def prob_q(x):
        return 1-x/q
    L = [[0]*21 for _ in range(51)]
    L[1] = [1-prob_q(1), prob_q(1)]+[0]*19
    for i in range(2, 51):
        L[i][0] = L[i-1][0]*(i/q)
        for k in range(1, 21):
            a = prob_q(i)
            L[i][k] = L[i-1][k]*(1-a) + L[i-1][k-1]*a
    return L[50][20] - 0.02


q0 = dichotomy(prob, 51, 100, 10**-10)
print('{:.10f}'.format(q0))  # sol = 52.6494571953
