e,f= map(int, input().split())
a,b,c=1700,1800,1900
list_a=[1,3,5,7,8,10,12]
list_b=[4,6,9,11]
list_c=[2]
if e%4==0 and e!=a and e!=b and e!=c and f in list_c:
 print("29")
elif e%4!=0 and f in list_b:
 print("30")
elif e%4!=0 and f in list_a:
 print("31")
elif e%4==0 or e==b or e==c and f in list_c:
 print("28")
