list_a=list(map(str,input().strip()))
list_b=list(map(str,input().strip()))

print(list_a)
print(list_b)
for i in range(len(list_a)):
    for j in range(len(list_b)):
        if list_a[i]!=list_b[j]:
            list_a.remove(list_a[i])
list_c=''.join(list_a)
print(list_c)