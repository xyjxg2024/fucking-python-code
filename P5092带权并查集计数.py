def find(x):
    if fa[x] != x:#判断
        far_x = fa[x]
        fa[x] = find(fa[x])#递归查找根节点
        root[x] += root[far_x]#计算当前节点带有权值大小
    return fa[x]#递归操作改参数

def union(x, y):
    fx = find(x)#找根节点
    fy = find(y)
    if fx != fy:#判断
        fa[fx] = fy#合并操作f并入y
        root[fx] =  size[fy]#更换根节点大小
        size[fy] += size[fx]#累加树的节点的权值

a = int(input())
fa = [i for i in range(30005)]
root = [0] * 30005
size = [1] * 30005

for _ in range(a):
    list_a = input().split()
    if list_a[0] == 'M':
        x, y = int(list_a[1]), int(list_a[2])
        union(x, y)
    elif list_a[0] == 'C':
        x = int(list_a[1])
        find(x)
        print(root[x])