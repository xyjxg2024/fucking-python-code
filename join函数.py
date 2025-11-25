t = int(input())
for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if heights[j] <= heights[i - 1]:
                dp[i] = min(dp[i], dp[j] + 1)

    result = dp[n] - 1

    # Custom binary representation
    custom_binary = ''
    while result > 0:
        custom_binary = str(result % 2) + custom_binary
        result //= 2

    print(custom_binary)
