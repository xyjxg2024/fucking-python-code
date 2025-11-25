n = int(input())
x = list(map(int, input().split()))

a = 0
sum = {0: -1}  # 初始时，前缀和0的位置为-1
max = 0

for i in range(n):
    if x[i] == 0:
        a -= 1
    else:
        a += 1
    # 检查当前前缀和是否已经存在
    if a in sum:
        # 如果存在，计算当前子数组的长度
        y = i - sum[a]
        if y > max:
            max = y
    else:
        # 如果不存在，记录当前前缀和的位置
        sum[a] = i

print(max)