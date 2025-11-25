def find(x):
    if list_a[x] != x:
        list_a[x] = find(list_a[x])  # 路径压缩
    return list_a[x]

def union(x, y):
    rx=find(x)
    ry=find(y)
    if rx!=ry:
        list_a[ry]=rx

class road:
    def __init__(self,a,b,time):
        self.a=a
        self.b=b
        self.time=time

num=1
max=-1
n,m=map(int,input().split())
list_a=[i for i in range(n + 5)]
roads = [road(*map(int, input().split())) for _ in range(m)]
roads.sort(key=lambda r: r.time)
for i in roads:
    u=find(i.a)
    v=find(i.b)
    if u!=v:
        num+=1
        z=i.time
        union(i.a,i.b)
        if z>=max:
            max=z
if num==n:
    print(max)
else:
    print(-1)