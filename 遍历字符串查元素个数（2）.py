def count_digit(n, x):
    count = 0
    for i in range(1, n + 1):
        count += str(i).count(str(x))
    return count
n, x = map(int, input().split())
print(count_digit(n, x))