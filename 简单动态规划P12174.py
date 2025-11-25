# 读取序列长度
a = int(input())
# 读取整数序列
list_a = list(map(int, input().split()))

if a == 0:
    print(0)  # 处理空序列的特殊情况
else:
    max_a = 1  # 全局最长序列长度记录器
    # 创建二维DP数组，dp[i][j]表示：
    # 以list_a[i]结尾，且查看前j个位置时的最长递增序列长度
    dp = [[1] * a for _ in range(a)]

    # 外层循环：遍历序列中的每个元素（从第二个开始）
    for i in range(1, a):
        # 内层循环：控制查看前驱元素的距离
        # j表示查看前驱元素的偏移量，范围是[1, i]
        for j in range(1, i + 1):
            x = i - j  # 计算实际比较的前驱元素位置

            # 如果当前元素大于前驱元素
            if list_a[i] > list_a[x]:
                # 状态转移：当前长度 = 前驱位置的对应偏移量长度 + 1
                dp[i][j] = dp[x][j] + 1

                # 更新全局最大值
                if dp[i][j] > max_a:
                    max_a = dp[i][j]

    print(max_a)  # 输出最终结果
#6
#3 5 4 7 6 7
