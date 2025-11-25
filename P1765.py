a=str(input())
b=0
for i in a:
    if i=="a" or i=="d" or i=="g" or i=="j"or i=="m" or i=="p" or i=="t" or i=="w" or i==" " :
         b+=1
    elif i=="b" or i=="e" or i=="h" or i=="k" or i=="n" or i=="q" or i=="u" or i=="x":
         b+=2
    elif i=="c" or i=="f" or i=="i" or i=="l" or i=="o" or i=="r" or i=="v" or i=="y":
         b+=3
    elif i=="s" or i=="z":
        b+=4
print(b)