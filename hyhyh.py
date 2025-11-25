a = int(input())
list_a =[0]+sorted(list(map(int, input().split())))
n=int(input())
for _ in range(n):
    x = int(input())
    l,r=0,len(list_a)-1
    while l<=r:
        mid = (l + r) // 2
        if x<list_a[mid]:
            r=mid-1
        else:
            l=mid+1
    print(l-1)