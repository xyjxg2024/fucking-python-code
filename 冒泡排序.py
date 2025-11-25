a,b,c,d,e,f,g,h,i,j= map(int, input().split())#十个数
list_a=[a,b,c,d,e,f,g,h,i,j]

def list(list_a):
    for i in range(len(list_a)-1):
     for x in range(0, len(list_a) - 1):
        if list_a[x] > list_a[x + 1]:
            list_a[x + 1], list_a[x] = list_a[x], list_a[x + 1]
    print(list_a)
list(list_a)
