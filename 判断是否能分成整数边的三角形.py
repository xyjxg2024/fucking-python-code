t = int(input())
results = []

for _ in range(t):
    n = int(input())
    if n>4 or n==3:
        results.append("YES")
    else:
        results.append("NO")
for result in results:
    print(result)