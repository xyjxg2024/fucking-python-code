import random


def lottery():
    # 生成一个0到1之间的随机数
    number = random.random()

    # 判断中奖概率
    if number < 0.000001:
        return "一等奖"
    elif number < 0.1:
        return "二等奖"
    else:
        return "三等奖"


# 初始化计数器
second_prize_count = 0

# 循环十万次抽奖
for i in range(100000):
    result = lottery()
    print(f"第{i + 1}次抽奖，恭喜你，获得了{result}")

    # 如果中了二等奖，增加计数器
    if result == "二等奖":
        second_prize_count += 1

    # 如果中了一等奖，结束程序
    if result == "一等奖":
        print("恭喜你抽中了一等奖，程序结束。")
        break
else:
    print("十万次抽奖均未抽中一等奖。")

# 输出中了多少次二等奖
print(f"在本次抽奖中，你一共中了{second_prize_count}次二等奖。")
