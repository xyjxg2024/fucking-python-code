# 读取输入的三个整数 a, b, c
a, b, c = map(int, input().split())

# 初始化并查集的父节点数组，大小为 a+5，确保足够大
list_a = [i for i in range(a + 5)]

# 初始化秩数组，大小为 a+5，初始值为 1
rank = [1] * (a + 5)

# 查集函数，实现路径压缩
def find(x):
    # 如果当前节点不是根节点，递归查找根节点，并进行路径压缩
    if list_a[x] != x:
        list_a[x] = find(list_a[x])
    # 返回根节点
    return list_a[x]

# 并集函数，实现按秩合并
def union(x, y):
    # 分别查找 x 和 y 的根节点
    far_x = find(x)
    far_y = find(y)
    # 如果根节点不同，进行合并
    if far_x != far_y:
        # 将秩较小的树合并到秩较大的树上
        if rank[far_x] > rank[far_y]:
            list_a[far_y] = far_x
        else:
            list_a[far_x] = far_y
            # 如果两棵树的秩相等，合并后秩加 1
            if rank[far_x] == rank[far_y]:
                rank[far_y] += 1

# 主函数
# 处理 b 次合并操作
for _ in range(b):
    x, y = map(int, input().split())
    union(x, y)

# 处理 c 次查询操作
for _ in range(c):
    m, n = map(int, input().split())
    # 如果 m 和 n 的根节点相同，说明连通，输出 Yes
    if find(m) == find(n):
        print("Yes")
    # 否则，输出 No
    else:
        print("No")