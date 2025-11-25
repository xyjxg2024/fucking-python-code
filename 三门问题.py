#模拟三门问题
import random as rd
#n:模拟次数,m:中奖次数
n=100000
m=0
for i in range(n):
     #车位于的门号
   car=rd.randint(0,2)
   #人随机选择一个门
   door=rd.randint(0,2)
   #主持人展示空门
   empties={0,1,2}-{car,door}
   empty=rd.choice(list(empties))
   #换另一扇门
   choose=({0,1,2}-{door,empty}).pop()
   #判断是否中奖
   if choose==car:
       m+=1
p=m/n
print(f'中奖概率:{float(p):.2f}')
