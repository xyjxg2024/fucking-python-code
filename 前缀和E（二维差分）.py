a, b = map(int, input().split())
s = [[0] * (a + 2) for _ in range(a + 2)]  # 调整数组大小
c = int(input())
for _ in range(c):
    x1, y1, x2, y2 = map(int, input().split())
    s[x1][y1] += 1
    s[x2 + 1][y1] -= 1
    s[x1][y2 + 1] -= 1
    s[x2 + 1][y2 + 1] += 1

# 第一次二维前缀和计算
for i in range(1, a + 1):
    for j in range(1, a + 1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + s[i][j]

# 将非零元素置为1
for i in range(1, a + 1):
    for j in range(1, a + 1):
        if s[i][j] != 0:
            s[i][j] = 1

# 第二次二维前缀和计算
for i in range(1, a + 1):
    for j in range(1, a + 1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + s[i][j]

x = []
d = int(input())
for _ in range(d):
    x3, y3, x4, y4 = map(int, input().split())
    # 计算查询区域的覆盖情况
    covered = s[x4][y4] - s[x4][y3-1] - s[x3-1][y4] + s[x3-1][y3-1]
    area = (y4 - y3 + 1) * (x4 - x3 + 1)
    if covered == area:
        x.append("YES")
    else:
        x.append("NO")

for res in x:
    print(res)