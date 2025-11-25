n = int(input())
lists = []

# 输入第一个数组
for i in range(n):
    input_str = input()
    elements = list(map(int, input_str.split()))
    lists.append(elements)

m = int(input())
lists_b = []

# 输入第二个数组
for i in range(m):
    input_str = input()
    elements = list(map(int, input_str.split()))
    lists_b.append(elements)

result = []

# 遍历第二个数组中的每个范围
for range_vals in lists_b:
    a, b, c, d = range_vals  # a < x < b, c < y < d
    sum_val = 0
    # 遍历第一个数组中的每个点
    for point in lists:
        x, y, value = point
        # 判断点是否在范围内
        if a <= x <= c and b <= y <= d:
            sum_val += value
    result.append(sum_val)

for i in (result):
    print(i)