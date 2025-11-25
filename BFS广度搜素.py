from collections import deque
a=int(input())
list_a=[]
list_a.append([0] * (a+2))
for i in range(a):
    x=list(map(int,input().split()))
    list_a.append([0]+x+[0])
list_a.append([0] * (a+2))
for i in range(len(list_a)):
    for j in range(len(list_a[i])):
        if list_a[i][j]==0:
            list_a[i][j]=2
def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        if x < 0 or x >= len(list_a) or y < 0 or y >= len(list_a[0]) or list_a[x][y] != 2:
            continue
        list_a[x][y] = 0
        queue.append((x + 1, y))
        queue.append((x - 1, y))
        queue.append((x, y + 1))
        queue.append((x, y - 1))
for i in range(len(list_a)):
    for j in range(len(list_a[i])):
        if(i==0 or i==len(list_a)-1 and j==0 or j==len(list_a[i])-1) :
            bfs(i,j)
for i in range(1,len(list_a)-1):
    for j in range(1,len(list_a[i])-1):
        print(list_a[i][j],end=" ")
    print()