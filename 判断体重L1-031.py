a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    d=(b-100)*0.9*2
    if abs(c-d)<d*0.1 :
        print("You are wan mei!")
    elif c-d<0 and abs(c-d)>=d*0.1 :
        print("You are tai shou le!")
    elif c-d>0 and abs(c-d)>=d*0.1:
        print("You are tai pang le!")

#b是身高c是真实体重d是标准体重
#d=b-100*0.9
#|c-d|<d*0.1为完美
#c-d>d*0.1时
