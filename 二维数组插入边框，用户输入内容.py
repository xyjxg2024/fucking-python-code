list_a=[['*'for _ in range(12)]for _ in range(12)]
for i in range(1,11):
    x=input().strip()
    for j in range(1,11):
        list_a[i][j]=x[j-1]
for i in range(12):
    for j in range(12):
        print(list_a[i][j],end='')
