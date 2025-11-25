a,b,c= map(int, input().split())
x=input()
list_a =a,b,c
z=sorted(list_a)
d=z[0]
e=z[1]
f=z[2]
if  x=="ABC":
     print(d,e,f)
elif x=="BAC":
     print(e,d,f)
elif x=="CAB":
      print(f,d,e)
elif x=="ACB":
     print(d,f,e)
elif x=="BCA":
       print(e,f,d)
elif x=="CBA":
      print(f,e,d)






