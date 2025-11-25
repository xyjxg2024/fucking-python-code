a,b=map(int,input().split())
x=[]
for i in range(a):
    x.append(int(input()))
x=sorted(x)
def fen(n):
    an=x[0]
    bn=1
    for i in range(1,a):
        if x[i]-an>=d:
            an=x[i]
            bn+=1
            if bn==b:
                return True
    return False
l,r=1,1000000000//(b-1)+1
mmax=0
while l<=r:
    d=l+(r-l)//2
    if fen(d):
        best=d
        l=d+1
    else:
        r=d-1
print(best)