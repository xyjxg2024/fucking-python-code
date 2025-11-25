n, m = map(int, input().split())
a = list(map(int, input().split()))
b = set(map(int, input().split()))

segments = 0
prev = -2

for i in range(n):
    if a[i] not in b:
        if prev == i - 1:
            pass
        else:
            segments += 1
        prev = i

print(segments)