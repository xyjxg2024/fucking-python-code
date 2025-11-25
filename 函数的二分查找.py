import math

def func(x, y):
    return 6 * pow(x, 7) + 8 * pow(x, 6) + 7 * pow(x, 3) + 5 * x * x - y * x

def qiudao(x, y):
    return 42 * pow(x, 6) + 48 * pow(x, 5) + 21 * pow(x, 2) + 10 * x - y

t = int(input())
for _ in range(t):
    left = 0.0
    right = 100.0
    y = float(input())
    while right - left >= 1e-4:
        mid = (left + right) / 2
        if qiudao(mid, y) < 0:
            left = mid
        else:
            right = mid
    print("{0:.4f}".format(func(left, y)))

