a=int(input())
list_a=[True]*10005
list_b=[]
for i in range(2,10000):
    if list_a[i]:
        list_b.append(i)
    for j in list_b:
        if i*j>10000:
            break
        list_a[i*j]=False
        if i%j==0:
            break
list_c=[0]*len(list_b)
list_c[0]=list_b[0]
for i in range(1,len(list_b)):
    list_c[i]=list_c[i-1]+list_b[i]
for i in range(len(list_c)):
    if a>=list_c[i]:
        print(list_b[i])
    else:
        print(i)
        break