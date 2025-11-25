a, b = map(int, input().split())
list_a = [0] * 21  # 存储当前组合
list_b = [0] * 21   # 标记数组

def dfs(x, y):
    if x == b:
        formatted = ''.join(["{:>3}".format(num) for num in list_a[1:b+1]])
        print(formatted)
        return
    for i in range(y + 1, a + 1):
        if list_b[i] == 0:
            list_b[i] = 1
            list_a[x + 1] = i
            dfs(x + 1, i)
            list_b[i] = 0

dfs(0, 0)