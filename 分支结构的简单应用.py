number=int(input())
if number%2==0 and 4<number<=12:
    print(1,end=" ")
else:
    print(0,end=" ")
if number%2==0 or 4<a<=12:
    print(1,end=" ")
else:
    print(0,end=" ")
if number%2==0 and (4>=number or number>12):
    print(1,end=" ")
elif number%2==1 and 4<number<=12:
    print(1,end=" ")
elif number%2==0 and 4<number<=12:
    print(0,end=" ")
elif number%2==1 and (4>=number or number>12):
    print(0,end=" ")
if number%2==0 or 4<number<=12:
    print(0,end=" ")
else:
    print(1,end=" ")