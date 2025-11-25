a=str(input())
b=str(input())
x=len(a)
y=len(b)
z=[]
n=0
if x>=y:
    for i in range(x-y):
        b='0'+str(b)
else:
    for i in range(y-x):
        a='0'+str(a)
for i in range(len(a)-1,-1,-1):
    m=int(a[i])+int(b[i])+n
    n=m//10
    z.append(m%10)
if n>0:
    z.append(n)
z.reverse()
for i in range(len(z)):
    print(z[i],end='')