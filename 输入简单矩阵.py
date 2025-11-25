def input_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row_str = input(f"请输入第{_ + 1}行的{cols}个数，用空格隔开: ")
        matrix.append([int(num) for num in row_str.split()])
    return matrix

rows = 5  # 矩阵的行数
cols = 5  # 矩阵的列数
matrix = input_matrix(rows, cols)

for row in matrix:
    print(row)