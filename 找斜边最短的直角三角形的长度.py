import math
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
m_d = 999999
for i in range(n):
    for j in range(i + 1, n):
        d = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
        if d < m_d:
            m_d = d
print(f"{m_d:.2f}")
