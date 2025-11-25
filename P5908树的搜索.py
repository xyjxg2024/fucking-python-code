s = input().split()
n, d = int(s[0]), int(s[1])
se = set()
list_a = [1]
l = list()
for i in range(n - 1):
    s = input().split()
    s = [int(s[0]), int(s[1])]
    s = sorted(s)
    l.append(s)
j = 0
while j < d:
    cnt = len(list_a)
    size = len(l)
    for i in range(size):
        if l[i][0] in list_a[:cnt]:
            list_a.append(l[i][1])
    for i in list_a:
        se.add(i)
    list_a = list_a[cnt:]
    j += 1
print(len(se) - 1)
