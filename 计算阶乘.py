n=int(input())
if n==1:
    print("1")
elif n>=1:
    b=1
    a=1
    for i in range(2,n+1):
        a*=i
        b+=a
    print(b)
