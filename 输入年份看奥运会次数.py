def sai(a, b):
    s = 0
    w = 0
    for i in range(a, b + 1):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
            s += 1
        elif i % 2 == 0:
            w += 1
    return s, w
a, b = map(int, input().split())
s, w = sai(a, b)
print(s+w)

