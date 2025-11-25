def gcd(x, y):
    if x == 0: return y
    if y == 0: return x
    return gcd(x, y%x) if x < y else gcd(y, x%y)

a,b,c=map(int,input().split())
x=a*b/gcd(a,b)
y=x*c/gcd(x,c)
print(int(y))