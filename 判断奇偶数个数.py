a=int(input())
b = list(map(int, input().split()))
c=0
d=0
for i in b:
    if i%2==0:
        c+=1
    else:
        d+=1
print(f"{d} {c}")
