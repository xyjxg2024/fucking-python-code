a, b = map(int, input().split())
b_str = str(b)
total_count = 0
for i in range(1,a + 1):
    count = 0
    for char in str(i):
        if char == b_str:
            count += 1
    total_count += count

print(total_count)