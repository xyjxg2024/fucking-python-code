# 思路：
#
#     输入
#         输入人数与命令条数
#         使用for循环输入每个人的朝向与名称
#     模拟（循环n次）
#         输入第i条指令的方向与名称
#         判断是顺时针或逆时针
#             如果是顺时针：序号 --
#             否则是逆时针：序号 ++
#         判断序号是否超过限制(大于总人数或小于0)
#             如果小于0：序号加上总人数
#             否则大于总人数：序号减少总人数
#     输出：输出序号所对应的人的名称
x,y=map(int,input().split())
z=0
list_a=[]
for i in range(x):
    xx=list(map(str,input().split()))
    list_a.append(xx)
for i in range(y):
    a,b=map(int,input().split())
    if a==0:
        if list_a[z][0]=="1":
            if z+b>x-1:
                z=z+b-x
            else:
                z=z+b
        elif list_a[z][0]=="0":
            if z-b<0:
                z=z-b+x
            else:
                z=z-b
    elif a==1:
        if list_a[z][0]=="1":
            if z-b<0:
                z=z-b+x
            else:
                z=z-b
        elif list_a[z][0]=="0":
            if z+b>x-1:
                z=z+b-x
            else:
                z=z+b
print(list_a[z][1])