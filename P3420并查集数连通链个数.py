def find(x):
    if list_a[x] != x:
        list_a[x] = find(list_a[x])
    return list_a[x]

def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx != ry:
        list_a[ry] = rx

a=int(input())
list_a=[i for i in range(a+5)]
list_b=[0]
x=0
for i in range(a):
    x=int(input())
    list_b.append(x)

for i in range(1,a+1):
    if list_b[i]!=i:
        union(i, list_b[i])

xx=set()
for i in range(1,a+1):
    yy=find(i)
    xx.add(yy)

print(len(xx))