e=(a,b,c)= map(int, input().split())
if a<b and a<c and b<c:
    print(a,b,c)
elif a>b and a<c and b<c:
    print(b,a,c)
elif a<b and a>c and b>c:
    print(c,a,b)
elif b>a and b>c and c>a:
    print(a,c,b)
elif a>b and a>c and b>c:
    print(c,b,a)
elif a>b and a>c and c>b:
    print(b,a,c)
else:
    print(a,b,c)
