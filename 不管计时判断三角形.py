def sjx(n):
    a1 = n // 3 + 1
    for a in range(1, a1):
        limit_b = (n - a) // 2 + 1
        for b in range(a, limit_b):
            c = n - a - b
            if a + b > c and a + c > b and b + c > a:
                return "YES"
    return "NO"
a = int(input())
results = [sjx(int(input())) for i in range(a)]
#看到这个代码的人，你真是个帅逼啊
for result in results:
    print(result)
