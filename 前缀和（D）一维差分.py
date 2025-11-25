y = []  # 用于存储每次查询的结果

while True:
    a = int(input())
    if a == 0:
        break  # 如果输入为0，退出循环

    s = [0] * (a + 5)  # 初始化差分数组

    # 更新差分数组
    for j in range(a):
        b, c = map(int, input().split())
        s[b] += 1
        if c + 1 <= a + 4:  # 确保不会越界
            s[c + 1] -= 1

    # 计算前缀和
    for k in range(1, a + 1):
        s[k] += s[k - 1]

    # 存储当前查询的结果
    x = []
    for j in range(1, a + 1):
        x.append(str(s[j]))
    y.append(' '.join(x))

# 统一输出所有结果
for result in y:
    print(result)