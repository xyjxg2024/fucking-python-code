a,b,c,d,e,f,g,h,i,j= map(int, input().split())
k= int(input())
list_a=a,b,c,d,e,f,g,h,i,j
m=0
for i in list_a:
 if k+30>=i:
  m+=1
print(m)