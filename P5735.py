import math
x1,y1=(map(float,input().split()))
x2,y2=(map(float,input().split()))
x3,y3=(map(float,input().split()))
ab=math.sqrt(((x2-x1)**2)+(y2-y1)**2)
bc=math.sqrt(((x3-x2)**2)+(y3-y2)**2)
ca=math.sqrt(((x3-x1)**2)+(y3-y1)**2)
z=ab+bc+ca
z1 = "{:.2f}".format(z)
print(z1)