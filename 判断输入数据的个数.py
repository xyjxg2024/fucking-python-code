# 提示用户输入数据，并使用空格分隔每个数据项
user_input = input("请输入一些数据，用空格分隔: ")

# 将输入的字符串分割成列表
data_list = user_input.split()

# 计算列表的长度，即数据的数量
num_of_data = len(data_list)

# 输出数据的数量
print("你输入了", num_of_data, "个数据")
