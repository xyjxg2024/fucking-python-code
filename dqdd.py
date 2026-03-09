list_a = list(input().strip())
list_b = list(input().strip())

# 倒序遍历，删除不影响前面的索引
for i in range(len(list_a) - 1, -1, -1):
    if list_a[i] in list_b:
        list_a.pop(i)  # 或 list_a.remove(list_a[i])，但 pop(i) 更高效

list_c = ''.join(list_a)
print(list_c)