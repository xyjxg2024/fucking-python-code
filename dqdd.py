# list_a=list(map(str,input().split()))
list_a = list(input().rstrip('\n'))  # 只删除换行符，保留其他空格
for i in range(len(list_a)):
    if "6666666666" in list_a[i]:
        list_a[i]="27"
    elif "6666" in list_a[i]:
        list_a[i]="9"
print(' '.join(list_a))
#it is so 666 really 6666 what 66666 else can I say 6666666666
