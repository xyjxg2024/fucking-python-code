def find_range(n, arr):
    max_val = max(arr)
    min_val = min(arr)
    return max_val - min_val#极差函数

n = int(input())
arr = list(map(int, input().split()))#输入多个值

result = find_range(n, arr)
print(result)
