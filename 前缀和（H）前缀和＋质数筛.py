def prime(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    else:
        return 1
n=int(input())
list_n=list(map(int,input().split()))
q=int(input())
list_a=[0]*(n+1)
list_b=[0]*(n+1)
list_c=[]
for i in range(1,n+1):
    list_b[i]=list_b[i-1]+(1 if prime(list_n[i-1]) else 0)
for i in range(q):
    l,r=map(int,input().split())
    c=list_b[r]-list_b[l-1]
    list_c.append(c)
for i in list_c:
    print(i,end=" ")