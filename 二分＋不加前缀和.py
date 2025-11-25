a ,b=map(int,input().split())
max_a=1e9
min_a=0
list_a=[]

for i in range(a):
    aa=int(input())
    list_a.append(aa)
list_a=sorted(list_a)

def fen(mid):
    x=0

    for i in list_a:
        if i<=mid:
            x+=1
        if  x>=b:
            return True
    return False
best=0
while min_a<=max_a:
    mid=(max_a+min_a)//2
    if fen(mid):
        best=mid
        max_a=mid-1
    else:
        min_a=mid+1

print(int(best))