def generate_triangle(n):
    triangle = []  # 初始化一个空列表，用于存储每一行的数字字符串
    num = 1        # 初始化数字从1开始
    for i in range(n, 0, -1):  # 外层循环，从 n 到 1 递减
        line = ''  # 初始化当前行的字符串为空
        for j in range(i):  # 内层循环，控制当前行的数字个数
            line += f'{num:02}'  # 将当前数字格式化为两位数，不足两位前面补零，并添加到当前行字符串中
            num += 1  # 数字递增
        triangle.append(line)  # 将当前行字符串添加到三角形列表中
    return '\n'.join(triangle)  # 将所有行用换行符连接成一个字符串返回

# Read input
n = int(input().strip())  # 读取输入的正整数 n

# Print the result
print(generate_triangle(n))  # 调用函数生成三角形并打印结果
