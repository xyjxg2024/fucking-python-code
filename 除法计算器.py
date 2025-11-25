a,b=map(int,input("请输入两个数并用空格隔开").split())
if b==0:
    print(f"{a}/{b}=Error")
elif b>0:
    c = a / b
    formatted_number = "{:.2f}".format(c)
    print(f"{a}/{b}={formatted_number}")
elif b<0:
    c = a / b
    formatted_number = "{:.2f}".format(c)
    print(f"{a}/({b})={formatted_number}")