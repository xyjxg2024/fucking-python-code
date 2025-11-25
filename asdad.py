a = int(input())
list_a =[0]+sorted(list(map(int, input().split())))
x = int(input())
for _ in range(x):
    n=int(input())
    l, r = 0,a
    while l <= r:
        mid = (l + r) // 2
        if list_a[mid] <= n:
            l = mid + 1
        else:
            r = mid - 1
    print(l-1)