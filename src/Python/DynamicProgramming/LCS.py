import numpy as np


# Solution 1 - most efficient
class Manager:
    def __init__(self):
        self.num = 0
        self.lst = []

    def increment(self, value):
        self.num = value

    def add(self, value):
        self.lst.append(value)

    def clean(self, value):
        self.lst = [value]


def find_LCS(T1, T2):
    result = Manager()
    B(T1, T2, len(T1) - 1, len(T2) - 1, result)
    print(result.lst)


def find_repeat(T1):
    result = Manager()
    B(T1, T1, len(T1) - 1, len(T1) - 1, result, True)
    print(set(result.lst))


def B(T1, T2, i, j, counter, rule=False, s=""):
    if i == -1 or j == -1:
        if len(s) == counter.num:
            counter.add(s[::-1])
        if len(s) > counter.num:
            counter.clean(s[::-1])
            counter.increment(len(s))
        return counter
    if T1[i] == T2[j] and (not rule or i != j):
        s = s + T2[j]
        return B(T1, T2, i - 1, j - 1, counter, rule, s)
    else:
        return B(T1, T2, i - 1, j, counter, rule, s), B(T1, T2, i, j - 1, counter, rule, s)


# Solution 2
def C(T1, T2, i, j, m):
    if i == 0 or j == 0:
        m[i, j] = 0
    else:
        corr = 1 if T1[i - 1] == T2[j - 1] else 0
        m[i, j] = max([m[i - 1, j], m[i, j - 1], m[i - 1, j - 1] + corr])


def print_matrix(T1, T2):
    m = np.zeros((len(T1) + 1, len(T2) + 1))
    for i in range(len(T1) + 1):
        for j in range(len(T2) + 1):
            C(T1, T2, i, j, m)

    for j in range(m.shape[1]):
        if j == 0:
            print("   *  ", end='')
        else:
            print(T2[j - 1], " ", end='')
    print("")
    for i in range(m.shape[0]):
        if i == 0:
            c = "*"
        else:
            c = T1[i - 1]
        print(c, m[i])
    max_m = m[m.shape[0] - 1, m.shape[1] - 1]
    return max_m


def main():
    A1 = "ABCBDAB"
    A2 = "BDCABA"

    T3 = "ABBDCACB"
    T4 = "ATACTCGGA"

    find_LCS(A1, A2)  # regular
    find_LCS(T3, T3[::-1])  # Palindrome
    find_repeat(T4)  # longest repetitions

