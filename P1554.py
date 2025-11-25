a,b=map(int,input().split())
c={str(i):0 for i in range (10)}
for i in range(a,b+1):
    str(i)
    for j in list(str(i)):
        if j in c:
            c[j]+=1
        else:
            c[j]=1
for n in c.values():
 print(n,end=" ")