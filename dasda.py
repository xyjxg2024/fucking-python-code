c=[126,33,64,35,36,37,94,38,42,40,41,95]
t=int(input())
while t:
    t=t-1
    flag=0
    d=set()
    x=set()
    sz=set()
    ts=set()
    s=input()
    n=len(s)
    hf=True
    for si in s:
        if si>='A' and si<='Z':
            d.add(si)
        elif si>='a' and si<='z':
            x.add(si)
        elif si>='0' and si<='9':
            sz.add(si)
        elif ord(si) in c:
            ts.add(si)
        else:
            hf=False
    if hf==False:
        print(0)
        continue
    count=0
    if len(d)>0:
        count+=1
    if len(x)>0:
        count+=1
    if len(sz)>0:
        count+=1
    if len(ts)>0:
        count+=1
    if n>=12 and (count>=4 or(count>=3 and len(ts)>=3)):
        print(3)
    elif n>=8 and count>=2:
        print(2)
    elif n>=6:
        print(1)
    else:
        print(0)



