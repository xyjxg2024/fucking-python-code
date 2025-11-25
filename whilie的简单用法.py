def cao(a):
    day=1
    while a >1:
        a//=2
        day += 1
    return day
a=int(input())
print (cao(a))



