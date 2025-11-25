a = int(input())  # 初始进制
b = str(input())  # 初始值
c = int(input())  # 目标进制

# 先将输入值从a进制转换为10进制
decimal_value = int(b, a)

# 然后将10进制值转换为c进制
if c == 1:
    # 1进制特殊情况处理
    print('1' * decimal_value if decimal_value > 0 else '0')
else:
    # 使用内置函数转换并处理大写字母表示的数字
    converted = []
    if decimal_value == 0:
        converted.append('0')
    else:
        while decimal_value > 0:
            remainder = decimal_value % c
            if remainder < 10:
                converted.append(str(remainder))
            else:
                # 10以上用大写字母表示，如10=A,11=B等
                converted.append(chr(ord('A') + remainder - 10))
            decimal_value = decimal_value // c
    # 反转列表得到正确顺序
    converted.reverse()
    print(''.join(converted))
