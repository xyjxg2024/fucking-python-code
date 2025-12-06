#第七章第一题:
a=input()
b=a.replace('py','python')
print(b)

#第七章第二题:
# list_a=[]
# while True:
#     x=input()
#     if x=='':
#         break
#     else:
#         list_a.append(eval(x))
# num=0
# for i in list_a:
#     num+=i
# print(num/len(list_a))

#第七章第三题:
# import random
# list_a=[[],[],[]]
# list_b=[1,2,3,4,5,6,7,8]
# for i in list_b:
#     n=random.randint(0,2)
#     list_a[n].append(i)
# print(list_a)

#第八章第一题:
# def jianfa(x,y):
#     if x<y:
#         raise BaseException('被减数不能小于减数')
#     else:
#         return x-y
# try:
#     a=eval(input("请输入："))
#     b=eval(input("请输入："))
#     print(jianfa(a,b))
# except:
#     print("被减数不能小于减数")

#第八章第二题：
# def num(x,y):
#     if y==0:
#         raise BaseException('除数不为0')
#     else:
#         print(x/y)

# n=eval(input())
# a=eval(input())
# b=eval(input())
# for i in range(a,b):
#     try:
#         num(n,i)
#     except:
#         print("除数不为0")

#第八章第三题:
# def num(n):
#     if n==0:
#         raise BaseException('除数不为0')
#     else:
#         return 100/n
#
# a=eval(input())
# while True:
#     try:
#         print(num(a))
#         break
#     except:
#         print("除数不为0")
#         a=int(input())

# #第十章第一题:
class Dog:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def wangwang(self):
        print("wang! wang!")
dog=Dog("旺财","黄色",10)
dog.wangwang()

# #第十章第二题:
class student:
    def __init__(self,name=age,chinese,math,english):
        self.name=name
        self.age=age
        self.chinese=chinese
        self.math=math
        self.english=english
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.chinese,self.math,self.english)
zm = student('zhangming',20,69,88,100)
print(zm.get_name(),zm.get_age(),zm.get_course())

#第十章第三题:
class HighSchoolStudent(student):
    def __init__(self,name,age,chinese,math,english,chemistry, physics,biology, history,politics):
        student.__init__(self,name,age,chinese,math,english)
        self.chemistry=chemistry
        self.physics=physics
        self.biology=biology
        self.history=history
        self.politics=politics
    def get_average(self):
        return sum([self.chinese,self.math,self.english,self.chemistry,self.physics,self.biology,self.history,self.politics])/8
    def get_max(self):
        return max(self.chinese,self.math,self.english,self.chemistry,self.physics,self.biology,self.history,self.politics)
zm = HighSchoolStudent('zhangming',20,69,88,100,75,83,95,87,62)
print(zm.name,zm.get_average(),zm.get_max())
while :
