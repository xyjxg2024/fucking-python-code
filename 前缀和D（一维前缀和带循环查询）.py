n, m, k = map(int, input().split())
a = list(map(int, input().split()))

# 初始化数组，索引从1开始
a = [0] + a  # a[1..n]
c = [0] * (n + 2)  # c[1..n]
for i in range(1, n+1):
    c[i] = a[i] - a[i-1]

# 读取m个操作，b[1..m]
b = [[] for _ in range(m+2)]  # 索引1到m
for i in range(1, m+1):
    l, r, val = map(int, input().split())
    b[i] = (l, r, val)

# 处理k次查询，差分数组d[1..m]
d = [0] * (m + 2)
for _ in range(k):
    x, y = map(int, input().split())
    d[x] += 1
    if y + 1 <= m:
        d[y + 1] -= 1

# 计算前缀和得到每个操作被应用的次数
for i in range(1, m+1):
    d[i] += d[i-1]

# 应用操作到差分数组c
for i in range(1, m+1):
    l, r, val = b[i]
    c[l] += val * d[i]
    if r + 1 <= n:
        c[r + 1] -= val * d[i]

# 还原数组
result = [0] * (n + 1)
for i in range(1, n+1):
    result[i] = result[i-1] + c[i]
    print(result[i], end=' ')
