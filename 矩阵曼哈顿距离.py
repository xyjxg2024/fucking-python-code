hang = 5
lie = 5
a = []
for _ in range(hang):
    row = list(map(int, input().split()))
    a.append(row)

b = []
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 1:
            b.append((i+1, j+1))

if b:
    for pos in b:
        xxx = abs(3 - pos[0]) + abs(3 - pos[1])
        print(xxx)
