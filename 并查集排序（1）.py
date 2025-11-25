a, b = map(int, input().split())
list_a = [i for i in range(a + 5)]  # 初始化并查集，每个元素的父节点是自身
rank = [1] * (a + 5)  # 初始化秩数组
list_output = []

# 查集函数
def find(n):
    if list_a[n] != n:
        list_a[n] = find(list_a[n])  # 路径压缩
    return list_a[n]

# 并集函数（按秩合并）
def union(x, y):
    far_x = find(x)
    far_y = find(y)
    if far_x != far_y:
        # 按秩合并，将秩较小的树合并到秩较大的树上
        if rank[far_x] > rank[far_y]:
            list_a[far_y] = far_x
        else:
            list_a[far_x] = far_y
            if rank[far_x] == rank[far_y]:
                rank[far_y] += 1

for _ in range(b):
    z, x, y = map(int, input().split())
    if z == 1:
        union(x, y)
    elif z == 2:
        if find(x) == find(y):
            list_output.append("Y")
        else:
            list_output.append("N")

for i in list_output:
    print(i)