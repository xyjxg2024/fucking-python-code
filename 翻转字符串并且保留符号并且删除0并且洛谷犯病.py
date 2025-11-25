list_a = list(input())
output = ''.join(list_a)
reversed_output = []
if list_a[0] != "-":
    for item in output:
        reversed_output.insert(0, item)
    caonima = ''.join(reversed_output)
    if caonima[0] != reversed_output[-1]:
        print(caonima)
elif list_a[0] == "-":
    for item in output[1:]:  # 跳过第一个字符 '-'
        reversed_output.insert(0, item)
    caonima = '-' + ''.join(reversed_output)  # 加上负号
    if caonima[1] != reversed_output[-1]:
        # 去掉负号后紧跟着的所有0
        while len(reversed_output) > 1 and reversed_output[0] == '0':
            reversed_output.pop(0)
        caonima = '-' + ''.join(reversed_output)
        print(caonima)