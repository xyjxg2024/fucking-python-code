a=int(input())
for i in range(a):
    list_a=[]
    x,y=map(int,input().split())
    num_a=2**(x+1)
    num_b=num_a-y
    ans=0
    while num_a==num_b:
        ans+=1
        if num_a>num_b:
            if num_a//2==0:
                num_b+=num_a//2
                num_a=num_a//2
            else:
                num_a+=num_b//2
                num_b=num_b//2
        else:
            if num_b//2==0:
                num_a+=num_b//2
                num_b=num_b//2
            else:
                num_b+=num_a//2
                num_a=num_a//2