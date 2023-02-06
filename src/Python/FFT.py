import cmath


def runner_FFT(a):
    n = len(a)
    if n == 1:
        return a
    a_even = runner_FFT(a[::2])
    a_odd = runner_FFT(a[1::2])
    result = [0] * n
    for j in range(n//2):
        w = cmath.exp(2 * cmath.pi * complex(0, 1) * j / n)
        result[j] = a_even[j] + w * a_odd[j]
        result[j + n//2] = a_even[j] - w * a_odd[j]
    return result


def FFT(a):
    n = len(a)
    k = 2
    while n / k > 1:
        k *= 2
    return runner_FFT(a + [0] * (n - k))


arr = [1,1,1,1,1,1,1,1]
print(FFT(arr))
