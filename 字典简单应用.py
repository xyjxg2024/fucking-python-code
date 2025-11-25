a,b=map(int,input().split())
l=0
list_a=list(map(int,input().split()))
dict_a={}
for i in list_a:
    if i in dict_a:
        dict_a[i]+=1
    else:
        dict_a[i]=1
dict_a=sorted(dict_a.items(),key=lambda x:x[1],reverse=True)
for i in list_a:
    if i + b in dict_a:
        l+=dict_a[i+b]
print(l)