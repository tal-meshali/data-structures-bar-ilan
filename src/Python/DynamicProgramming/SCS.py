import Python.DynamicProgramming.LCS as LCS


def SCS(T1, T2, counter, i=0, j=0, s=""):
    if i == len(T1) and j == len(T2):
        if not counter.lst:
            counter.increment(len(s))
            counter.add(s)
        elif len(s) == counter.num:
            counter.add(s)
        elif len(s) < counter.num:
            counter.increment(len(s))
            counter.clean(s)
        return s
    if i == len(T1):
        return SCS(T1, T2, counter, i, j + 1, s + T2[j])
    elif j == len(T2):
        return SCS(T1, T2, counter, i + 1, j, s + T1[i])
    elif T1[i] == T2[j]:
        return SCS(T1, T2, counter, i + 1, j + 1, s + T2[j])
    else:
        return SCS(T1, T2, counter, i + 1, j, s + T1[i]), SCS(T1, T2, counter, i, j + 1, s + T2[j])


def find_SCS(T1, T2):
    result = LCS.Manager()
    SCS(T1, T2, result)
    print(result.lst)


def main():
    B1 = "ABCBDAB"
    B2 = "BDCABA"
    find_SCS(B1, B2)

main()
