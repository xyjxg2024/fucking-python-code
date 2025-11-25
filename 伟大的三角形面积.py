import math

a,b,c=map(float,input().split())
d=(1/2)*(a+b+c)
e=math.sqrt(d*(d-a)*(d-b)*(d-c))
round_e=round(e,1)
print(round_e)