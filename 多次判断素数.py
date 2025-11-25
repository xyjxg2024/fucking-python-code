def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True
# 读取输入
N = int(input())
numbers = [int(input()) for _ in range(N)]
# 判断每个数是否为素数并输出结果
for number in numbers:
    if is_prime(number):
        print("Yes")
    else:
        print("No")