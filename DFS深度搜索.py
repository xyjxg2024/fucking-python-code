import sys
sys.setrecursionlimit(10**6)
a, b = map(int, input().split())
list_a = []
list_b = [[0 for _ in range(b)] for _ in range(a)]  # 正确初始化
list_h = [-1, 1, 0, 0]
list_l = [0, 0, -1, 1]
x = 0

for i in range(a):
    n = list(map(int, input()))
    list_a.append(n)

def dfs(x, y):
    list_b[x][y] = 1
    for i in range(4):  # 遍历四个方向
        nx = x + list_h[i]
        ny = y + list_l[i]
        if 0 <= nx < a and 0 <= ny < b:
            if list_a[nx][ny] != 0 and list_b[nx][ny] == 0:
                dfs(nx, ny)

for i in range(a):
    for j in range(b):
        if list_a[i][j] != 0 and list_b[i][j] == 0:
            dfs(i, j)
            x += 1  # 正确增加计数器
print(x)