def calculate_averages(n, k):
    # 计算 A 类数的和
    a_sum = 0
    a_count = 0
    for num in range(1, n + 1):
        if num % k == 0:
            a_sum += num
            a_count += 1
    # 计算 A 类数的平均数
    a_average = a_sum / a_count

    # 计算 B 类数的和
    b_sum = 0
    b_count = 0
    for num in range(1, n + 1):
        if num % k!= 0:
            b_sum += num
            b_count += 1
    # 计算 B 类数的平均数
    b_average = b_sum / b_count

    return round(a_average, 1), round(b_average, 1)

# 输入 n 和 k
n, k = map(int, input().split())

# 计算并输出结果
a_avg, b_avg = calculate_averages(n, k)
print(f"{a_avg} {b_avg}")
