def a(n, r):
    b_str = ""
    # 将 n 转换为基数 r 的表示
    while n > 0:
        b_str = str(n % r) + b_str
        n //= r
    # 计算 b_str 中所有数字的和
    sum_c = sum(int(c) for c in b_str)
    result = ""
    # 将 sum_c 转换为基数 r 的表示
    while sum_c > 0:
        result = str(sum_c % r) + result
        sum_c //= r
    return result
# 从用户输入中读取 n 和 r
n, r = map(int, input().split())
# 打印函数 a(n, r) 的结果
print(a(n, r))
