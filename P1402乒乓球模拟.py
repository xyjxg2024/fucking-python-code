x = []
a = 0
b = 0
while True:
    line = input().strip()
    if 'E' in line:
        e = line.index('E')
        x.append(line[:e])
        break
    else:
        x.append(line)
x = ''.join(x)
for i in range(len(x)):
    if x[i]=='W':
        a+=1
    elif x[i]=='L':
        b+=1
    if (a>=11 or b>=11) and (a-b>=2 or b-a>=2):
        print(f"{a}:{b}")
        a=0
        b=0
if x=='':
    print("0:0")
else:
    print(f"{a}:{b}")
print()
a=0
b=0
for i in range(len(x)):
    if x[i]=='W':
        a+=1
    elif x[i]=='L':
        b+=1
    if (a>=21 or b>=21) and (a-b>=2 or b-a>=2) :
        print(f"{a}:{b}")
        a=0
        b=0
if x=='':
    print("0:0")
else:
    print(f"{a}:{b}")