# class Student:
#     name=None
#     time=None
#
#     def say_hi(self,msg):
#         print(f"大家好，我是{self.name}，练习时长{self.time}的个人练习生，{msg}")
#
# std_1=Student()
# std_1.name="蔡虚琨"
# std_1.time="两年半"
# std_1.say_hi("你干嘛，哎哟")

# class Student:
#     # name=None
#     # age=None
#     # city=None
#     # (可以不写)
#     def __init__(self,x,y,z):
#         self.name=x
#         self.age=y
#         self.city=z
#         print('我真帅')
#         print(f"我叫{self.name},{y}岁,住在{z}")
#
# std=Student("大帅比",20,"南京")


class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.age=y
        self.address=z
        print(f"第{i}个学生信息：【姓名：{self.name},年龄：{y}，地址：{z}】")

for i in range(1,11):
    x=input("请输入学生姓名：")
    y=input("请输入学生年龄：")
    z=input("请输入学生地址：")
    std=Student(x,y,z)
    if i<10:
        print(f"学生{i + 1}信息正在录入，总共有10个学生")
    continue