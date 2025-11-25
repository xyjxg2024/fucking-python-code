# 多组测试用例，先读入测试用例数量
for _ in range(int(input())):

    # 读入 x：数组长度，y：操作次数
    x, y = map(int, input().split())

    # 读入数组并排序（从小到大）
    list_a = sorted(list(map(int, input().split())))

    ans = 0  # 用来保存最大剩余和

    # 构造前缀和数组 list_b，list_b[i] 表示前 i 个元素的和
    list_b = [0] * (x + 1)
    for i in range(x):
        list_b[i + 1] = list_b[i] + list_a[i]

    # 枚举“删除 i 对最小值”的情况，i 从 0 到 y
    for i in range(y + 1):
        # 删除 i 对最小值（共 2*i 个）
        # 删除 (y - i) 个最大值（共 y - i 个）
        # 剩余部分为：list_a[2*i] 到 list_a[x - (y - i) - 1]
        # 其和为：list_b[x - (y - i)] - list_b[2*i]
        ans = max(ans, list_b[x - (y - i)] - list_b[2 * i])

    # 输出最大剩余和
    print(ans)