a = int(input())
zz=[]
# 初始化一个 (30) x (30) 的二维数组，用于存储前缀和
s = [[0] * 2006 for _ in range(2006)]

# 读取输入并填充数组
for _ in range(a):
    b, c, d = map(int, input().split())
    # 将 d 的值赋给 s[b][c]
    s[b+1][c+1] = d

# 计算二维前缀和
for i in range(1, 2006):
    for j in range(1, 2006):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + s[i][j]
b=int(input())
for i in range(b):
    e,f,g,h=map(int,input().split())
    total = s[g+1][h+1] - s[e][h+1] - s[g+1][f] + s[e][f]
    zz.append(total)
for i in zz:
    print(i)
