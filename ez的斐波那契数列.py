def saogang(a):
    num= ((((1+5**0.5)/2)**a)-(((1-5**0.5)/2)**a))/(5**0.5)
    return  "{:.2f}".format(num)
a=int(input())
print(saogang(a))

