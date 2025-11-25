import math
a=int(input())
b,c= map(int, input().split())
d,e= map(int, input().split())
f,g= map(int, input().split())
x=math.ceil(a/b)
y=math.ceil(a/d)
z=math.ceil(a/f)
b1=x*c
b2=y*e
b3=z*g
list_a=(b1,b2,b3)
list_b=sorted(list_a)
print(list_b[0])


