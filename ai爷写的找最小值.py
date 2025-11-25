def find_min(n, a):
    min_value = a[0]
    for i in range(1, n):
        if a[i] < min_value:
            min_value = a[i]
    return min_value

n = int(input())
a = list(map(int, input().split()))
print(find_min(n, a))