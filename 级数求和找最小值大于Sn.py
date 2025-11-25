a = int(input())
b =100000000
c = 0
for i in range(1, b):
    c += 1 / i
    if c > a:
        print(i)
        break
