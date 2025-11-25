a = int(input())
b = list(map(int, input().split()))
c = sorted(b)
c = c[1:-1]
e = sum(c)
average = e / (a - 2)
d="{:.2f}".format(average)
print(d)
