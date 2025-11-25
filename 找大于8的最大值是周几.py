def main():
    # 初始化变量
    unhappy_day = 0
    max_unhappiness = -1

    # 遍历7天的数据
    for day in range(1, 8):
        # 读取每天的上课时间
        school_time, mother_time = map(int, input().split())
        total_time = school_time + mother_time
        # 计算不高兴的程度
        if total_time > 8:
            unhappiness = total_time - 8
            # 更新最不高兴的一天
            if unhappiness > max_unhappiness:
                max_unhappiness = unhappiness
                unhappy_day = day

    # 输出结果
    print(unhappy_day)


if __name__ == "__main__":
    main()
