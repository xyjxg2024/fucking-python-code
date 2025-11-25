def sieve_of_eratosthenes(n):
    # 初始化标记列表，所有数默认为True（可能的质数）
    prime = [True] * (n + 1)
    # 0和1既不是质数也不是合数
    prime[0] = prime[1] = False
    # 遍历到n的算术平方根
    for p in range(2, int(n ** 0.5) + 1):
        # 如果p是质数，则标记所有p的倍数为非质数
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    # 返回所有标记为True的索引，即质数列表
    return [p for p in range(2, n + 1) if prime[p]]

n=int(input())
# 使用函数获取1到100范围内的质数
print(sieve_of_eratosthenes(n))