a = int(input())
y = -1e11
list_a = [[0]*(a+2) for _ in range(a+2)]
x1=0
y1=0
for i in range(1, a+1):
    row = list(map(int, input().split()))
    for j in range(1, a+1):
        list_a[i][j] = row[j-1] + list_a[i-1][j] + list_a[i][j-1] - list_a[i-1][j-1]

for i in range(1, a+1):
    for j in range(1, a+1):
        for k in range(i, a+1):
            for l in range(j, a+1):
                now = list_a[k][l]- list_a[i-1][l]- list_a[k][j-1] + list_a[i-1][j-1]
                if now > y:
                    y = now
                    x1=k
                    y1=l
print(x1 ,y1)
print(y)