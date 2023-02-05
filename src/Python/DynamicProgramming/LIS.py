arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


def LIS_lengths(a):
    c = [0] * len(arr)
    for i in range(len(a)):
        for j in range(i):
            if a[i] >= a[j]:
                c[i] = max(c[i], c[j])
        c[i] += 1
    return c


def find_LIS(a, i):
    c = LIS_lengths(a)
    result = [a[i]]
    j = i
    while j >= 0:
        j = j - 1
        if c[j] == c[i] - 1:
            result.append(a[j])
            i = j
    return result


print(find_LIS(arr, len(arr) - 1))
