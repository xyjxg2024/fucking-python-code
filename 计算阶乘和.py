n=int(input())
def jiecheng(n):
    if n == 0:
        return 1
    else:
        return n * jiecheng(n-1)
def jiechenghe(n):
    jiechenghe=0
    for i in range(1,n+1):
        jiechenghe += jiecheng(i)
    return jiechenghe
print(jiechenghe(n))