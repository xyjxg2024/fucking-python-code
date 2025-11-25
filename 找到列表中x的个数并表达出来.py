def get_hash_positions(blocks):
    positions = []
    for index, char in enumerate(blocks):
        if char == '#':
            positions.append(str(index))  # 保持索引从0开始计数
    return " ".join(positions)

# 读取输入
N = int(input())
blocks = input()

# 获取#的位置序列
output = get_hash_positions(blocks)

# 输出结果
print(output)
