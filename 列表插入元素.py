a = int(input())  # 输入列表的长度
us_ip = input()  # 输入列表的元素
abc = us_ip.split()
list_a = list(abc)
b = int(input())  # 输入要插入的位置
c = int(input())  # 输入要插入的元素


if b < 1 or b > len(list_a):  # 检查插入位置是否合法
        print("error")
else:
        list_a.insert(b-1, c)
        print(" ".join(map(str, list_a)))
