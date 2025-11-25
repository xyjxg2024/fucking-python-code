a,b=map(int,input().split())
x=[]
nx=[1,0,-1,0]
ny=[0,1,0,-1]
for _ in range(a):
    list_x=list(map(int,input().strip()))
    for i in range(len(list_x)):
        if i=='.':
            list_x[i]=1
        elif i=='X':
            list_x[i]=0
        else:
            list_x[i]=2
    x.append(list_x)
n=int(input())

for i in range(n):
    m=str(input())
    if m=='NORTH':
        nm=1
    elif m=='SOUTH':
        nm=2
    elif m=='EAST':
        nm=3
    elif m=='WEST':
        nm=4
def dfs(x,y,z):
    if