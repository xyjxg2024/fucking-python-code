from datetime import datetime
# 获取当前时间
current_time = datetime.now()
# 打印当前时间的小时和分钟（格式为：HH:MM）
print("当前时间的小时和分钟：", current_time.strftime("%H:%M"))
# 你也可以输入一个具体的时间
input_time = input("请输入一个时间（格式：YYYY-MM-DD HH:MM:SS）：")
# 将输入的时间字符串转换为datetime对象
input_time_obj = datetime.strptime(input_time, "%Y-%m-%d %H:%M:%S")
# 打印输入时间的小时和分钟
print("你输入时间的小时和分钟：", input_time_obj.strftime("%H:%M"))
#########################################################################################
from datetime import datetime
# 获取当前时间
current_time = datetime.now()
# 打印当前时间的小时和分钟（格式为：HH:MM）
print("当前时间的小时和分钟：", current_time.strftime("%H:%M"))
# 你也可以输入一个具体的时间
input_time = input("请输入一个时间（格式：YYYY-MM-DD HH:MM:SS）：")
# 将输入的时间字符串转换为datetime对象
input_time_obj = datetime.strptime(input_time, "%Y-%m-%d %H:%M:%S")
# 打印输入时间的小时和分钟
print("你输入时间的小时和分钟：", input_time_obj.strftime("%H:%M"))
