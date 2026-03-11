list_a=list(map(int,input().split()))
list_b=[]
num=0
ans=0
for i in range(4):
    list_b.append(list_a[i])
num_max=max(list_b)
for i in range(4):
    if num_max-list_b[i]>list_a[-1]:
        num+=1
        ans=i+1
    if list_b[i]<list_a[-2]:
        num+=1
        ans=i+1
if  num>1:
    print(f"Warning: please check all the tires!")
elif num==1:
    print(f"Warning: please check #{ans}!")
else:
    print("Normal")
# print(num)
# print(ans)
# print(list_b)
# # 242 251 231 248 230 20