from collections import deque

# 读取输入
n, m, a, b = map(int, input().split())

# 初始化一个二维列表来记录每个位置被感染的时间，初始值为-1表示未被感染
list_a = [[-1 for _ in range(m)] for _ in range(n)]

# 初始化一个队列用于广度优先搜索（BFS）
queue = deque()

# 读取a个感染源的位置，并将它们的时间初始化为0，加入队列
for _ in range(a):
    x, y = map(int, input().split())
    list_a[x-1][y-1] = 0  # 将坐标转换为0索引
    queue.append((x-1, y-1))

# 读取b个需要检查的点，并存储它们的位置和索引
queue2 = []
queued = {}  # 用于存储每个位置对应的索引

for i in range(b):
    x, y = map(int, input().split())
    queue2.append((x-1, y-1))  # 将坐标转换为0索引
    queued[(x, y)] = i  # 使用原始输入的坐标（1索引）作为键

# 定义四个方向：上、下、左、右
way = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 初始化一个集合，用于记录已经被感染的检查点的索引
in_queue2 = set()

# 开始广度优先搜索（BFS）
while queue and len(in_queue2) < b:
    # 从队列中取出一个位置
    x, y = queue.popleft()
    real_time = list_a[x][y]

    # 遍历四个方向
    for dx, dy in way:
        new_x, new_y = x + dx, y + dy

        # 检查新位置是否在网格范围内且未被感染
        if 0 <= new_x < n and 0 <= new_y < m and list_a[new_x][new_y] == -1:
            list_a[new_x][new_y] = real_time + 1  # 更新感染时间
            queue.append((new_x, new_y))  # 将新位置加入队列

            # 检查这个新位置是否是需要检查的点之一
            if (new_x, new_y) in queued:
                # 如果是，则将对应的索引加入集合
                i = queued[(new_x, new_y)]
                in_queue2.add(i)

# 输出每个检查点的感染时间，未被感染的输出-1
for i in range(b):
    x, y = queue2[i]
    print(list_a[x][y])