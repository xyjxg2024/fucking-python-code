a,b=(int(i.strip()) for i in input().split())
s=0
for i in range(a,b+a):
	if i%7!=0 and i%7!=6:
          s+=250
print(s)