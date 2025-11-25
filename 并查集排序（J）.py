def find(x):
    if list_a[x] != x:
        list_a[x] = find(list_a[x])  # 路径压缩
    return list_a[x]

def union(x, y):
    list_a[find(y)] = find(x)

a = int(input())
b = int(input())

# 初始化并查集数组，总共有a个人，每个人有两个状态，总大小为2*a+1（假设人编号从1开始）
max_size = 2 * a + 10  # 确保足够大
list_a = [i for i in range(max_size)]

for _ in range(b):
    parts = input().split()
    if len(parts) != 3:
        continue  # 跳过无效输入
    rel, y, z = parts[0], int(parts[1]), int(parts[2])
    if rel == "F":
        union(y, z)
    else:
        # 处理敌人关系，合并y和z的对立面，z和y的对立面
        union(y, z + a)
        union(z, y + a)

# 统计1到a中的独立集合数目
count = 0
for i in range(1, a + 1):
    if find(i) == i:
        count += 1

print(count)