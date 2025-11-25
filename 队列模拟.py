#灌伤害，骗骗花
#拉开距离回回拉
#给压压，再开大
#压力有点大骚钢
#小馒头，压力大
#压力大如骚钢庭
#压力大，压力雷
#压力像一个大爆雷
from collections import deque
a,b=map(int,input().split())
list_a=[0]+list(map(int,input().split()))
q=deque(range(1,a+1))
while len(q)>1:
    x=q.popleft()
    list_a[x]-=b
    if list_a[x]>0:
        q.append(x)
print(q[0])