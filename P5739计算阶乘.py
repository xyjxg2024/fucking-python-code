n=int(input())
def 阶乘(n):
    if n == 0:
        return 1
    else:
        return n * 阶乘(n-1)
print(阶乘(n))