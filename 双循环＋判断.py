a = int(input())
found = False

# 遍历可能的指数 j（从 1 开始）
for j in range(31,0,-1):  # 限制 j 的范围避免无限循环
    total = 0
    terms = []
    # 遍历可能的底数 i（从 1 开始）
    for i in range(1, 99999):  # 限制 i 的范围避免无限循环
        total += i ** j
        terms.append(f"{i}^{j}")
        if total == a:
            print("+".join(terms))
            found = True
            break
        elif total > a:
            break  # 如果和已经超过 a，换下一个 j
    if found:
        break

if not found:
    print(f"Impossible for {a}.")