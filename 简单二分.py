a,b=map(int,input().split())
list_a=[0]
list_b=[0]
list_a+=list(map(int,input().split()))
list_b+=list(map(int,input().split()))
def find(x):
    l=1
    r=a
    while l<r:
        mid=(l+(r-1))//2
        if list_a[mid]>=x:
            r=mid
        else:
            l=mid+1
    if  list_a[l]==x:
        return l
    else:
        return -1
for i in range (1,len(list_b)):
    ans=find(list_b[i])
    print(ans,end=' ')