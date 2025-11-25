def find(x):
    # 路径压缩查找函数
    if a[x] != x:
        a[x] = find(a[x])
    return a[x]


def union(x, y):
    # 合并函数
    root_x = find(x)
    root_y = find(y)
    a[root_x] = root_y

while True:
        # 读取第一行输入
        line = input().strip()
        if line == '0':
            break
        # 读取 m 和 n
        parts = list(map(int, line.split()))
        if len(parts) < 2:
            # 如果第一行只有一个数且不是0，可能是异常输入，跳过
            continue
        m, n = parts[0], parts[1]

        # 初始化并查集
        a = [i for i in range(m + 1)]  # 假设元素从1到m编号

        # 读取 n 对数据并进行合并操作
        for _ in range(n):
            x, y = map(int, input().split())
            union(x, y)

        # 计算连通分量的数量
        ok = [0] * (m + 1)
        count = 0
        for i in range(1, m + 1):
            root = find(i)
            if not ok[root]:
                ok[root] = 1
                count += 1

        # 输出结果
        print(count - 1)
