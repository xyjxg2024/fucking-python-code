def main():
    a, b = map(int, input().split())
    list_a = list(map(int, input().split()))
    freq = [0] * (1000050)
    l = 0
    num = 0
    best_len = 1e9+7
    ansl = 0
    ansr = -1

    for r in range(a):
        # 把右端点数字加入窗口
        if freq[list_a[r]] == 0:
            num += 1
        freq[list_a[r]] += 1

        # 当不同数字个数 ≥ b 时，尝试收缩左端
        while num >= b:
            if r - l + 1 < best_len:
                best_len = r - l + 1
                ansl, ansr = l, r
            # 移除左端点
            freq[list_a[l]] -= 1
            if freq[list_a[l]] == 0:
                num -= 1
            l += 1
    print(ansl + 1, ansr + 1)


if __name__ == '__main__':
    main()