
a = int(input())  # 输入列表的长度
us_ip = input()  # 输入列表的元素
abc = us_ip.split()
list_a = list(abc)
b = int(input())  # 输入要删除的位置
if b < 2 or b > len(list_a)+1:  # 检查删除位置是否合法
        print("error")
else:
        del list_a[b-2]
        print(" ".join(map(str, list_a)))