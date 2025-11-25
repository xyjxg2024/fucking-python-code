a,b=map(int,input().split())
c=0
d=[]
for i in range(a,b+1):
    if  (i%4==0 and i%100 !=0) or i % 400 ==0:
        c+=1
        d.append(str(i))
print(c)
print(" ".join(d))
x=int(input())