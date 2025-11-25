t=int(input())
for _ in range(t):
    a=int(input())
    list_b=list(map(int,input().split()))
    minn=min(list_b)+min(list_b)
    mmax=max(list_b)+max(list_b)
    item_a = {}
    ans=-1
    if a<2:
        print(0)
    else:
        for k in range(minn,mmax):
            list_a = list_b.copy()
            for i in range(a-1):
                for j in range(i+1,a):
                    if list_a[i]!=False and list_a[j]!=False:
                        if list_a[i]+list_a[j] == k :
                            item_a[list_a[i]+list_a[j]] = 1
                            list_a[i] = False
                            list_a[j] = False
                        else:
                            item_a[list_a[i]+list_a[j]] += 1
                            list_a[i] = False
                            list_a[j] = False
                num=0
                for p in list_a:
                    if p==False:
                        num+=1
                ans=max(num/2,ans)
        print(ans)
