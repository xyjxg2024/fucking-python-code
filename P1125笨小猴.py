def is_prime(n):
    """判断一个数是否为质数"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

s = str(input())
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 找出出现次数最多和最少的字符及其次数
most_common_char = max(char_count, key=char_count.get)
least_common_char = min(char_count, key=char_count.get)
most_common_count = char_count[most_common_char]
least_common_count = char_count[least_common_char]

# 计算次数之差
d = most_common_count - least_common_count

# 判断并输出结果
if is_prime(d):
    print("Lucky Word")
    print(d)
else:
    print("No Answer")
    print(0)
