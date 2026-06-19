# height = float(input("输入你的身高（米）："))
# weight = float(input("输入你的体重（千克）："))
# bmi = weight / (height ** 2)
# if bmi<18.5:
#     print("过轻")
# elif bmi>=18.5 and bmi<25:
#     print("正常")
# elif bmi>=25 and bmi<28:
#     print("过重")
# elif bmi>=28 and bmi<32:
#     print("肥胖")
# else:
#     print("严重肥胖")
# print(f"你的BMI是：{bmi:.2f}")


# liebiao=[1,2,3,98,5,6,7,8,9,10]
# liebiao.append(4)
# liebiao.remove(1)  
# print(liebiao)

# zidian={"xuehao":121313,"name":"张三","age":18}
# print(zidian["xuehao"])
# print(zidian.values())


# avg=0
# number=0
# bool1=True
# while bool1:
#     temp=(input("请输入你要计算的数字："))
#     if temp=='p':
#         break
#     else:
#         temp=int(temp)
#     avg+=temp
#     number+=1
# print(f"你输入的数字平均值是：{avg/number:.2f}")


# print("今年是{0}年,今年的生肖是{1}年".format(2026,"马"))
# a=float(input("请输入数字："))
# print(f"你输入的数字为，{a:.2f}")


# def BMIjisuan(higth,  wegth):
#     return wegth/higth**2
# bmi1=BMIjisuan(178,78)
# print(f"你的BMI是：{bmi1}")

# class CatMess:
#     def __init__(self,name,age,job):
#         self.name=name
#         self.age=age
#         self.job=job
#     def eat(self):
#         print("小猫爱吃鱼")
#     def work(self):
#         print(f"小猫会{self.job}")

# cat1=CatMess("mimi",2,"抓老鼠")
# cat1.eat()
# cat1.work()
# print(cat1.job)
# print(cat1.name)
# print(cat1.age)

# class Student:
#     def __init__(self,name,num,chinese_score,math_score,english_score):
#          self.name=name
#          self.num=num
#          self.chinese_score=chinese_score
#          self.math_score=math_score
#          self.english_score=english_score
#     def all_score(self):
#         print(f"{self.name}的语文分数为{self.chinese_score}，数学分数为{self.math_score}，英语分数为{self.english_score}，\n"
#               f"总分为{self.chinese_score+self.math_score+self.english_score}")
# stu1=Student("张三",2021001,85,90,95)
# stu1.all_score()

# chengji={"语文":0,"数学":0,"英语":0}
# kemu=input("请输入科目名：")
# if kemu in chengji:
#     score=int(input("请输入分数："))
#     chengji[kemu]=score
#     print(chengji)
# else:
#     print("没有这个科目")


#类的继承
# class Employee():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def print_info(self):
#         print(f"员工姓名：{self.name}，员工编号：{self.id}")

# class FullTimeEmployee(Employee):
#     def __init__(self,name,id,monthly_salary):
#         super().__init__(name,id)
#         self.monthly_salary=monthly_salary
#     def yvexin(self):
#         print(f"全职员工的月薪为：{self.monthly_salary}")
# class PartTimeEmployee(Employee):
#     def __init__(self,name,id,daily_salary,work_days):
#         super().__init__(name,id)
#         self.daily_salary=daily_salary
#         self.work_days=work_days

#     def yvexin(self):
#         print(f"兼职员工的月薪为：{self.daily_salary*self.work_days}")
# xiaoming=FullTimeEmployee("小明",2021001,10000)
# xiaohuang=PartTimeEmployee("小黄",2021002,300,22)
# xiaoming.print_info()
# xiaoming.yvexin()
# xiaohuang.print_info()
# xiaohuang.yvexin()

# f=open("data.txt","r",encoding="utf-8")
# print(f.readline())
# print(f.readlines())
# for i in f.readlines():
#     print(i)
# print(f.read())
# with open("text3.txt","r+",encoding="utf-8") as f:
#     f.write("这是第一行文本\n")
#     f.write("这是第二行文本\n")
#     f.write("这是第三行文本\n")
#     f.seek(0)
#     print(f.read())
# with open("text2.txt","a",encoding="utf-8") as f:
#     f.write("这是追加的文本\n")
# with open("text2.txt","r",encoding="utf-8") as f:
#     print(f.read())

# try:
#     a=int(input("请输入一个整数："))
#     b=1/a
#     print(b)
# except ValueError:
#     print("请输入数字")
# except ZeroDivisionError:
#     print("不能除以0")
# finally:
#     print("程序结束了")
def sum1(a):
    res=a(10)
    print(f"输入的数字是{res}")
sum1(lambda v:v+10)