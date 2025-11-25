# 读取输入的两个整数 a 和 b
a, b = map(int, input().split())

# 读取列表 list_a 并排序（升序）
list_a = sorted(list(map(int, input().split())))

# 读取列表 list_b（无需排序）
list_b = list(map(int, input().split()))

# 初始化答案 ans 为 0
ans = 0

# 遍历 list_b 中的每一个元素
for i in range(b):
    # 初始化二分查找的左右边界
    l = 0          # 左边界（初始为 0）
    r = a - 1       # 右边界（初始为 a-1，即 list_a 的最后一个索引）

    # 二分查找：在 list_a 中寻找 list_b[i] 的插入位置（最后一个 <= list_b[i] 的元素的位置）
    while l <= r:
        mid = (l + r) // 2  # 计算中间位置
        if list_a[mid] <= list_b[i]:
            l = mid + 1     # 如果 list_a[mid] <= list_b[i]，说明目标在右半部分
        else:
            r = mid - 1     # 否则，目标在左半部分

    # 二分查找结束后：
    # - r 是最后一个 <= list_b[i] 的元素的索引（可能为 -1，表示 list_b[i] 比所有 list_a 元素都小）
    # - l 是第一个 > list_b[i] 的元素的索引（可能为 a，表示 list_b[i] 比所有 list_a 元素都大）

    # 情况 1：list_b[i] 比 list_a 的所有元素都小（r == -1）
    if list_b[i] <= list_a[0]:
        # 最接近的是 list_a[0]，计算差值并累加到 ans
        ans += list_a[0] - list_b[i]

    # 情况 2：list_b[i] 比 list_a 的所有元素都大（l == a）
    elif l == a:
        # 最接近的是 list_a[-1]，计算差值并累加到 ans
        ans += list_b[i] - list_a[-1]

    # 情况 3：list_b[i] 在 list_a 的范围内
    else:
        # 比较 list_a[r]（最后一个 <= list_b[i] 的元素）和 list_a[l]（第一个 > list_b[i] 的元素）
        # 选择差值较小的那个，并累加到 ans
        ans += min(abs(list_a[r] - list_b[i]), abs(list_b[i] - list_a[l]))

# 输出最终的累加结果
print(ans)