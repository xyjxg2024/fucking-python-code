n,m,p,q=map(int,input().split())
list_a=[i for i in range(m+n+5)]
rank=[0]*(m+n+5)
j=0
k=0
def find(n):
    if list_a[n] != n:
        list_a[n] = find(list_a[n])  # 路径压缩
    return list_a[n]

# 并集函数（按秩合并）
def union(x, y):
    far_x = find(x)
    far_y = find(y)
    if far_x != far_y:
        # 按秩合并，将秩较小的树合并到秩较大的树上
        if rank[far_x] > rank[far_y]:
            list_a[far_y] = far_x
        else:
            list_a[far_x] = far_y
            if rank[far_x] == rank[far_y]:
                rank[far_y] += 1
union(1,n+1)
for i in range(p):
    x,y=map(int,input().split())
    if find(x)!=find(y):
        union(x,y)
for i in range(q):
    x,y=map(int,input().split())
    x*=-1
    y*=-1
    if(find(x+n)!=find(y+n)):
        union(x+n,y+n)
for i in range(1,n+1):
    if find(i)==find(1):
        j+=1
for i in range(n+1,n+m+1):
    if find(i)==find(n+1):
        k+=1
l=min(k,j)
print(l)

